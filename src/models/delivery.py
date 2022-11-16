from generators import utils


class Delivery:
    expected_arrival = ''
    sent_date = ''
    fk_address = ''
    fk_purchase = ''

    def __init__(self, delivery_id, expected_arrival, delivery_type, status, sent_date, fk_address, fk_purchase):
        self.delivery_id = delivery_id
        self.expected_arrival = expected_arrival
        self.delivery_type = delivery_type
        self.status = status
        self.sent_date = sent_date
        self.fk_address = fk_address
        self.fk_purchase = fk_purchase

    def insert_query(self):
        formatted_expected_arrival_date = utils.format_date_for_oracle(self.expected_arrival)
        formatted_sent_date = utils.format_date_for_oracle(self.sent_date)

        return f"({self.delivery_id}, {formatted_expected_arrival_date}, '{self.delivery_type}', '{self.status}', " \
               f"{formatted_sent_date}, {self.fk_address}, {self.fk_purchase})"
