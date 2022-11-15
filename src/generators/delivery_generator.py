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

    def generate_deliveries(self, number_of_category: int, delivery_id: int):
        offers = []

        for category_id in range(number_of_category):
            if category_id % 10000 == 0:
                print(f'Creating offer {category_id}...')
                EndDate = date.today() + timedelta(days=random.randrange(2, 60))
                expected_arrival = self.fake.date_between_dates(date_start=today(), date_end=EndDate)
                status = delivery_status(random.randrange(1, 7))
                delivery_type = DeliveryType(random.randrange(1, 6))

                if int(delivery_status.DISPATCHED) < int(status) < int(delivery_status.REJECTED):
                    send_date = date.today() + timedelta(days=random.randrange(2, 10))
                else:
                    send_date = date.today() - timedelta(days=random.randrange(2, 6000))

            offer = f"({delivery_id}, '{expected_arrival}', '{delivery_type}', '{status}', '{send_date}')"
            offers.append(offer)
            delivery_id += 1
        return offers

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
