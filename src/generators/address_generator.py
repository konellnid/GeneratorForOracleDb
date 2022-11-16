import random

import faker_commerce
from faker import Faker
from faker.providers import lorem
from models.address import Address


class AddressGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(faker_commerce.Provider)
        self.fake.add_provider(lorem)

    def generate_address(self, adr_id: int, customer_id: int):
        return Address(
            adr_id,
            self.fake.country().replace("'", " "),
            self.fake.city().replace("'", " "),
            self.fake.state().replace("'", " "),
            self.fake.street_name().replace("'", " "),
            self.fake.building_number(),
            random.randrange(1, 20),
            self.fake.postcode(),
            customer_id
        )
