# Create a Data Model for an Email System

## Conceptual Data Model

A conceptual data model is designed with the goal of understanding data in a particular domain. In this example, the model is captured using an Entity-Relationship Diagram (ERD) that documents entity types, relationship types, attribute types, and cardinality and key constraints.

![](https://user-images.githubusercontent.com/62965911/214248154-dba659ef-cf4e-46f3-9239-57584ca9f909.png)

The conceptual data model for messaging data features users, folders, emails and email attachments. A user is identified by a unique username and may have other attributes like name. A folder has a label and color, and is uniquely identified by a combination of a label and username. An email has a unique id, timestamp, one or more recipients, one sender, subject and body. While a user can own many folders, each folder can only belong to one user. Similarly, an email can have many attachments, but an attachment always belongs to exactly one email. Finally, a user can have multiple emails and each email can be seen by multiple users. Since an email can have many labels, it can appear in many folders.

## Application workflow

An application workflow is designed with the goal of understanding data access patterns for a data-driven application. Its visual representation consists of application tasks, dependencies among tasks, and data access patterns. Ideally, each data access pattern should specify what attributes to search for, search on, order by, or do aggregation on.

![](https://user-images.githubusercontent.com/62965911/214248142-9b916756-9267-4aa5-ac85-ba8f99a3e6e1.png)

First, the application workflow has an entry-point task that shows all folders that belong to a particular user. This task requires querying a database to find information about folder labels, colors and unread email quantities for a given user, which is documented as Q1 on the diagram. Second, an application can proceed to display all emails with a given label based on a user folder selection, which requires data access pattern Q2. The resulting list of emails should be sorted using email timestamps, showing the most recent emails at the top. Third, the next task can show all information about an individual email selected by a user, which requires data access pattern Q3. Finally, the task of downloading an individual email attachment is based on data access pattern Q4. All in all, there are four data access patterns for a database to support.

## Logical Data model

A logical data model results from a conceptual data model by organizing data into Cassandra-specific data structures based on data access patterns identified by an application workflow. Logical data models can be conveniently captured and visualized using Chebotko Diagrams that can feature tables, materialized views, indexes and so forth.

![](https://user-images.githubusercontent.com/62965911/214248160-3867a4f2-a31e-4cd4-918a-c3ddf20205ca.png)

The logical data model for messaging data is represented by the shown Chebotko Diagram. There are four tables, namely folders_by_user, emails_by_user_folder, emails and attachments, that are designed to specifically support data access patterns Q1, Q2, Q3 and Q4, respectively. Table folders_by_user is designed to have a separate partition for each user, and each partition can contain multiple rows capturing information about individual folders. Therefore, Q1 can be satisfied by retrieving all rows from one partition. Table emails_by_user_folder has a composite partition key, consisting of columns username and label, and a composite clustering key, consisting of columns timestamp and id. It is designed to store all emails that belong to the same folder in one partition, where each individual email maps to a row. Similarly to Q1, Q2 can be satisfied by accessing only one partition. Finally, tables emails and attachments are single-row partition tables that are designed to store one email or one attachment per partition, respectively. Access patterns Q3 and Q4 require retrieving one row from one partition. While this design is straightforward, notice how each email or attachment is intended to be stored only one time, even though they can be accessed by many users via many folders.

## Physical Data Model
A physical data model is directly derived from a logical data model by analyzing and optimizing for performance. The most common type of analysis is identifying potentially large partitions. Some common optimization techniques include splitting and merging partitions, data indexing, data aggregation and concurrent data access optimizations.

![](https://user-images.githubusercontent.com/62965911/214248167-78290bd2-fcf7-40c3-a90d-6f16f3a753db.png)

The physical data model for messaging data is visualized using the Chebotko Diagram. This time, all table columns have associated data types. In addition, every table has some column-related changes, and there is even one new table. Table folders_by_user no longer has column num_unread as it is now part of new table unread_email_stats. The new table is necessary to be able to use the COUNTER data type: any table with one or more counter columns cannot have non-counter columns other than primary key columns. Tables emails_by_user_folder and emails no longer have separate columns to store email timestamps because, in both cases, timestamps can be easily extracted from column id of type TIMEUUID. Furthermore, in the case of table emails_by_user_folder, the clustering order is going to be based on timestamps. It is worth mentioning that partitions in table emails_by_user_folder can grow over time to become very large. However, instead of introducing a new column into the partition key, overflow labels can be used. For example, if a folder with the inbox label becomes too big, the system can automatically start using a new label like inbox-overflow-1 to store more emails, which should be transparent to the user. Finally, column chunk_number is introduced into the partition key of table attachments to be able to divide large attachments into smaller chunks and store them separately. For example, assuming the chunk size limit of 1000KB, a 530KB file can be stored as one chunk and a 2416KB file has to be stored using three chunks. This optimization helps to store and retrieve large attachments faster since different nodes in a cluster may be able to handle different chunks in parallel. Our final blueprint is ready to be instantiated in Cassandra.

## Hands-on

In this lab, you will:

- Create tables for a messaging data use case
- Populate tables with sample messaging data
- Design and execute CQL queries over messaging data

### Create Keyspace

```sql
CREATE KEYSPACE messaging_data
WITH replication = {
  'class': 'SimpleStrategy', 
  'replication_factor': 1 }; 

USE messaging_data;
```

### Create Tables

```sql
CREATE TABLE IF NOT EXISTS folders_by_user (
  username TEXT,
  label TEXT,
  color TEXT,
  PRIMARY KEY ((username),label)
);

CREATE TABLE IF NOT EXISTS unread_email_stats (
  username TEXT,
  label TEXT,
  num_unread COUNTER,
  PRIMARY KEY ((username),label)
);

CREATE TABLE IF NOT EXISTS emails_by_user_folder (
  username TEXT,
  label TEXT,
  id TIMEUUID,
  "from" TEXT,
  subject TEXT,
  is_read BOOLEAN,
  PRIMARY KEY ((username,label),id)
) WITH CLUSTERING ORDER BY (id DESC);

CREATE TABLE IF NOT EXISTS emails (
  id TIMEUUID,
  "to" LIST<TEXT>,
  "from" TEXT,
  subject TEXT,
  body TEXT,
  attachments MAP<TEXT,INT>,
  PRIMARY KEY ((id))
);

CREATE TABLE IF NOT EXISTS attachments (
  email_id TIMEUUID,
  filename TEXT,
  chunk_number INT,
  type TEXT,
  value BLOB,
  PRIMARY KEY ((email_id,filename,chunk_number))
);

DESCRIBE TABLES;
```

### Populate tables

```sql
SOURCE 'messaging_data.cql'
```

Retrieve some rows from tables:

```sql
SELECT * FROM folders_by_user;        
SELECT * FROM unread_email_stats;
SELECT * FROM emails_by_user_folder;                    
SELECT id, "to", "from" FROM emails; 
SELECT id, subject, body FROM emails; 
SELECT id, attachments FROM emails;
SELECT * FROM attachments;  
```

### Design query Q1

Find all folder labels and colors for user joe@datastax.com:

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT label, color 
    FROM folders_by_user
    WHERE username = 'joe@datastax.com';  
    ```
</details>
<br/>

### Design query Q2

Find all folder labels and unread email quantities for user joe@datastax.com:

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT label, num_unread 
    FROM unread_email_stats
    WHERE username = 'joe@datastax.com';
    ```
</details>
<br/>

### Design query Q3

Find ids, subjects, senders, read/unread statuses and timestamps of all emails with label inbox for user joe@datastax.com; order by timestamp (desc):

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT id, subject, "from", is_read, 
          toTimestamp(id) AS timestamp
    FROM emails_by_user_folder
    WHERE label = 'inbox' 
      AND username = 'joe@datastax.com';
    ```
</details>
<br/>

### Design query Q4

Find all available information about an email with id 8ae31dd0-d361-11ea-a40e-5dd6331dfc45:

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT id, "to", "from",
          toTimestamp(id) AS timestamp,
          subject, body,
          attachments
    FROM emails
    WHERE id = 8ae31dd0-d361-11ea-a40e-5dd6331dfc45;
    ```
</details>
<br/>

### Design query Q5

Find an attachment file with name Budget.xlsx for an email with id 8ae31dd0-d361-11ea-a40e-5dd6331dfc45, assuming that the complete file is stored in one partition with chunk number 1:

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT filename, type, value,
          blobAsText(value)
    FROM attachments
    WHERE email_id = 8ae31dd0-d361-11ea-a40e-5dd6331dfc45
      AND filename = 'Budget.xlsx'
      AND chunk_number = 1;
    ```
</details>
<br/>

### Design query Q6

Find an attachment file with name Presentation.pptx for an email with id 8ae31dd0-d361-11ea-a40e-5dd6331dfc45, assuming that the three file chunks are stored across three partitions with chunk numbers 1, 2 and 3:

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT filename, type, value,
          blobAsText(value)
    FROM attachments
    WHERE email_id = 8ae31dd0-d361-11ea-a40e-5dd6331dfc45
      AND filename = 'Presentation.pptx'
      AND chunk_number IN (1,2,3);
    ```
</details>
<br/>