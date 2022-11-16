from datetime import timedelta, date

from faker import Faker
from faker.generator import random
from faker.providers import date_time, lorem

from models.photo import Photo


class PhotoGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(date_time)
        self.fake.add_provider(lorem)

    def generate_photo(self, photo_id: int, upload_date: date, offer_id: int):
        extensions = ["jpeg", "png", "jpg"]

        return Photo(
            photo_id,
            "photo_" + self.fake.word().replace("'", " "),
            self.fake.text(200).replace("'", "").replace("'", " "),
            upload_date,
            self.fake._select_factory_choice(extensions),
            offer_id
        )
