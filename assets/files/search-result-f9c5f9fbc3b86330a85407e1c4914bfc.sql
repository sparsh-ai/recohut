SELECT TRIM('search_click_result_' FROM event_name)::INT AS search_result,
       COUNT(*) AS clicks
  FROM tutorial.yammer_events
 WHERE event_name LIKE 'search_click_%'
 GROUP BY 1
 ORDER BY 1