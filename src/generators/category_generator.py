import faker_commerce
from faker import Faker
from faker.providers import lorem

from models.category import Category


class CategoryGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(faker_commerce.Provider)
        self.fake.add_provider(lorem)

    def generate_category(self, number_of_category: int, cat_id: int):
        offers = []

        for category_id in range(number_of_category):
            if category_id % 10000 == 0:
                print(f'Creating offer {category_id}...')

                category_name = self.fake.ecommerce_category().replace("'", " ")
                category_description = self.fake.text(1000).replace("'", " ")
            offer = f"({cat_id}, '{category_name}', '{category_description}')"
            offers.append(offer)
            cat_id += 1

        return offers

    def generate_category(self, cat_id: int, fk_cat_id: int):
        if fk_cat_id == -1:
            fk_cat_id = 'null'
        return Category(
            cat_id,
            self.fake.ecommerce_category().replace("'", " "),
            self.fake.text(1000).replace("'", " "),
            fk_cat_id
        )
