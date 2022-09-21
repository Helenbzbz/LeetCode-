# Write your MySQL query statement below
select
distinct page_id as recommended_page
from Likes l join Friendship f on l.user_id = f.user2_id and user1_id = 1
or l.user_id = f.user1_id and user2_id = 1
where page_id not in (select page_id from Likes where user_id = 1)
