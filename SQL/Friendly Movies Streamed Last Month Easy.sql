# Write your MySQL query statement below
select
    distinct title
from TVProgram t join Content c on t.content_id = c.content_id
where Kids_content = 'Y' and program_date like '2020-06%'
and content_type = 'Movies'
