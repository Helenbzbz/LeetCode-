# Write your MySQL query statement below
select
    ad_id,
    if (ctr is not null, round(ctr*100,2), 0.00) as ctr
from
(select
    ad_id,
    sum(case when action = 'Clicked'then 1 else 0 end)/sum(case when action = 'Clicked' or action = 'Viewed' then 1 else 0 end) as ctr
    from Ads
    group by 1) as pre
order by ctr desc, ad_id asc
