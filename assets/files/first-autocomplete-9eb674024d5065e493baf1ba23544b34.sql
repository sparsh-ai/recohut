SELECT searches,
       COUNT(*) AS users
  FROM (
SELECT user_id,
       COUNT(*) AS searches
  FROM (
SELECT x.session_start,
       x.session,
       x.user_id,
       x.first_search,
       COUNT(CASE WHEN x.event_name = 'search_autocomplete' THEN x.user_id ELSE NULL END) AS autocompletes
  FROM (
SELECT e.*,
       first.first_search,
       session.session,
       session.session_start
  FROM tutorial.yammer_events e
  JOIN (
       SELECT user_id,
              MIN(occurred_at) AS first_search
         FROM tutorial.yammer_events
        WHERE event_name = 'search_autocomplete'
        GROUP BY 1
       ) first
    ON first.user_id = e.user_id
   AND first.first_search <= '2014-08-01'
  LEFT JOIN (
       SELECT user_id,
              session,
              MIN(occurred_at) AS session_start,
              MAX(occurred_at) AS session_end
         FROM (
              SELECT bounds.*,
              		    CASE WHEN last_event >= INTERVAL '10 MINUTE' THEN id
              		         WHEN last_event IS NULL THEN id
              		         ELSE LAG(id,1) OVER (PARTITION BY user_id ORDER BY occurred_at) END AS session
                FROM (
                     SELECT user_id,
                            event_type,
                            event_name,
                            occurred_at,
                            occurred_at - LAG(occurred_at,1) OVER (PARTITION BY user_id ORDER BY occurred_at) AS last_event,
                            LEAD(occurred_at,1) OVER (PARTITION BY user_id ORDER BY occurred_at) - occurred_at AS next_event,
                            ROW_NUMBER() OVER () AS id
                       FROM tutorial.yammer_events e
                      WHERE e.event_type = 'engagement'
                      ORDER BY user_id,occurred_at
                     ) bounds
               WHERE last_event >= INTERVAL '10 MINUTE'
                  OR next_event >= INTERVAL '10 MINUTE'
               	 OR last_event IS NULL
              	 	 OR next_event IS NULL   
              ) final
        GROUP BY 1,2
       ) session
    ON session.user_id = e.user_id
   AND session.session_start <= e.occurred_at
   AND session.session_end >= e.occurred_at
   AND session.session_start <= first.first_search + INTERVAL '30 DAY'
 WHERE e.event_type = 'engagement'
       ) x
 GROUP BY 1,2,3,4
       ) z
 WHERE z.autocompletes > 0
 GROUP BY 1
       ) z
 GROUP BY 1
 ORDER BY 1
LIMIT 100