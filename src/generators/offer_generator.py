import random
from datetime import date, timedelta

import faker_commerce
from faker import Faker
from faker.providers import lorem

from generators import utils
from models.offer import Offer


class OfferGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(faker_commerce.Provider)
        self.fake.add_provider(lorem)

    def generate_offers(self, number_of_offers: int, id: int):
        offers = []

        for offer_id in range(number_of_offers):
            if offer_id % 10000 == 0:
                print(f'Creating offer {offer_id}...')
            name = self.fake.ecommerce_name()
            offer_description = self.fake.text(2000)
            price = self.fake.ecommerce_price()
            offer_date = date.today() - timedelta(days=random.randrange(2, 6000))
            quantity = random.randrange(1, 100)
            formatted_date = utils.format_date_for_oracle(offer_date)

            offer = f"({id}, '{name}', '{offer_description}', '{price}', {formatted_date}, '{quantity}')"
            offers.append(offer)
            id +=1
        return offers

    def generate_offer(self, offer_id: int, customer_id: int, category_id):
        formatted_date = utils.format_date_for_oracle(date.today() - timedelta(days=random.randrange(2, 6000)))
        return Offer(
            offer_id,
            self.fake.ecommerce_name(),
            self.fake.text(2000),
            self.fake.ecommerce_price(),
            formatted_date,
            random.randrange(1, 100),
            customer_id,
            category_id
        )

