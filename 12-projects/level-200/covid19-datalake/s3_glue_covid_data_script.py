import redshift_connector
conn = redshift_connector.connect(
    host='my-first-redshift-cluster.cpsgscpuauoo.ap-south-1.redshift.amazonaws.com',
    database = 'dev',
    user = 'awsuser',
    password = 'Geforce1050',
    port = 5439
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE "dimDate" (
"index" INTEGER,
  "fips" REAL,
  "date" TIMESTAMP,
  "year" INTEGER,
  "month" INTEGER,
  "day_of_week" INTEGER
)
""")
cursor.execute("""
CREATE TABLE "dimRegion" (
"index" INTEGER,
  "fips" REAL,
  "province_state" TEXT,
  "country_region" TEXT,
  "latitude" REAL,
  "longitude" REAL,
  "county" TEXT,
  "state" TEXT
)
""")

cursor.execute("""
CREATE TABLE "factCovid" (
"index" INTEGER,
  "fips" REAL,
  "province_state" TEXT,
  "country_region" TEXT,
  "confirmed" REAL,
  "deaths" REAL,
  "recovered" REAL,
  "active" REAL,
  "date" INTEGER,
  "positive" INTEGER,
  "negative" REAL,
  "hospitalizedcurrently" REAL,
  "hospitalized" REAL,
  "hospitalizeddischarged" REAL
)
""")
cursor.execute("""
copy dimDate from 's3://shyan-covid19-de-project/output/dimDate.csv'
credentials 'aws_iam_role=arn:aws:iam::470048303105:role/redshift-s3-access'
delimiter ','
region 'ap-south-1'
IGNOREHEADER 1
""")
cursor.execute("""
copy dimRegion from 's3://shyan-covid19-de-project/output/dimRegion.csv'
credentials 'aws_iam_role=arn:aws:iam::470048303105:role/redshift-s3-access'
delimiter ','
region 'ap-south-1'
IGNOREHEADER 1
""")

cursor.execute("""
copy factCovid from 's3://shyan-covid19-de-project/output/factCovid.csv'
credentials 'aws_iam_role=arn:aws:iam::470048303105:role/redshift-s3-access'
delimiter ','
region 'ap-south-1'
IGNOREHEADER 1
""")
