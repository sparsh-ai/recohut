# category 당 선호도
# 패키지를 가져오고
from pyspark import SparkConf, SparkContext
import pandas as pd

# Spark 설정
conf = SparkConf().setMaster("local").setAppName("restaurant-reviews")
sc = SparkContext(conf=conf)

# 우리가 가져올 데이터가 있는 파일
directory = "/Users/keon/fastcampus/data-engineering/01-spark/data"
filename = "restaurant_reviews.csv"

# 데이터 파싱
lines = sc.textFile(f"file:///{directory}/{filename}")
header = lines.first() 
filtered_lines = lines.filter(lambda row:row != header) 

# 필요한 부분만 골라내서 세는 부분
# countByValue로 같은 날짜등장하는 부분을 센다
def parse(filtered_lines):
  fields = filtered_lines.split(",")
  category = str(fields[2])
  reviews = int(fields[3])
  return (category, reviews)

categoryReviews = filtered_lines.map(parse)

result1 = categoryReviews.take(10)
result2 = categoryReviews.mapValues(lambda x: (x, 1)).collect()
# 카테고리당 
categoryReviewsCount = categoryReviews.mapValues(lambda x: (x, 1))

reduced = categoryReviewsCount.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
averages = reduced.mapValues(lambda x: x[0] / x[1])
res = averages.collect()
print(res)