TASK_1 = """UPDATE Offer Set offer.price = offer.price*(1-{Z}/100)
Where fk_category in (
Select cat1.category_id id from category cat1 left join category cat2
on cat1.fk_category = cat2.category_id
where '{X}' in (cat1.name, cat2.name)
) and TO_CHAR(offer_date, 'YYYY') = '{Y}'
"""

TASK_2_1 = """DELETE FROM Photo ph
WHERE ph.fk_offer IN (
SELECT o.offer_id
FROM Offer o
LEFT JOIN Purchase pu ON o.offer_id = pu.fk_offer
WHERE pu.purchase_id IS NULL AND o.offer_date < (SELECT SYSDATE - NUMTOYMINTERVAL(3, 'year') FROM dual)
)"""

TASK_2_2 = """DELETE FROM Offer
WHERE offer_id IN (
SELECT o.offer_id
FROM Offer o
LEFT JOIN Purchase pu ON o.offer_id = pu.fk_offer
WHERE pu.purchase_id IS NULL AND o.offer_date < (SELECT SYSDATE - NUMTOYMINTERVAL(3, 'year') FROM dual)
)"""

TASK_3_1 = """Insert INTO Category (category_id, name, description, fk_category)
Select 1 + (Select count(*) from category),
'{B}', 'subcategory', (Select category_id from category where category.name='{A}')
From category where '{C}' < (Select count(*) from category
right join offer on offer.fk_category = category.category_id
where category.name = '{A}' and offer.name LIKE '%{B}%') Group by 1"""

TASK_3_2 = """Update offer Set offer.fk_category = (Select count(*) from category)
Where '{C}' < (
Select count(*) from category
right join offer on offer.fk_category = category.category_id
where category.name = '&A' and offer.name LIKE '%{B}%'
)
and offer_id in (
Select offer_id from category
right join offer on offer.fk_category = category.category_id
where category.name = '{A}' and offer.name LIKE '%{B}%')
"""

TASK_4 = """Select mail, sum(purchase_price) "wydana_kwota"
from (
Select offer_id, offer.price * sum(purchase.quantity) as purchase_price, purchase.fk_customer as purchase_customer_id
from offer right join purchase on fk_offer = offer_id
Where TO_CHAR(purchase_date, 'mm') = TO_CHAR(current_date, 'mm') and
TO_CHAR(purchase_date, 'yyyy') = TO_CHAR(current_date, 'yyyy')
Group by offer_id, offer.price, purchase.fk_customer)
join customer on customer_id = purchase_customer_id
group by purchase_customer_id, mail
having sum(purchase_price) > (
select avg(purchase_price_sum)
from (
Select sum(purchase_price) as purchase_price_sum
from (
Select offer_id, offer.price * sum(purchase.quantity) as purchase_price, purchase.fk_customer as purchase_customer_id
from offer right join purchase on fk_offer = offer_id
Where TO_CHAR(purchase_date, 'mm') = TO_CHAR(current_date, 'mm') and
TO_CHAR(purchase_date, 'yyyy') = TO_CHAR(current_date, 'yyyy')
Group by offer_id, offer.price, purchase.fk_customer)
group by purchase_customer_id
)
)
"""

TASK_5 = """select offer_id, offer.name "name", price, avg(rating) "avg_rating", sum(purchase.quantity) "count_purchase", customer.name "user_name"
from offer
left join customer on customer_id = fk_customer
right join purchase on fk_offer = offer_id
Where TO_CHAR(offer_date, 'mm') = '{A1}' and
TO_CHAR(offer_date, 'yyyy') = '{A2}'
group by offer_id, offer.name, price, customer.name
Having sum(purchase.quantity) > '{B}' and avg(rating) > '{D}'
"""

TASK_6 = """Select country, postal_code, city, street, street_number, apartment_number, offer.name "offer_name", purchase.quantity
from delivery
left join address on delivery.fk_address = address_id
left join purchase on delivery.fk_purchase = purchase.purchase_id
left join offer on purchase.fk_offer = offer.offer_id
where delivery.expected_arrival = trunc(sysdate)
and address.country = '{country}'
and address.postal_code = '{postal_code}'
"""

EXPLAIN_PLAN = """
EXPLAIN PLAN FOR {query}
"""

QUERY_1 = [TASK_1.format(X="Shoes", Y="2012", Z=10)]
QUERY_2 = [TASK_2_1, TASK_2_2]
QUERY_3 = [TASK_3_1.format(A="Kids", B="Toys", C=1), TASK_3_2.format(A="Kids", B="Toys", C=1)]
QUERY_4 = [TASK_4]
QUERY_5 = [TASK_5.format(A1="02", A2="2012", B=100, D=1)]
QUERY_6 = [TASK_6.format(country="Barbados", postal_code="28499")]

SELECT_XPLAN = "SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY)"

FLUSH_BUFFER = "ALTER SYSTEM FLUSH BUFFER_CACHE"


