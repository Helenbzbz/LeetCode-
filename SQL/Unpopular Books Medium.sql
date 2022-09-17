# Write your MySQL query statement below
with books_avai as (select
    book_id,
    name
from Books
where available_from < '2019-05-23'),

one_year as(
select book_id, quantity from Orders
where dispatch_date >'2018-06-23')

select b.book_id, name
from books_avai b left join one_year o on b.book_id = o.book_id
group by 1,2
having sum(quantity) < 10 or sum(quantity) is null
