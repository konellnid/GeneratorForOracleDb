/* For reference */
CREATE TABLE Customer (
  customer_id NUMBER,
  mail CHAR(40)
    CONSTRAINT customer_mail_not_null NOT NULL,
  name CHAR(30)
    CONSTRAINT customer_name_not_null NOT NULL,
  surname CHAR(30)
    CONSTRAINT customer_surname_not_null NOT NULL,
  date_of_birth DATE
    CONSTRAINT customer_date_of_birth_not_null NOT NULL,
  description VARCHAR(2000),
  CONSTRAINT customer_pk PRIMARY KEY (customer_id)
);

CREATE TABLE Address (
  address_id NUMBER,
  country CHAR(60)
    CONSTRAINT address_country_not_null NOT NULL,
  city CHAR(100)
    CONSTRAINT address_city_not_null NOT NULL,
  state CHAR(300)
    CONSTRAINT address_state_not_null NOT NULL,
  street CHAR(300)
    CONSTRAINT address_street_not_null NOT NULL,
  street_number NUMBER
    CONSTRAINT address_street_number_not_null NOT NULL,
  apartment_number NUMBER,
  postal_code CHAR(20)
    CONSTRAINT address_postal_code_not_null NOT NULL,
  fk_customer NUMBER
    CONSTRAINT address_fk_customer_not_null NOT NULL,
  CONSTRAINT address_pk PRIMARY KEY (address_id)
);

CREATE TABLE Photo (
  photo_id NUMBER,
  name CHAR(100)
    CONSTRAINT photo_name_not_null NOT NULL,
  file_name CHAR(200)
    CONSTRAINT photo_file_name_not_null NOT NULL,
  upload_date DATE
    CONSTRAINT photo_upload_date_not_null NOT NULL,
  file_extension CHAR(10)
    CONSTRAINT photo_file_extension_not_null NOT NULL,
  fk_offer NUMBER
    CONSTRAINT photo_fk_offer_not_null NOT NULL,
  CONSTRAINT photo_pk PRIMARY KEY (photo_id)
);

CREATE TABLE Category (
  category_id NUMBER,
  name CHAR(200)
    CONSTRAINT category_name_not_null NOT NULL,
  description VARCHAR(1000)
    CONSTRAINT category_description_not_null NOT NULL,
  fk_category NUMBER,
  CONSTRAINT category_pk PRIMARY KEY (category_id)
);

CREATE TABLE Offer (
  offer_id NUMBER,
  name CHAR(300)
    CONSTRAINT offer_name_not_null NOT NULL,
  description VARCHAR(2000)
    CONSTRAINT offer_description_not_null NOT NULL,
  price NUMBER
    CONSTRAINT offer_price_not_null NOT NULL,
  offer_date DATE
    CONSTRAINT offer_offer_date_not_null NOT NULL,
  quantity NUMBER
    CONSTRAINT offer_quantity_not_null NOT NULL,
  fk_customer NUMBER
    CONSTRAINT offer_fk_customer_not_null NOT NULL,
  CONSTRAINT offer_pk PRIMARY KEY (offer_id)
);

CREATE TABLE Purchase (
  purchase_id NUMBER,
  quantity NUMBER
    CONSTRAINT purchase_quantity_not_null NOT NULL,
  additional_info VARCHAR(1000),
  rating NUMBER,
  purchase_date DATE
    CONSTRAINT purchase_purchase_date_not_null NOT NULL,
  fk_offer NUMBER
    CONSTRAINT purchase_fk_offer_not_null NOT NULL,
  fk_customer NUMBER
    CONSTRAINT purchase_fk_customer_not_null NOT NULL,
  CONSTRAINT purchase_pk PRIMARY KEY (purchase_id)
);

CREATE TABLE Delivery (
  delivery_id NUMBER,
  expected_arrival DATE,
  delivery_type CHAR(100)
    CONSTRAINT delivery_delivery_type_not_null NOT NULL,
  status CHAR(100)
    CONSTRAINT delivery_status_not_null NOT NULL,
  sent_date DATE,
  fk_address NUMBER
    CONSTRAINT delivery_fk_address_not_null NOT NULL,
  fk_purchase NUMBER
    CONSTRAINT delivery_fk_purchase_not_null NOT NULL,
  CONSTRAINT delivery_pk PRIMARY KEY (delivery_id)
);