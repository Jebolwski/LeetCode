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