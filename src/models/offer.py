from generators import utils


class Offer:
    def __init__(self, offer_id, name, description, price, offer_date, quantity, fk_customer, fk_category):
        self.offer_id = offer_id
        self.name = name
        self.description = description
        self.price = price
        self.offer_date = offer_date
        self.quantity = quantity
        self.fk_customer = fk_customer
        self.fk_category = fk_category

    def insert_query(self):
        formatted_date = utils.format_date_for_oracle(self.offer_date)
        return f"({self.offer_id}, '{self.name}', '{self.description}', '{self.price}', '{formatted_date}'," \
               f"{self.quantity}, {self.fk_customer}, {self.fk_category})"
