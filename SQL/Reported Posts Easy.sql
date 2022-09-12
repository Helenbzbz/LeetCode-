# Write your MySQL query statement below
    # select
    #     report_reason,
    #     count(post_id) as report_count
    # from(
    # select
    #     distinct post_id,
    #     extra as report_reason
    # from Actions
    # where action = 'report'
    # and action_date = '2019-07-04'
    # ) as distinct_report
    #     group by 1
        
# A faster way is to count distinct post_id !
    select
        extra as report_reason,
        count(distinct post_id) as report_count
    from Actions
    where action = 'report'
    and action_date = '2019-07-04'
        group by 1
