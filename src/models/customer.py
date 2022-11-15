from generators import utils


class Customer:
    def __init__(self, customer_id, mail, name, surname, date_of_birth, description):
        self.customer_id = customer_id
        self.mail = mail
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.description = description

    def insert_query(self):
        formatted_date = utils.format_date_for_oracle(self.date_of_birth)
        return f"({self.customer_id}, '{self.mail}', '{self.name}', '{self.surname}', '{formatted_date}', '{self.description}')"
