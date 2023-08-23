# Write your MySQL query statement below
select person.email from
person group by person.email having count(person.email)>1