from datetime import timedelta, date
from generators import utils

from faker import Faker
from faker.generator import random
from faker.providers import date_time, lorem

from generators import utils
from models.purchase import Purchase


class PurchaseGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(date_time)
        self.fake.add_provider(lorem)

    def generate_purchase(self, purchase_id: int, offer_date: date, fk_offer: int, fk_customer: int):
        return Purchase(
            purchase_id=purchase_id,
            quantity=random.randrange(1, 10),
            additional_info=self.fake.text(1000).replace("'", " "),
            rating=random.randrange(1, 6),
            purchase_date=self.get_random_purchase_date(offer_date),
            fk_offer=fk_offer,
            fk_customer=fk_customer
        )

    def get_random_purchase_date(self, offer_date: date):
        days_between = (date.today() - offer_date).days - 1
        return offer_date + timedelta(days=random.randrange(days_between))

