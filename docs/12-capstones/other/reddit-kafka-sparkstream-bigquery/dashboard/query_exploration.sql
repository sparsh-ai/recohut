--Submissions Table should be Unique (One Row per Submission)
--Comments Table might have duplicates

SELECT submission.* EXCEPT(create_time, ups, upvote_ratio, images, videos, num_comments), 
       comments.id AS comment_id,
       comments.author AS comment_author,
       comments.author_flair AS comment_author_flair,
       comments.text_body	AS comment_text_body,
       comments.parent_id	AS comment_parent_id,
       comments.link_id AS comment_link_id,
       comment_datetime,
       CASE WHEN comments.parent_id = comments.link_id THEN 1 ELSE 0 END AS direct_comment_flag, 
       CASE 
              WHEN comments.id IS NOT NULL THEN ROW_NUMBER() OVER (PARTITION BY submission.id ORDER BY comment_datetime ASC) 
              ELSE NULL
       END AS rank_comment_order, 
       COUNT(DISTINCT images.element) AS num_images,
       COUNT(DISTINCT videos.element) AS num_videos,
       STRING_AGG(images.element) AS string_submission_images,
       STRING_AGG(videos.element) AS string_submission_videos,
FROM `learning-gcp-356802.fedex_reddit_dataset.submissions` AS submission
LEFT JOIN UNNEST(submission.images.list) AS images
LEFT JOIN UNNEST(submission.videos.list) AS videos
LEFT JOIN (
       -- There might be duplicates here
       SELECT DISTINCT id, author, author_flair, text_body, parent_id, link_id, comment_datetime 
       FROM `learning-gcp-356802.fedex_reddit_dataset.comments`
) AS comments ON submission.id = comments.link_id
GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ORDER BY submission.id