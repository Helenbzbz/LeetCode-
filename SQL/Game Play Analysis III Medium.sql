# Write your MySQL query statement below
select
    l1.player_id,
    l1.event_date,
    sum(l2.games_played) as games_played_so_far
from Activity as l1
left join Activity as l2
on l1.player_id = l2.player_id
    and l1.event_date >= l2.event_date
group by
1, 2


SELECT
player_id, event_date, sum(games_played) over(PARTITION BY player_id ORDER BY event_date)
AS 'games_played_so_far'
FROM activity
ORDER BY player_id, games_played_so_far;
