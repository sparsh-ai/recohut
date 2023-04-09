with test_summaries as(

    with distance_summaries as(
        select type,max(traveled_d) from endpoints_trafficinfo group by type
    ),
    speed_summaries as(
        select type,max(speed) from endpoints_trafficinfo group by type
    ),
    time_summaries as(
        select type,max(time) from endpoints_trafficinfo group by type
    )
)

select * from test_summaries