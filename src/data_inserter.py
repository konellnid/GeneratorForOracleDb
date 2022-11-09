import oracledb
import sql_info

un = 'user123'  # os.environ.get('PYTHON_USERNAME')
pw = 'password'  # os.environ.get('PYTHON_PASSWORD')
cs = 'localhost/xepdb1 '  # os.environ.get('PYTHON_CONNECTSTRING')


def build_insert_all(values_list: list, table_name: str, table_fields):
    connected_lines = '\n'.join([f'INTO {table_name} ({table_fields}) VALUES {value}' for value in values_list])
    return f'INSERT ALL\n {connected_lines}\n SELECT * FROM dual'


class DataInserter:
    def __init__(self, customer_values):
        self.customer_values = customer_values

    def insert_all(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                self._insert_customers(cursor)
            connection.commit()

    def _insert_customers(self, cursor):
        insert_all_statement = build_insert_all(self.customer_values, sql_info.TABLE_NAME_CUSTOMER,
                                                sql_info.CUSTOMER_FIELDS)
        cursor.execute(insert_all_statement)
        print('CUSTOMERS INSERTED (hopefully)')
