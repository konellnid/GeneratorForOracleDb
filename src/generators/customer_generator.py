import utils

from faker import Faker
from faker.providers import date_time, lorem


# CREATE TABLE Customer (
#   customer_id NUMBER,
#   mail CHAR(40)
#     CONSTRAINT customer_mail_not_null NOT NULL,
#   name CHAR(30)
#     CONSTRAINT customer_name_not_null NOT NULL,
#   surname CHAR(30)
#     CONSTRAINT customer_surname_not_null NOT NULL,
#   date_of_birth DATE
#     CONSTRAINT customer_date_of_birth_not_null NOT NULL,
#   description VARCHAR(2000),
#   CONSTRAINT customer_pk PRIMARY KEY (customer_id)
# );


class CustomerGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(date_time)
        self.fake.add_provider(lorem)

    def generate_customers(self, number_of_customers: int):
        customers = []

        for customer_id in range(number_of_customers):
            if customer_id % 10000 == 0:
                print(f'Creating customer {customer_id}...')
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            domain_name = self.fake.domain_name()
            mail = f'{first_name}.{last_name}@{domain_name}'
            date_of_birth = self.fake.date_of_birth(minimum_age=18)
            formatted_date = utils.format_date_for_oracle(date_of_birth)
            description = self.fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
            customer = f"({customer_id}, '{mail}', '{first_name}', '{last_name}', {formatted_date}, '{description}')"
            customers.append(customer)

        return customers
