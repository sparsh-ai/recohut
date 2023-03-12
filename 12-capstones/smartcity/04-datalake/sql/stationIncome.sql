SELECT 
  r."stationid",
  s."location",
  SUM(r."price") AS stationIncome
FROM 
"swipebike"."rides" r,
"swipebike"."stations" s
WHERE 
  r."stationid" = s."stationid"
GROUP BY 
  r."stationid",
  s."location"
order by 3 desc
