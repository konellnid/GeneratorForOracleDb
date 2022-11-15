import oracledb
import sql_info

un = 'user123'  # os.environ.get('PYTHON_USERNAME')
pw = 'password'  # os.environ.get('PYTHON_PASSWORD')
cs = 'localhost/xepdb1 '  # os.environ.get('PYTHON_CONNECTSTRING')


def build_insert_all(values_list: list, table_name: str, table_fields):
    connected_lines = '\n'.join([f'INTO {table_name} ({table_fields}) VALUES {value}' for value in values_list])
    return f'INSERT ALL\n {connected_lines}\n SELECT * FROM dual'


class DataInserter:
    def __init__(self, values):
        self.values = values

    def insert_all(self, offers):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                # self._insert_customers(cursor)
                # self._insert_offers(cursor)
                # self._insert_address(cursor)
                # self._insert_category(cursor)
                self._insert_delivery(cursor)
                # self._insert_purchase(cursor)
            connection.commit()

    def _insert_customers(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                insert_all_statement = build_insert_all(self.customer_values, sql_info.TABLE_NAME_CUSTOMER,
                                                        sql_info.CUSTOMER_FIELDS)
                cursor.execute(insert_all_statement)
            connection.commit()

    def _insert_offers(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                insert_all_statement = build_insert_all(self.values, sql_info.TABLE_NAME_OFFER,
                                                        sql_info.OFFER_FIELDS)
                cursor.execute(insert_all_statement)
        connection.commit()

    def _insert_address(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                insert_all_statement = build_insert_all(self.values, sql_info.TABLE_NAME_ADDRESS,
                                                        sql_info.ADDRESS_FIELDS)
                cursor.execute(insert_all_statement)
            connection.commit()
        print('OFFERS INSERTED (hopefully)')

    def insert_category(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                insert_all_statement = build_insert_all(self.values, sql_info.TABLE_NAME_CATEGORY,
                                                        sql_info.CATEGORY_FIELDS)
                cursor.execute(insert_all_statement)
            connection.commit()

    def _insert_delivery(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                insert_all_statement = build_insert_all(self.values, sql_info.TABLE_NAME_DELIVERY,
                                                        sql_info.DELIVERY_FIELDS)
                cursor.execute(insert_all_statement)
            connection.commit()

    def _insert_photo(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                insert_all_statement = build_insert_all(self.values, sql_info.TABLE_NAME_PHOTO,
                                                        sql_info.PHOTO_FIELDS)
                cursor.execute(insert_all_statement)
            connection.commit();

    def _insert_purchase(self):
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                insert_all_statement = build_insert_all(self.values, sql_info.TABLE_NAME_PURCHASE,
                                                        sql_info.PURCHASE_FIELDS)
                cursor.execute(insert_all_statement)
            connection.commit()
