from datetime import timedelta, date

from dateutil.utils import today
from faker import Faker
from faker.generator import random
from faker.providers import date_time, lorem

from delivery import DeliveryType
from delivery_status import delivery_status
from models.delivery import Delivery


class DeliveryGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(date_time)
        self.fake.add_provider(lorem)

    def generate_delivery(self, delivery_id: int, offer_date: date, address: int, purchase: int):
        status = delivery_status(random.randrange(1, 7))
        expected_date = self._get_expected_date(status, offer_date)
        sent_date = self._get_expected_date(status, offer_date)

        return Delivery(
            delivery_id,
            expected_date,
            DeliveryType(random.randrange(1, 6)),
            status,
            sent_date,
            address,
            purchase
        )

    def _get_expected_date(self, status, offer_date: date):
        days_between = (date.today() - offer_date).days - 1

        if int(status) > delivery_status.PAID:
            return offer_date + timedelta(days=random.randrange(days_between))
        else:
            return date.today() + timedelta(days=random.randrange(10))

    def _get_send_date(self, expected_date: date):
        return expected_date + timedelta(days=random.randrange(-3, 10))
