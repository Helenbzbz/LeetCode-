# Write your MySQL query statement below
select
    e.left_operand,
    e.operator,
    e.right_operand,
    case
    when operator = '>' then if(a.value > b.value, 'true', 'false')
    when operator = '=' then if(a.value = b.value, 'true', 'false')
    when operator = '<' then if(a.value < b.value, 'true', 'false')
    end as value
from Expressions e
join Variables a on a.name = e.left_operand
join Variables b on b.name = e.right_operand
