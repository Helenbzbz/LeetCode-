# Write your MySQL query statement below
with report_num as (
select
    managerID,
    count(distinct id) as report_count
from Employee
group by managerID)

select
name
from report_num rn
join Employee em on rn.managerID = em.id
where report_count >=5

# Use having will make the query faster and shorter
# Use select name, join and gourp by manager ID to show all the name of manager but then use the having clause to filter out only the one with >5 employee

select
    em.name
from Employee as em
join employee as em2
on em.id = em2.managerID
group by em2.managerID
having count(em2.managerID) >=5
