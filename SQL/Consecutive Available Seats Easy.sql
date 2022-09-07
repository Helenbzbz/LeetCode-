# Write your MySQL query statement below
with availability as (select
    a.seat_id,
    a.free as this,
    l.free as lef,
    r.free as righ
from Cinema a
left join Cinema l on a.seat_id -1 = l.seat_id
left join Cinema r on a.seat_id +1 = r.seat_id)

select
    seat_id
from availability
where this = 1
and (lef = 1 or righ = 1)
