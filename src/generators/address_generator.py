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

    def generate_addresses(self, number_of_address: int, adr_id: int):
        offers = []

        for address_id in range(number_of_address):
            if address_id % 10000 == 0:
                print(f'Creating offer {address_id}...')

            country = self.fake.country().replace("'"," ")
            city = self.fake.city().replace("'"," ")
            state = self.fake.state().replace("'"," ")
            street = self.fake.street_name().replace("'"," ")
            street_number = self.fake.building_number()
            apartment_number = random.randrange(0, 20)
            postal_code = self.fake.postcode()

            offer = f"({adr_id}, '{country}', '{city}', '{state}', '{street}', {street_number}, {apartment_number}, '{postal_code}')"
            offers.append(offer)
            adr_id += 1
        return offers

    def generate_address(self, adr_id: int, customer_id: int):
        return Address(
            adr_id,
            self.fake.country().replace("'", " "),
            self.fake.city().replace("'", " "),
            self.fake.state().replace("'", " "),
            self.fake.street_name().replace("'", " "),
            self.fake.building_number(),
            random.randrange(0, 20),
            self.fake.postcode(),
            customer_id
        )
