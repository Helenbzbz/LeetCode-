# Write your MySQL query statement below
select
    s.student_id,
    s.student_name,
    su.subject_name,
    count(e.student_id) as attended_exams
from students s cross join subjects su
left join examinations e on e.student_id = s.student_id
and su.subject_name = e.subject_name
group by 1,2,3
order by 1,3
