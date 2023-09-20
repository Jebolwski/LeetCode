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
