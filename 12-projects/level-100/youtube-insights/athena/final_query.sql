SELECT snippet_title, views, likes, comment_count, channel_title, title, region  FROM "final_analytics" 
WHERE region='us'
ORDER BY views desc;