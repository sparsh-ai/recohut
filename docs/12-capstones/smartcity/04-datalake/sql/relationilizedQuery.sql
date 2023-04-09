SELECT 
  R."stationid", 
  R."bikedetail.bikenum", 
  bd."bikedetail.bikeattributes.val.attribname" AS attribName, 
  bd."bikedetail.bikeattributes.val.attribvalue" AS attribValue
FROM 
  "swipebike"."c_rides" r,
  "swipebike"."c_rides_bikedetail_bikeattributes" bd 
WHERE
  R."bikedetail.bikenum" = 'a33492a7-d59f-4484-bb37-7431252d8099' AND
  R."price" = 67 AND
  R."stationid" = 130 AND
  R."bikedetail.bikeattributes" = bd."id"
