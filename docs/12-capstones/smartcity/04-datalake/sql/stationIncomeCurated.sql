SELECT 
  "station-st-id",
  "location",
  SUM("price") as stationIncome
FROM 
  "swipebike"."c_stationincome" 
GROUP BY 
  "station-st-id",
  "location"
ORDER BY 3 DESC
  
