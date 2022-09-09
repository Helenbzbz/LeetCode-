# Write your MySQL query statement below
with group_player as (select
    group_id,
    player,
    sum(score) as total_amount
from
(select match_id, first_player as player, first_score as score
from Matches
union
select match_id, second_player as player, second_score as score
from Matches) as ps
join Players as p
on ps.player = p.player_id
group by 1,2)

select group_id  as GROUP_ID, player as PLAYER_ID from (
select
    group_id,
    player,
    total_amount,
    rank() over(partition by group_id order by total_amount desc, player asc) as rank_id
    from group_player
    ) as gp
    where rank_id = 1
    
