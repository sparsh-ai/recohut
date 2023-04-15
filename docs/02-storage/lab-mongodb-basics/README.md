# Lab: MongoDB Basics

## Environment Setup

Connect to Atlas Cluster:

```sh
mongosh "mongodb+srv://cluster0.css32tr.mongodb.net/myFirstDatabase" --apiVersion 1 --username admin
```

## MongoDB CRUD

Run the below code on mongo console. It will insert 5 documents, which will serve as sample data for the the assignment.

```sql
use training
db.languages.insert({"name":"java","type":"object oriented"})
db.languages.insert({"name":"python","type":"general purpose"})
db.languages.insert({"name":"scala","type":"functional"})
db.languages.insert({"name":"c","type":"procedural"})
db.languages.insert({"name":"c++","type":"object oriented"})
```

Task 1: Insert an entry for 'Haskell' programming language which is of type 'functional

```sql
db.languages.insert({"name":"Haskell","type":"functional"})
```

Task 2: Query for all functional languages

```sql
db.languages.find({"type":"functional"})
```

Task 3: Add ‘Bjarne Stroustrup’ as creator for c++

```sql
db.languages.updateMany({"name":"c++"},{$set:{"creator":"Bjarne Stroustrup"}})
```

Task 4: Delete all functional programming languages

```sql
db.languages.remove({"type":"functional"})
```

Task 5: Disconnect from the mongodb server

```sql
exit
```

## MongoDB Indexing

Task 1: Create a collection named bigdata

```sql
db.createCollection("bigdata")
```

**Insert documents**

-   Let us insert a lot of documents into the newly created collection.
-   This should take around 3 minutes, so please be patient.
-   The code given below will insert 200000 documents into the 'bigdata' collection.
-   Each document would have a field named **account_no** which is a simple auto increment number.
-   And a field named **balance** which is a randomly generated number, to simulate the bank balance for the account.

Copy the below code and paste it on the mongo client.

```sql
use training
for (i=1;i<=200000;i++){print(i);db.bigdata.insert({"account_no":i,"balance":Math.round(Math.random()*1000000)})}
```

Task 2: Verify that 200000 documents got inserted

```sql
db.bigdata.count()
```

Task 3: Measure the time taken by a query

Let us run a query and find out how much time it takes to complete.

Let us query for the details of account number 58982.

We will make use of the explain function to find the time taken to run the query in milliseconds.

```sql
db.bigdata.find({"account_no":58982}).explain("executionStats").executionStats.executionTimeMillis
```

**Working with indexes**

Before you create an index, choose the field you wish to create an index on. It is usually the field that you query most.

Run the below command to create an index on the field account_no.

```sql
db.bigdata.createIndex({"account_no":1})
```

Task 4: Get a list of indexes on the ‘bigdata’ collection.

```sql
db.bigdata.getIndexes()
```

Task 5: Find out how effective an index is

Let us query for the details of account number 69271:

```sql
db.bigdata.find({"account_no": 69271}).explain("executionStats").executionStats.executionTimeMillis
```

Task 6: Delete the index we created earlier

```sql
db.bigdata.dropIndex({"account_no":1})
```

Task 7: Create an index on the balance field

```sql
db.bigdata.createIndex({"balance":1})
```

Task 8: Query for documents with a balance of 10000 and record the time taken

```sql
db.bigdata.find({"balance":10000}).explain("executionStats").executionStats.executionTimeMillis
```

Task 9: Drop the index you have created

```sql
db.bigdata.dropIndex({"balance":1})
```

Task 10: Query for documents with a balance of 10000 and record the time taken, and compare it with the previously recorded time

```sql
db.bigdata.find({"balance": 10000}).explain("executionStats").executionStats.executionTimeMillis
```

Task 11: Disconnect from the mongodb server

```sql
exit
```

## MongoDB Aggregation

Load sample data into the training database:

```sql
use training
db.marks.insert({"name":"Ramesh","subject":"maths","marks":87})
db.marks.insert({"name":"Ramesh","subject":"english","marks":59})
db.marks.insert({"name":"Ramesh","subject":"science","marks":77})
db.marks.insert({"name":"Rav","subject":"maths","marks":62})
db.marks.insert({"name":"Rav","subject":"english","marks":83})
db.marks.insert({"name":"Rav","subject":"science","marks":71})
db.marks.insert({"name":"Alison","subject":"maths","marks":84})
db.marks.insert({"name":"Alison","subject":"english","marks":82})
db.marks.insert({"name":"Alison","subject":"science","marks":86})
db.marks.insert({"name":"Steve","subject":"maths","marks":81})
db.marks.insert({"name":"Steve","subject":"english","marks":89})
db.marks.insert({"name":"Steve","subject":"science","marks":77})
db.marks.insert({"name":"Jan","subject":"english","marks":0,"reason":"absent"})
```

### Assignment 1

Task 1: Limiting the rows in the output - print only 2 documents from the marks collection

```sql
use training
db.marks.aggregate([{"$limit":2}])
```

Task 2: Sorting based on a column - sorts the documents based on field marks in ascending/descending order

```sql
-- ascending
db.marks.aggregate([{"$sort":{"marks":1}}])

--descending
db.marks.aggregate([{"$sort":{"marks":-1}}])
```

Task 3: Sorting and limiting - create a two stage pipeline that answers the question `What are the top 2 marks?`

```sql
db.marks.aggregate([
{"$sort":{"marks":-1}},
{"$limit":2}
])
```

Task 4: Group by - prints the average marks across all subjects

```sql
db.marks.aggregate([
{
    "$group":{
        "_id":"$subject",
        "average":{"$avg":"$marks"}
        }
}
])
```

Task 5: Write the SQL equivalent of the above query

```sql
SELECT subject, average(marks)
FROM marks
GROUP BY subject
```

Task 6: Write a query to answer this question - `Who are the top 2 students by average marks?`

This involves:

- finding the average marks per student.
- sorting the output based on average marks in descending order.
- limiting the output to two documents.

```sql
db.marks.aggregate([
{
    "$group":{
        "_id":"$name",
        "average":{"$avg":"$marks"}
        }
},
{
    "$sort":{"average":-1}
},
{
    "$limit":2
}
])
```

### Assignment 2

Task 1: Find the total marks for each student across all subjects

```sql
db.marks.aggregate([
    {
        "$group":{"_id":"$name","total":{"$sum":"$marks"}}
    }
])
```

Task 2: Find the maximum marks scored in each subject

```sql
db.marks.aggregate([
    {
        "$group":{"_id":"$subject","max_marks":{"$max":"$marks"}}
    }
])
```

Task 3: Find the minimum marks scored by each student

```sql
db.marks.aggregate([
    {
        "$group":{"_id":"$name","min_marks":{"$min":"$marks"}}
    }
])
```

Task 4: Find the top two subjects based on average marks

```sql
db.marks.aggregate([
{
    "$group":{
        "_id":"$subject",
        "average":{"$avg":"$marks"}
        }
},
{
    "$sort":{"average":-1}
},
{
    "$limit":2
}
])
```

Task 5: Disconnect from the mongodb server

```sql
exit
```