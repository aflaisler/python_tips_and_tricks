/* https://www.postgresql.org/docs/current/static/functions-math.html */

/*CASE*/

SELECT e.meal_id,
    e.event,
    SUM(CASE e.event
            WHEN 'bought' THEN 1
            WHEN 'like' THEN 1
            WHEN 'share' THEN 1
        END)
FROM events e
GROUP BY e.event,
      e.meal_id;


/*intervals*/
/*date*/
date('now') + interval '1 year' AS today_in_one_year,
/*timestamp*/
date '2003-12-13' + interval '1 year' AS my_next_birthday ;
-- Difference between Oct 02, 2011 and Jan 01, 2012 in years
SELECT DATE_PART('year', '2012-01-01'::date) - DATE_PART('year', '2011-10-02'::date);
SELECT DATE_PART('year', '2012-01-01'::timestamp) - DATE_PART('year', '2011-10-02'::timestamp);

/*with ...*/
WITH regional_sales AS (
        SELECT region, SUM(amount) AS total_sales
        FROM orders
        GROUP BY region
     ), top_regions AS (
        SELECT region
        FROM regional_sales
        WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
     )
SELECT region,
       product,
       SUM(quantity) AS product_units,
       SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region, product;

/*RECURSIVE Hierarchical query - 1 (easy) */

WITH RECURSIVE subordinates AS (
 SELECT
 employee_id,
 manager_id,
 full_name
 FROM
 employees
 WHERE
 employee_id = 2
 UNION
 SELECT
 e.employee_id,
 e.manager_id,
 e.full_name
 FROM
 employees e
 INNER JOIN subordinates s ON s.employee_id = e.manager_id
) SELECT
 *
FROM
 subordinates;

/*RECURSIVE Hierarchical query - 2 (medium)*/
WITH RECURSIVE employee_levels(id, first_name, last_name, manager_id, LEVEL) AS
  ( SELECT e.*,
           1
   FROM employees e
   WHERE e.manager_id IS NULL
     UNION ALL
     SELECT e.*,
            el.level + 1
     FROM employees e,
          employee_levels el WHERE e.manager_id = el.id )
SELECT *
FROM employee_levels el
ORDER BY el.level

/*Conditional Count*/

SELECT EXTRACT(MONTH
               FROM payment_date) AS MONTH,
       COUNT(*) AS total_count,
       SUM(amount) AS total_amount,
       COUNT(*) FILTER (
                        WHERE staff_id = 1) AS mike_count,
       SUM(amount) FILTER (
                           WHERE staff_id = 1) AS mike_amount,
       COUNT(*) FILTER (
                        WHERE staff_id = 2) AS jon_count,
       SUM(amount) FILTER (
                           WHERE staff_id = 2) AS jon_amount
FROM payment
GROUP BY MONTH
ORDER BY MONTH;

/*SQL Basics: Simple VIEW*/
CREATE VIEW members_approved_for_voucher AS
SELECT m.id, m.name, m.email, SUM(p.price) AS total_spending
FROM members m
INNER JOIN sales s ON s.member_id = m.id
INNER JOIN products p ON p.id = s.product_id
WHERE s.department_id IN (
  SELECT s2.department_id
  FROM sales s2
  INNER JOIN products p2 ON p2.id = s2.product_id
  GROUP BY s2.department_id
  HAVING SUM(p2.price) > 10000
)
GROUP BY m.id, m.name, m.email
HAVING SUM(p.price) > 1000
ORDER BY m.id;

SELECT * FROM members_approved_for_voucher;

/*quick random row selection in Postgres*/
SELECT orderid FROM orders OFFSET floor(random()*(select count(*) from orders)) LIMIT 1;
