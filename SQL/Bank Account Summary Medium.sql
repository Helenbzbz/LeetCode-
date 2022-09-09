# Write your MySQL query statement below
with pay as (select
    paid_by,
    sum(amount) as pay
    from Transactions
    group by 1),
    
    receive as (select
    paid_to,
    sum(amount) as receive
    from Transactions
    group by 1),
    
    bal_change as (select
    user_id,
    user_name,
    case when pay is not null then pay else 0 end as pay,
    case when receive is not null then receive else 0 end as receive,
    credit
    from Users
    left join pay on pay.paid_by = Users.user_id
    left join receive on receive.paid_to = Users.user_id)
    
    select
    user_id,
    user_name,
    credit - pay + receive as credit,
    case when (credit - pay + receive) <0 then 'Yes'
    else 'No' end as credit_limit_breached
    from bal_change
