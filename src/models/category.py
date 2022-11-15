class Category:
    def __init__(self, category_id, name, description, fk_category):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.fk_category = fk_category

    def insert_query(self):
        return f"({self.category_id}, '{self.name}', '{self.description}', {self.fk_category})"
