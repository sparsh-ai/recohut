SELECT a.title, a.category_id, b.snippet_title FROM "dataengineer-youtube_raw"."raw_statistics" a
INNER JOIN "db_youtube_cleaned"."cleaned_statistics_reference_data" b ON a.category_id=b.id
WHERE a.region='ca';