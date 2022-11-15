import random
from datetime import date, timedelta

from data_inserter import DataInserter
from generators.address_generator import AddressGenerator
from generators.category_generator import CategoryGenerator
from generators.customer_generator import CustomerGenerator
from generators.offer_generator import OfferGenerator
from generators.photo_generator import PhotoGenerator

NUMBER_OF_CUSTOMERS = 100
NUMBER_OF_ADDRESSES = 100
NUMBER_OF_PHOTOS = 100
NUMBER_OF_CATEGORIES = 100
NUMBER_OF_OFFERS = 100
NUMBER_OF_PURCHASES = 100
NUMBER_OF_DELIVERIES = 100


def run():
    i = 0
    addresses = []
    customers = []
    categories = []
    offers = []
    photos = []

    address_id = 0
    offer_id = 0
    category_id = 0
    photo_id = 0

    category_data_inserter = DataInserter(categories)
    category_generator = CategoryGenerator()
    customer_generator = CustomerGenerator()
    address_generator = AddressGenerator()
    offer_generator = OfferGenerator()
    photo_generator = PhotoGenerator()

    while i < 2000:
        while category_id < NUMBER_OF_CATEGORIES:
            category = category_generator.generate_category(category_id, -1)
            categories.append(category.insert_query())
            category_id += 1
            parent_cat_id = category_id

            number_of_subcategory = random.randrange(0, 4)
            for cat_number in range(number_of_subcategory):
                category = category_generator.generate_category(category_id, parent_cat_id)
                categories.append(category.insert_query())
                category_id += 1
        category_data_inserter.values = categories
        category_data_inserter.insert_category()
        categories = []

        for customer_id in range(NUMBER_OF_CUSTOMERS):
            customer = customer_generator.generate_customer(customer_id)
            customers.append(customer.insert_query())

            number_of_addresses = random.randrange(1, 4)
            for address_number in range(number_of_addresses):
                address = address_generator.generate_address(address_id, customer_id)
                addresses.append(address.address_query())
                address_id += 1

            number_of_offers = random.randrange(0, 30)
            for offer_number in range(number_of_offers):
                offer = offer_generator.generate_offer(offer_id, customer_id, random.randrange(NUMBER_OF_CATEGORIES))
                offers.append(offer.insert_query())
                offer_id += 1

                number_of_photos = random.randrange(1, 4)
                for photo_number in range(number_of_photos):
                    days_between = (date.today() - offer.offer_date).days
                    upload_date = offer.offer_date + timedelta(days=random.randrange(days_between))
                    photo = photo_generator.generate_photo(photo_id, upload_date, offer.offer_id)
                    photos.append(photo.insert_query())
                    photo_id += 1

        # customer_generator = CustomerGenerator()
        # customers = customer_generator.generate_customers(NUMBER_OF_CUSTOMERS, id)

        # generator = OfferGenerator()
        # customers = generator.generate_offers(NUMBER_OF_OFFERS, id)
        # generator = AddressGenerator()
        # customers = generator.generate_address(NUMBER_OF_OFFERS, id)

        # generator = DeliveryGenerator()
        # customers = generator.generate_delivery(NUMBER_OF_OFFERS, id)

        # generator = CategoryGenerator()
        # customers = generator.generate_category(NUMBER_OF_OFFERS, id)

        # generator = PhotoGenerator()
        # customers = generator.generate_photo(NUMBER_OF_OFFERS, id)

        # generator = PurchaseGenerator()
        # customers = generator.generate_purchase(NUMBER_OF_OFFERS, id)
        # id += 1000
        # print('INSERT TIME!')
        #
        # data_inserter = DataInserter(customers)
        # data_inserter.insert_all(data_inserter)
        # i += 1


if __name__ == '__main__':
    run()
