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
        return f"({self.delivery_id}, '{self.expected_arrival}', '{self.delivery_type}', '{self.status}', " \
               f"'{self.sent_date}', {self.fk_address}, {self.fk_purchase})"
