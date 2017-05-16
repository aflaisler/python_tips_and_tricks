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
