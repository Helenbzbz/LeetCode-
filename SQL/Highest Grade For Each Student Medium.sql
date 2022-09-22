# Write your MySQL query statement below
select
    student_id,
    course_id,
    grade
from
(select
    rank() over (partition by student_id order by grade desc, course_id asc) as rank_id,
    student_id,
    course_id,
    grade
from Enrollments) as ranked
where rank_id = 1
