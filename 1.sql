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