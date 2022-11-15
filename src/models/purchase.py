from generators import utils


class Purchase:
    def __int__(self, purchase_id, quantity, additional_info, rating, purchase_date, fk_offer, fk_customer):
        self.purchase_id = purchase_id
        self.quantity = quantity
        self.additional_info = additional_info
        self.rating = rating
        self.purchase_date = purchase_date
        self.fk_offer = fk_offer
        self.fk_customer = fk_customer

    def insert_query(self):
        formatted_date = utils.format_date_for_oracle(self.purchase_date)
        return f"({self.purchase_id}, {self.quantity}, '{self.additional_info}', {self.rating}, '{formatted_date}', " \
               f"{self.fk_offer}, {self.fk_customer})"
