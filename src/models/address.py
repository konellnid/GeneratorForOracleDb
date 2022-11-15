class Address:
    def __init__(self, address_id, country, city, state, street, street_number, apartment_number, postal_code, fk_customer):
        self.address_id = address_id
        self.country = country
        self.city = city
        self.state = state
        self.street = street
        self.street_number = street_number
        self.apartment_number = apartment_number
        self.postal_code = postal_code
        self.fk_customer = fk_customer

    def address_query(self):
        return f"({self.address_id}, '{self.country}', '{self.city}', '{self.state}', '{self.street}', " \
               f"{self.street_number}, {self.apartment_number}, '{self.postal_code}') "
