import oracledb
import queries

un = 'user123'  # os.environ.get('PYTHON_USERNAME')
pw = 'password'  # os.environ.get('PYTHON_PASSWORD')
cs = 'localhost/xepdb1 '  # os.environ.get('PYTHON_CONNECTSTRING')

QUERIES = [
    queries.TASK_1.format(X="Shoes", Y="2012", Z=10)
]


def execute(task_query):
    with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.FLUSH_BUFFER)
            cursor.execute(task_query)
            for r in cursor.execute(queries.SELECT_XPLAN):
                print(r)
        connection.rollback()


if __name__ == '__main__':
    for query in QUERIES:
        execute(query)
