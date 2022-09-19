# Write your MySQL query statement below
select
    distinct viewer_id as id
from(
select
    viewer_id,
    view_date,
    count(distinct article_id) as art_count
from Views
group by 1,2
) as article_num
where art_count >1
order by 1
