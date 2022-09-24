SELECT q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

with cumu_weight as (select
    a.person_id,
    sum(b.weight) as cumulative_weight,
    a.turn,
    a.person_name
from Queue a join Queue b on a.turn >= b.turn
group by 1,3,4)

select
    person_name
from cumu_weight
where cumulative_weight <= 1000
order by cumulative_weight desc limit 1
