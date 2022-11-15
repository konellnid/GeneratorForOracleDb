class Photo:
    def __init__(self, photo_id, name, file_name, upload_date, file_extension, fk_offer):
        self.photo_id = photo_id
        self.name = name
        self.file_name = file_name
        self.upload_date = upload_date
        self.file_extension = file_extension
        self.fk_offer = fk_offer

    def insert_query(self):
        return f"({self.photo_id}, '{self.name}', '{self.file_name}', '{self.upload_date}', '{self.file_extension}', {self.fk_offer})"
