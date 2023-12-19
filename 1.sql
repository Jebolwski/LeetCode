--!https://leetcode.com/problems/combine-two-tables/
select firstName,lastName,city,state from Person left outer join address on person.personId=address.personId

--!https://leetcode.com/problems/employees-earning-more-than-their-managers/
SELECT name AS Employee
FROM Employee e
WHERE salary > (
    SELECT m.salary
    FROM Employee m
    WHERE m.id = e.managerId
);

--!https://leetcode.com/problems/duplicate-emails/
SELECT DISTINCT P1.Email FROM Person P1,Person P2 
WHERE P1.id <> P2.id AND P1.Email=P2.Email

--!https://leetcode.com/problems/delete-duplicate-emails/
delete p1 from person p1,person p2
where p1.email=p2.email and p1.id>p2.id

--!https://leetcode.com/problems/customers-who-never-order/
select name as Customers from Customers where id not in (select customerId from Orders)

--!https://leetcode.com/problems/rising-temperature/
select id from Weather w2 where temperature>(select temperature from Weather w1 where DATE_SUB(w2.recordDate, INTERVAL 1 DAY)=w1.recordDate)

--!https://leetcode.com/problems/employee-bonus/
SELECT E.name, B.bonus FROM Employee E LEFT OUTER JOIN Bonus B  ON 
E.empId = B.empId WHERE B.bonus < 1000 OR bonus IS NULL

--!https://leetcode.com/problems/find-customer-referee/
select name from Customer where referee_id<>2 or referee_id is null

--!https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
select customer_number from Orders group by customer_number order by COUNT(customer_number) desc limit 1;

--!https://leetcode.com/problems/big-countries/
select w1.name, w1.population, w1.area from World w1 where w1.area>=3000000 or w1.population>=25000000;

--!https://leetcode.com/problems/classes-more-than-5-students/
select class from Courses group by class having count(class)>4

--!https://leetcode.com/problems/sales-person/
select name from SalesPerson where sales_id 
not in (select sales_id from Orders where 
com_id=(select com_id from Company where name="RED" limit 1))

--!https://leetcode.com/problems/triangle-judgement/
select x, y, z, if(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle from Triangle

--!https://leetcode.com/problems/biggest-single-number/
SELECT MAX(num) AS num FROM (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1) new;


--!https://leetcode.com/problems/not-boring-movies/
select * from Cinema where id%2=1 and description<>"boring" order by rating desc

--!https://leetcode.com/problems/swap-salary/
UPDATE salary SET sex =
CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;

--!https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
select actor_id,director_id
from ActorDirector 
group by actor_id,director_id
having count(timestamp)>=3;

--!https://leetcode.com/problems/product-sales-analysis-i/
select product_name, year, price from Product p1, Sales s1 where s1.product_id=p1.product_id

--!https://leetcode.com/problems/project-employees-i/
select project_id,ROUND(avg(experience_years), 2) as average_years from Employee e1, Project p1 where p1.employee_id=e1.employee_id group by project_id

--!https://leetcode.com/problems/sales-analysis-iii/
select product_id,product_name
from product natural join sales
group by product_id
having min(sale_date)>='2019-01-01' and max(sale_date)<='2019-03-31'

--!https://leetcode.com/problems/game-play-analysis-i/
select player_id,min(event_date) as first_login
from Activity
group by player_id

--!https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
select activity_date as day,count(distinct(user_id)) as active_users from Activity group by activity_date having (activity_date > "2019-06-27" AND activity_date <= "2019-07-27");

--!https://leetcode.com/problems/article-views-i/
select distinct(author_id) as id from Views where author_id=viewer_id order by author_id

--!https://leetcode.com/problems/reformat-department-table/
select id, 
	sum(case when month = 'jan' then revenue else null end) as Jan_Revenue,
	sum(case when month = 'feb' then revenue else null end) as Feb_Revenue,
	sum(case when month = 'mar' then revenue else null end) as Mar_Revenue,
	sum(case when month = 'apr' then revenue else null end) as Apr_Revenue,
	sum(case when month = 'may' then revenue else null end) as May_Revenue,
	sum(case when month = 'jun' then revenue else null end) as Jun_Revenue,
	sum(case when month = 'jul' then revenue else null end) as Jul_Revenue,
	sum(case when month = 'aug' then revenue else null end) as Aug_Revenue,
	sum(case when month = 'sep' then revenue else null end) as Sep_Revenue,
	sum(case when month = 'oct' then revenue else null end) as Oct_Revenue,
	sum(case when month = 'nov' then revenue else null end) as Nov_Revenue,
	sum(case when month = 'dec' then revenue else null end) as Dec_Revenue
from department
group by id
order by id

--!https://leetcode.com/problems/queries-quality-and-percentage/
select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from
queries
group by
query_name;

--!https://leetcode.com/problems/average-selling-price/
SELECT p.product_id, IFNULL(round(SUM(p.price*u.units)/sum(u.units),2),0) as average_price
FROM Prices p 
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND 
u.purchase_date BETWEEN p.Start_date and p.end_date
GROUP BY p.product_id

--!https://leetcode.com/problems/students-and-examinations/
SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;

--!https://leetcode.com/problems/list-the-products-ordered-in-a-period/
select product_name, sum(o1.unit) as unit from Products p1 inner join Orders o1 on o1.product_id=p1.product_id where o1.order_date between '2020-02-01' and '2020-02-29' group by p1.product_id having sum(o1.unit)>=100 

--!https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
select eu.unique_id,e.name from Employees e left join EmployeeUNI eu on e.id=eu.id

--!https://leetcode.com/problems/top-travellers/
select name,coalesce(sum(distance), 0) as travelled_distance from Users u left join Rides r on r.user_id=u.id  group by user_id order by sum(distance) desc, name

--!https://leetcode.com/problems/group-sold-products-by-the-date/
select sell_date, count( DISTINCT product ) as num_sold, group_concat(distinct product order by product ASC separator ',' ) as products from Activities group by sell_date order by sell_date;

--!https://leetcode.com/problems/find-users-with-valid-e-mails/
select * from Users where mail regexp '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com';

--!https://leetcode.com/problems/patients-with-a-condition/
select * from Patients where conditions like 'DIAB1%' or conditions like '% DIAB1%';

--!https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans 
from Visits v 
LEFT JOIN Transactions t 
ON v.visit_id = t.visit_id  
WHERE t.transaction_id IS NULL 
GROUP BY v.customer_id; 

--!https://leetcode.com/problems/bank-account-summary-ii/
select u.name as NAME, sum(t.amount) as BALANCE from Users u left join Transactions t on t.account=u.account group by u.name having sum(t.amount)>10000

--!https://leetcode.com/problems/percentage-of-users-attended-a-contest/
select 
contest_id, 
round(count(distinct user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
from  Register
group by contest_id
order by percentage desc,contest_id

--!https://leetcode.com/problems/average-time-of-process-per-machine/
select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time 
from Activity a1, Activity a2 
where a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id;

--!https://leetcode.com/problems/fix-names-in-a-table/
SELECT user_id,CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(name,2,length(name)))) AS name
FROM Users ORDER BY user_id;

--!https://leetcode.com/problems/invalid-tweets/
select tweet_id from Tweets where char_length(content)>15;

--!https://leetcode.com/problems/daily-leads-and-partners/
SELECT date_id, make_name, COUNT(DISTINCT lead_id) as unique_leads, COUNT(DISTINCT partner_id) as unique_partners
FROM DailySales
GROUP BY date_id, make_name
ORDER BY date_id, make_name;

--!https://leetcode.com/problems/find-followers-count/
select user_id, count(follower_id) as followers_count from Followers group by user_id order by user_id

--!https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
select e1.employee_id, e1.name, count(e2.name) as reports_count,round(avg(e2.age)) as average_age from Employees e1, Employees e2 where e1.employee_id=e2.reports_to group by e1.employee_id order by e1.employee_id

--!https://leetcode.com/problems/find-total-time-spent-by-each-employee/
select event_day as day, emp_id, sum(out_time - in_time) as total_time from Employees group by day,emp_id order by day; 

--!https://leetcode.com/problems/recyclable-and-low-fat-products/
select product_id from Products where low_fats='Y' and recyclable='Y'

--!https://leetcode.com/problems/rearrange-products-table/
SELECT product_id,
       'store1' AS store,
       store1 AS price
  FROM Products
 WHERE store1 IS NOT NULL

 UNION

 SELECT product_id,
       'store2' AS store,
       store2 AS price
  FROM Products
 WHERE store2 IS NOT NULL

 UNION

 SELECT product_id,
       'store3' AS store,
       store3 AS price
  FROM Products
 WHERE store3 IS NOT NULL

 ORDER BY product_id, store;

--!https://leetcode.com/problems/calculate-special-bonus/
select employee_id,salary as bonus from Employees where employee_id%2=1 and name not like 'M%'
union
select employee_id,0 as bonus from Employees where employee_id%2=0 or name like 'M%' order by employee_id;

--!https://leetcode.com/problems/the-latest-login-in-2020/
select user_id, max(time_stamp) 'last_stamp'
from logins
where time_stamp like '2020%'
group by user_id ;

--!https://leetcode.com/problems/employees-with-missing-information/
SELECT T.employee_id
FROM  
  (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
   UNION 
   SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
AS T
WHERE T.salary IS NULL OR T.name IS NULL
ORDER BY employee_id;

--!https://leetcode.com/problems/employees-whose-manager-left-the-company/
select employee_id from Employees e1 where salary < 30000 and e1.manager_id NOT IN (
    SELECT employee_id FROM Employees
) order by e1.employee_id;

--!https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
select teacher_id, count(distinct(subject_id)) as cnt from Teacher group by teacher_id;

--!https://leetcode.com/problems/second-highest-salary/
select (select distinct salary as SecondHighestSalary from Employee order by salary desc limit 1 offset 1) as SecondHighestSalary;

--!https://leetcode.com/problems/nth-highest-salary/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT(salary)
          FROM Employee
         ORDER BY salary DESC
         LIMIT 1
        OFFSET N
  );
END

--!https://leetcode.com/problems/consecutive-numbers/
SELECT distinct 
    i1.num as ConsecutiveNums 
FROM 
    logs i1,
    logs i2,
    logs i3
WHERE 
    i1.id=i2.id+1 AND 
    i2.id=i3.id+1 AND 
    i1.num=i2.num AND 
    i2.num=i3.num

--!https://leetcode.com/problems/department-highest-salary/
select d.name as Department, e.name as Employee, e.salary as Salary from Employee e left join Department d on e.departmentId=d.id where 
e.departmentId = d.id AND (e.departmentId, salary) IN 
(SELECT departmentId, MAX(salary) FROM Employee GROUP BY 
departmentId)

--!https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
select m.name
from employee as e
inner join employee as m
on e.managerId=m.id
group by e.managerId 
having count(e.id)>=5

--!https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
select requester_id as id,
       (select count(*) from RequestAccepted
            where id=requester_id or id=accepter_id) as num
from RequestAccepted
group by requester_id
order by num desc limit 1

--!https://leetcode.com/problems/tree-node/
select id, case 
when p_id is null then 'Root'
when p_id in (select id from tree) and id in (select p_id from tree) then 'Inner'
else 'Leaf'
end as type
from Tree

--!https://leetcode.com/problems/customers-who-bought-all-products/
SELECT  customer_id FROM Customer GROUP BY customer_id HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)

--!https://leetcode.com/problems/product-sales-analysis-iii/
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) in (
    SELECT product_id, MIN(year) 
    FROM Sales
    GROUP BY product_id
)

--!https://leetcode.com/problems/game-play-analysis-iv/
SELECT
  ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
  Activity
WHERE
  (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
  IN (
    SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id
  )

--!https://leetcode.com/problems/market-analysis-i/
select u.user_id as buyer_id, u.join_date, IFNULL(count(o.order_date), 0) as orders_in_2019 from Users u LEFT JOIN Orders o on u.user_id=o.buyer_id and year(o.order_date)=2019 group by u.user_id;

--!https://leetcode.com/problems/immediate-food-delivery-ii/
select round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage 
from Delivery where (customer_id, order_date) in (
  select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);

--!https://leetcode.com/problems/monthly-transactions-i/
SELECT  
SUBSTR(trans_date,1,7) as month, 
country, 
count(id) as trans_count, 
SUM(CASE WHEN state = 'approved' then 1 else 0 END) as approved_count,
SUM(amount) as trans_total_amount, 
SUM(CASE WHEN state = 'approved' then amount else 0 END) as approved_total_amount
FROM Transactions
GROUP BY month, country

--!https://leetcode.com/problems/last-person-to-fit-in-the-bus/
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

--!https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
select * from CITY where population>100000 and countrycode='USA'

--!https://www.hackerrank.com/challenges/revising-the-select-query-2/
select name from city  where countrycode='USA' and population>120000

--!https://www.hackerrank.com/challenges/select-all-sql/
select * from city

--!https://www.hackerrank.com/challenges/select-by-id/
select * from city where id=1661

--!https://www.hackerrank.com/challenges/japanese-cities-attributes/
select * from CITY where COUNTRYCODE='JPN'

--!https://www.hackerrank.com/challenges/japanese-cities-name/
select name from CITY where COUNTRYCODE='JPN'

--!https://www.hackerrank.com/challenges/weather-observation-station-1/
select CITY,STATE from STATION

--!https://www.hackerrank.com/challenges/weather-observation-station-3/
select distinct CITY from STATION where MOD(id,2)=0

--!https://www.hackerrank.com/challenges/weather-observation-station-6/
select distinct city from station where city like "[aeiou]%"

--!https://www.hackerrank.com/challenges/weather-observation-station-7/
select distinct city from station where city like "%[aeiou]"

--!https://www.hackerrank.com/challenges/weather-observation-station-8/
select distinct city from station where city like "[aeiou]%[aeiou]"

--!https://www.hackerrank.com/challenges/weather-observation-station-9/
select distinct city from station where city not like "[aeiou]%"

--!https://www.hackerrank.com/challenges/weather-observation-station-10/
select distinct city from station where city not like "%[aeiou]"

--!https://www.hackerrank.com/challenges/salary-of-employees/
select name from Employee where salary>2000 and months<10 order by employee_id

--!https://leetcode.com/problems/investments-in-2016/
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)