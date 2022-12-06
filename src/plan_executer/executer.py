import pathlib
import time

import oracledb
import queries
import re
from statistics import mean
import pathlib

un = 'user123'  # os.environ.get('PYTHON_USERNAME')
pw = 'password'  # os.environ.get('PYTHON_PASSWORD')
cs = 'localhost/xepdb1 '  # os.environ.get('PYTHON_CONNECTSTRING')

FILE_NAME = 'all_times'

QUERIES = [
    queries.QUERY_1,
    queries.QUERY_2,
    queries.QUERY_3,
    queries.QUERY_4,
    queries.QUERY_5,
    queries.QUERY_6
]

NUMBER_OF_TRIES = 5
SEPARATOR = f"\n\n{'-' * 30}\n\n"


def measure_query_time(task_query):
    times = []
    for i in range(NUMBER_OF_TRIES):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.FLUSH_BUFFER)
                start = time.time()
                cursor.execute(task_query)
                end = time.time()
                times.append(end-start)
            connection.rollback()
    return times


def run_plans(task_query):
    executed_plans = []
    for i in range(NUMBER_OF_TRIES):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.FLUSH_BUFFER)
                start = time.time()
                query = queries.EXPLAIN_PLAN.format(query=task_query)
                cursor.execute(query)
                end = time.time()
                print(end - start)
                r = cursor.execute(queries.SELECT_XPLAN).fetchall()
                r_string = '\n'.join(str(element[0]) for element in r)
                executed_plans.append(r_string)
            connection.rollback()
    return executed_plans


def get_number_of_rows_in_table(table_name):
    with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
        with connection.cursor() as cursor:
            table = table_name.replace("'", "")
            query = queries.COUNT_ROWS.format(table=table)
            row = cursor.execute(query).fetchone()
            return row[0]


def get_information_about_db():
    number_of_rows = []
    for table in queries.TABLES:
        number_of_rows.append(get_number_of_rows_in_table(table))

    return "\t".join(f"{table}: {rows}\n" for rows, table in zip(number_of_rows, queries.TABLES))


def create_full_db_information_string(before, after):
    return f"Stan bazy:\n Przed: {before} \n Po: {after}\n {SEPARATOR}\n"


def work_time_data(executed_plans):
    execution_times = []
    for plan in executed_plans:
        times = re.search('\\d\\d:\\d\\d:\\d\\d', plan).group()
        # print(time)
        h, m, s = times.split(':')
        time_in_seconds = int(h) * 3600 + int(m) * 60 + int(s)
        execution_times.append(time_in_seconds)

    avg_time = mean(execution_times)

    all_times_string = "\n".join(f"{time}s" for time in execution_times)
    time_data_string = f"Avg: {avg_time}s\n\n All times:\n{all_times_string}"
    return time_data_string


def create_full_string(executed_plans, time_data_string, task_name, count_of_queries):
    plans_string = SEPARATOR.join(
        f"EXECUTION {int(i % (len(executed_plans) / count_of_queries)) + 1}\n{executed_plans[i]}" for i in
        range(len(executed_plans)))
    times = SEPARATOR.join(
        f"Query {x + 1}: {time_data_string[x]}" for x in range(len(time_data_string)))
    full_string = f"{task_name.upper()}\n\n{times}\n{SEPARATOR}{plans_string}"
    return full_string


def save_to_file(full_string, task_name):
    directory = pathlib.Path('saved_plans')
    directory.mkdir(parents=True, exist_ok=True)
    file_path = directory / f"{task_name}.txt"
    with file_path.open("a+", encoding="utf-8") as file:
        file.write(full_string)


def get_time_statistics(times, task_name): #times array of array
    statistic_sum_up = f"{task_name}: \n"

    for index in range(len(times)):
        statistic_sum_up += f"Query {index +1} times [s]: "
        statistic_sum_up += ' '.join([str(t) for t in times[index]])
        statistic_sum_up += '\n'

    avg_values = [sum(single_times)/len(single_times) for single_times in times]
    min_values = [min(single_times) for single_times in times]
    max_values = [max(single_times) for single_times in times]

    statistic_sum_up += "\nWARTOŚCI STATYSTYCZNE\n"
    for index in range(len(avg_values)):
        statistic_sum_up += f"Query {index +1}: \n"
        statistic_sum_up += f"\tŚredni czas [s]: {avg_values[index]}\n"
        statistic_sum_up += f"\tMax czas [s]: {max_values[index]}\n"
        statistic_sum_up += f"\tMin czas [s]: {min_values[index]}\n"

    if len(times) > 1:
        all_sum_times = [x + y for x, y in zip(times[0], times[1])]
        finished_avg = sum(all_sum_times) / len(all_sum_times)
        finished_min = min(all_sum_times)
        finished_max = max(all_sum_times)

        statistic_sum_up += '\n'
        statistic_sum_up += "Połączone czasy: \n"
        statistic_sum_up += f"\tŚredni czas [s]: {finished_avg}\n"
        statistic_sum_up += f"\tMax czas [s]: {finished_max}\n"
        statistic_sum_up += f"\tMin czas [s]: {finished_min}\n"

    statistic_sum_up += '\n'
    return statistic_sum_up


def execute(task_queries, task_name):
    executed_plans = []
    times = []
    single_times = []
    db_state_before = get_information_about_db()
    for query in task_queries:
        single_times.append(measure_query_time(query))
        plan = run_plans(query)
        executed_plans.extend(plan)
        times.append(work_time_data(plan))
    full_string = create_full_string(executed_plans, times, task_name, len(task_queries))
    save_to_file(full_string, task_name)
    times_string = get_time_statistics(single_times, task_name)
    save_to_file(times_string, FILE_NAME)
    # db_state_after = get_information_about_db()
    # db_info = create_full_db_information_string(db_state_before, db_state_after)
    # save_to_file(db_info, FILE_NAME)


if __name__ == '__main__':
    execution_block = []
    for index in range(len(QUERIES)):
        execute(QUERIES[index], f"plan_{index + 1}")
