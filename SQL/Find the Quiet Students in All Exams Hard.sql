# Write your MySQL query statement below
with ranked as (select
    student_id,
    rank() over(partition by exam_id order by score desc) as high_rank,
    rank() over(partition by exam_id order by score asc) as low_rank,
    exam_id
from Exam)

select
    s.student_id,
    student_name
from (select
    student_id,
    count(student_id) as exam_count,
    sum(case when high_rank = 1 or low_rank = 1 then 0 else 1 end) as quiet_count
from ranked group by 1) as q
join Student s on q.student_id = s.student_id
where exam_count = quiet_count
