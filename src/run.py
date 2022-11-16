import random
from datetime import date, timedelta

from data_inserter import DataInserter
from generators.address_generator import AddressGenerator
from generators.category_generator import CategoryGenerator
from generators.customer_generator import CustomerGenerator
from generators.delivery_generator import DeliveryGenerator
from generators.offer_generator import OfferGenerator
from generators.photo_generator import PhotoGenerator
from generators.purchase_generator import PurchaseGenerator

NUMBER_OF_CUSTOMERS = 100
NUMBER_OF_ADDRESSES = 100
NUMBER_OF_PHOTOS = 100
NUMBER_OF_CATEGORIES = 100
NUMBER_OF_OFFERS = 100
NUMBER_OF_PURCHASES = 100
NUMBER_OF_DELIVERIES = 100


def run():
    i = 0
    addresses_insert_queries = []
    customers_insert_queries = []
    categories = []
    offer_insert_queries = []
    photos = []
    purchases = []
    deliveries = []

    offers = []
    customers = []
    addresses = []

    customer_id = 0
    address_id = 0
    offer_id = 0
    category_id = 0
    photo_id = 0
    purchase_id = 0
    delivery_id = 0

    data_inserter = DataInserter([])

    category_generator = CategoryGenerator()
    customer_generator = CustomerGenerator()
    address_generator = AddressGenerator()
    offer_generator = OfferGenerator()
    photo_generator = PhotoGenerator()
    purchase_generator = PurchaseGenerator()
    delivery_generator = DeliveryGenerator()

    while i < 2:
        for _ in range(NUMBER_OF_CATEGORIES):
            category = category_generator.generate_category(category_id, -1)
            categories.append(category.insert_query())
            category_id += 1
            parent_cat_id = category_id

            number_of_subcategory = random.randrange(0, 4)
            for _ in range(number_of_subcategory):
                category = category_generator.generate_category(category_id, parent_cat_id)
                categories.append(category.insert_query())
                category_id += 1

        data_inserter.values = categories
        data_inserter.insert_category()

        for _ in range(NUMBER_OF_CUSTOMERS):
            customer = customer_generator.generate_customer(customer_id)
            customers_insert_queries.append(customer.insert_query())
            customers.append(customer)

            number_of_addresses = random.randrange(1, 4)
            for _ in range(number_of_addresses):
                address = address_generator.generate_address(address_id, customer_id)
                addresses_insert_queries.append(address.address_query())
                addresses.append(address)
                address_id += 1

            number_of_offers = random.randrange(0, 30)
            for _ in range(number_of_offers):
                offer = offer_generator.generate_offer(offer_id, customer_id, random.randrange(NUMBER_OF_CATEGORIES))
                offer_insert_queries.append(offer.insert_query())
                offers.append(offer)
                offer_id += 1

                number_of_photos = random.randrange(1, 4)
                for _ in range(number_of_photos):
                    days_between = (date.today() - offer.offer_date).days
                    upload_date = offer.offer_date + timedelta(days=random.randrange(days_between))
                    photo = photo_generator.generate_photo(photo_id, upload_date, offer.offer_id)
                    photos.append(photo.insert_query())
                    photo_id += 1
            customer_id += 1

        data_inserter.values = addresses_insert_queries
        data_inserter.insert_address()

        data_inserter.values = photos
        data_inserter.insert_photo()

        data_inserter.values = customers_insert_queries
        data_inserter.insert_customers()

        data_inserter.values = offer_insert_queries
        data_inserter.insert_offers()

        for _ in range(NUMBER_OF_PURCHASES):
            offer = offers[random.randrange(len(offers) - 1)]
            customer = customers[len(customers) - 1]
            purchase = purchase_generator.generate_purchase(purchase_id, offer.offer_date, offer.offer_id,
                                                            customer.customer_id)
            purchases.append(purchase.insert_query())
            purchase_id += 1

            number_of_delivery = random.randrange(1, 3)
            for _ in range(number_of_delivery):
                address = addresses[len(addresses) -1]
                delivery = delivery_generator.generate_delivery(delivery_id, offer.offer_date, address.address_id,
                                                                purchase.purchase_id)
                deliveries.append(delivery.insert_query())
                delivery_id += 1

        data_inserter.values = purchases
        data_inserter.insert_purchase()

        data_inserter.values = deliveries
        data_inserter.insert_delivery()

        addresses_insert_queries = []
        customers_insert_queries = []
        categories = []
        offer_insert_queries = []
        photos = []
        deliveries = []
        offers = []
        customers = []
        addresses = []



if __name__ == '__main__':
    run()
