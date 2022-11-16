from faker import Faker
from faker.providers import date_time, lorem
from models.customer import Customer


class CustomerGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(date_time)
        self.fake.add_provider(lorem)

    def generate_customer(self, customer_id: int):
        return Customer(
            customer_id,
            f'{self.fake.last_name()}@{self.fake.domain_name()}',
            self.fake.first_name(),
            self.fake.last_name(),
            self.fake.date_of_birth(minimum_age=18),
            self.fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
        )

