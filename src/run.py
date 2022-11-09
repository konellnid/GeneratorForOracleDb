from src.data_inserter import DataInserter
from src.generators.customer_generator import CustomerGenerator

NUMBER_OF_CUSTOMERS = 100
NUMBER_OF_ADDRESSES = 100
NUMBER_OF_PHOTOS = 100
NUMBER_OF_CATEGORIES = 100
NUMBER_OF_OFFERS = 100
NUMBER_OF_PURCHASES = 100
NUMBER_OF_DELIVERIES = 100


def run():
    customer_generator = CustomerGenerator()
    customers = customer_generator.generate_customers(NUMBER_OF_CUSTOMERS)

    print('INSERT TIME!')

    data_inserter = DataInserter(customers)
    data_inserter.insert_all()


if __name__ == '__main__':
    run()
