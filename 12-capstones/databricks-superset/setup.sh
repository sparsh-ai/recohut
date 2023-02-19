aws s3 cp s3://wysde-assets/projects/databricks-superset/solution.zip ./
unzip solution.zip
rm solution.zip
mv solution/* .
rm -r solution