from datetime import timedelta, date

from faker import Faker
from faker.generator import random
from faker.providers import date_time, lorem

from generators import utils


class PurchaseGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(date_time)
        self.fake.add_provider(lorem)

    def generate_purchase(self, number_of_category: int, purchase_id: int):
        offers = []

        for category_id in range(number_of_category):
            if category_id % 10000 == 0:
                print(f'Creating offer {category_id}...')
                purchase_quantity = random.randrange(1, 10)
                additional_info = self.fake.text(1000).replace("'", " ")
                rating = random.randrange(0, 6)
                purchase_date = date.today() - timedelta(days=random.randrange(2, 60))
                formatted_date = utils.format_date_for_oracle(purchase_date)

            offer = f"({purchase_id}, {purchase_quantity}, '{additional_info}', {rating}, {formatted_date})"
            offers.append(offer)
            purchase_id += 1
        return offers


