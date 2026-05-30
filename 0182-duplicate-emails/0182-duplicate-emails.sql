# Write your MySQL query statement below
select email as Email
from person
Group by Email
having count(Email) > 1
