# Write your MySQL query statement below
select
    x,
    y,
    z,
    if (z>=x+y or x>=y+z or y>=x+z, 'No', 'Yes') as triangle
from Triangle
