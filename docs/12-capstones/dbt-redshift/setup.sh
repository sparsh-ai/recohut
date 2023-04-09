aws s3 cp s3://wysde-assets/projects/dbt-redshift/solution.zip ./
unzip solution.zip
rm solution.zip
mv solution/* .
rm -r solution