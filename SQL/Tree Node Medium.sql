# Write your MySQL query statement below
# The key is understand you can use in and = to set a condition from a select in a ()
select
    id,
    case 
    when tree.id = (select a.id from tree as a where a.p_id is null)
    then 'Root'
    when tree.id in (select a.p_id from tree as a)
    then 'Inner'
    else 'Leaf'
    end as type
    from tree
    
