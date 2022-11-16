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

    def generate_offer(self, offer_id: int, customer_id: int, category_id):
        return Offer(
            offer_id,
            self.fake.ecommerce_name(),
            self.fake.text(2000),
            self.fake.ecommerce_price(),
            date.today() - timedelta(days=random.randrange(2, 6000)),
            random.randrange(1, 100),
            customer_id,
            category_id
        )

