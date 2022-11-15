TABLE_NAME_CUSTOMER = 'Customer'
CUSTOMER_FIELDS = 'user_id, mail, name, surname, date_of_birth, description'


TABLE_NAME_OFFER = 'Offer'
OFFER_FIELDS = 'offer_id, name, description, price, offer_date, quantity, fk_customer, fk_category'

TABLE_NAME_ADDRESS = 'Address'
ADDRESS_FIELDS = 'address_id, country, city, state, street, street_number, apartment_number, postal_code, fk_customer'


TABLE_NAME_CATEGORY = 'Category'
CATEGORY_FIELDS = 'category_id, name, description, fk_category'

TABLE_NAME_DELIVERY = 'Delivery'
DELIVERY_FIELDS = 'delivery_id, expected_arrival, delivery_type, status, sent_date, fk_address, fk_purchase'

TABLE_NAME_PHOTO = 'Photo'
PHOTO_FIELDS = 'photo_id, name, file_name, upload_date, file_extension, fk_offer'

TABLE_NAME_PURCHASE = 'Purchase'
PURCHASE_FIELDS = 'purchase_id, quantity, additional_info, rating, purchase_date, fk_offer, fk_customer'

