SELECT DATE_TRUNC('day',created_at) AS day,
       COUNT(*) AS all_users,
       COUNT(CASE WHEN activated_at IS NOT NULL THEN u.user_id ELSE NULL END) AS activated_users
  FROM tutorial.yammer_users u
 WHERE created_at >= '2014-06-01'
   AND created_at < '2014-09-01'
 GROUP BY 1
 ORDER BY 1