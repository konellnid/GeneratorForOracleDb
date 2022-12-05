import pathlib

import oracledb
import queries
import re
from statistics import mean
import pathlib

un = 'user123'  # os.environ.get('PYTHON_USERNAME')
pw = 'password'  # os.environ.get('PYTHON_PASSWORD')
cs = 'localhost/xepdb1 '  # os.environ.get('PYTHON_CONNECTSTRING')

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


def run_plans(task_query):
    executed_plans = []
    for i in range(NUMBER_OF_TRIES):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                cursor.execute(queries.FLUSH_BUFFER)
                cursor.execute(task_query)
                r = cursor.execute(queries.SELECT_XPLAN).fetchall()
                r_string = '\n'.join(str(element[0]) for element in r)
                # print(r_string)
                executed_plans.append(r_string)
            connection.rollback()
    return executed_plans


def work_time_data(executed_plans):
    execution_times = []
    for plan in executed_plans:
        time = re.search('\\d\\d:\\d\\d:\\d\\d', plan).group()
        # print(time)
        h, m, s = time.split(':')
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
    with file_path.open("x", encoding="utf-8") as file:
        file.write(full_string)


def execute(task_queries, task_name):
    executed_plans = []
    times = []
    for query in task_queries:
        plan = run_plans(query)
        executed_plans.extend(plan)
        times.append(work_time_data(plan))
    full_string = create_full_string(executed_plans, times, task_name, len(task_queries))
    save_to_file(full_string, task_name)


if __name__ == '__main__':
    execution_block = []
    for index in range(len(QUERIES)):
        execute(QUERIES[index], f"plan_{index + 1}")
