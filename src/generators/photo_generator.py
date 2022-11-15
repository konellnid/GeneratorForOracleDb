class PhotoGenerator:
    def __init__(self):
        self.fake = Faker(locale='en_US')
        self.fake.add_provider(date_time)
        self.fake.add_provider(lorem)

    def generate_photo(self, number_of_category: int, photo_id: int):
        offers = []
        extensions = ["jpeg", "png", "jpg"]

        for category_id in range(number_of_category):
            if category_id % 10000 == 0:
                print(f'Creating offer {category_id}...')
                photo_name = "photo_" + self.fake.word().replace("'", " ") # fake.url()
                file_name = self.fake.text(200).replace("'", "").replace("'", " ")
                upload_date = date.today() - timedelta(days=random.randrange(2, 6000)) #do poprawy xd
                file_extension = self.fake._select_factory_choice(extensions)

            offer = f"({photo_id}, '{photo_name}', '{file_name}', '{upload_date}', '{file_extension}')"
            offers.append(offer)
            photo_id += 1
        return offers
