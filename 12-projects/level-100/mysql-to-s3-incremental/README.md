# Reading data from MySQL in CSV and saving into S3

In this lab, we are loading the data from RDS MySQL Database into CSV and then saving that csv into S3 using Boto3.

We are loading the data in batch as well as in incremental fashion.

## Batch mode

```py title="./src/extract_mysql_full.py"
conn = pymysql.connect(host=hostname,
    user=username,
    password=password,
    db=dbname,
    port=int(port))

m_query = "SELECT * FROM orders;"
local_filename = "order_extracts.csv"

m_cursor = conn.cursor()
m_cursor.execute(m_query)
results = m_cursor.fetchall()

with open(local_filename, 'w') as fp:
    csv_w = csv.writer(fp, delimiter='|')
    csv_w.writerows(results)

fp.close()
m_cursor.close()
conn.close()

# load the aws_boto_credentials values:
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

s3 = boto3.client('s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key)

s3_file = local_filename

s3.upload_file(local_filename, bucket_name, s3_file)
```

## Incremental mode

```py title="./src/extract_mysql_incremental.py"
rs_conn = psycopg2.connect(
    "dbname=" + dbname
    + " user=" + user
    + " password=" + password
    + " host=" + host
    + " port=" + port
)

rs_sql = """ select coalesce(max(lastupdated), 
    '1900-01-01')
    from orders;"""
rs_cursor = rs_conn.cursor()
rs_cursor.execute(rs_sql)
result = rs_cursor.fetchone()

# There's only one row and column returned
last_updated_warehouse = result[0]

rs_cursor.close()
rs_conn.commit()

conn = pymysql.connect(host=hostname,
    user=username,
    password=password,
    db=dbname,
    port=int(port))

if conn is None:
    print("Error connecting to the MySQL database")
else:
    print("MySQL connection established!")

m_query = """SELECT * 
    FROM orders
    WHERE lastupdated > %s;"""
local_filename = "order_extracts_incremental.csv"

m_cursor = conn.cursor()
m_cursor.execute(m_query, (last_updated_warehouse,))
results = m_cursor.fetchall()

with open(local_filename, 'w') as fp:
    csv_w = csv.writer(fp, delimiter='|')
    csv_w.writerows(results)

fp.close()
m_cursor.close()
conn.close()

# load the aws_boto_credentials values:
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

s3 = boto3.client('s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key)

s3_file = local_filename

s3.upload_file(local_filename, bucket_name, s3_file)
```