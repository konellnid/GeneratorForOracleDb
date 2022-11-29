TASK_1 = """EXPLAIN PLAN FOR 
UPDATE Offer Set offer.price = offer.price*(1-{Z}/100)
Where fk_category in (
Select cat1.category_id id from category cat1 left join category cat2
on cat1.fk_category = cat2.category_id
where '{X}' in (cat1.name, cat2.name)
) and TO_CHAR(offer_date, 'YYYY') = '{Y}'
"""

TASK_2 = """EXPLAIN PLAN FOR <query>
"""

TASK_3 = """EXPLAIN PLAN FOR <query>
"""

TASK_4 = """EXPLAIN PLAN FOR <query>
"""

TASK_5 = """EXPLAIN PLAN FOR <query>
"""

TASK_6 = """EXPLAIN PLAN FOR <query>
"""

SELECT_XPLAN = "SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY)"

FLUSH_BUFFER = "ALTER SYSTEM FLUSH BUFFER_CACHE"
