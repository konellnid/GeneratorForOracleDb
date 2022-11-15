from faker import Faker
from faker.providers import date_time, lorem

from generators import utils
from models.customer import Customer


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

    def generate_customers(self, number_of_customers: int, id: int):
        customers = []

        for customer_id in range(number_of_customers):
            if customer_id % 10000 == 0:
                print(f'Creating customer {customer_id}...')
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            domain_name = self.fake.domain_name()
            mail = f'{last_name}@{domain_name}'
            date_of_birth = self.fake.date_of_birth(minimum_age=18)
            formatted_date = utils.format_date_for_oracle(date_of_birth)
            description = self.fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
            customer = f"({id}, '{mail}', '{first_name}', '{last_name}', {formatted_date}, '{description}')"
            customers.append(customer)
            id = id+1

        return customers

    def generate_customer(self, customer_id: int):
        date_of_birth = self.fake.date_of_birth(minimum_age=18),
        formatted_date = utils.format_date_for_oracle(date_of_birth)

        return Customer(
            customer_id,
            f'{self.fake.last_name()}@{self.fake.domain_name()}',
            self.fake.first_name(),
            self.fake.last_name(),
            formatted_date,
            self.fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
        )

