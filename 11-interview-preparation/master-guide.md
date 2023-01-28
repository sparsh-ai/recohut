# Master Guide

Whether you’re just getting into the data engineer job market or your interview is tomorrow, practice is an essential part of the interview preparation process for a data engineer. Data engineering interview questions assess your data engineering skills and domain expertise. They are based on a company’s tech stack and technology goals, and they test your ability to perform job functions. In an interview for any Engineering role, the interviewer wants to understand if you have good analytical skills, problem-solving ability, communication, work culture and ability to build technical solutions. Specific to Data Engineering, they also want to understand if you have the skills to handle large data and build scalable and robust systems.

## The typical Data Engineering interview process

![](https://user-images.githubusercontent.com/62965911/215105782-4169e1cf-6ec6-4a6f-889b-0346be841ded.svg)

## Phone Screen

There are two types of phone screens: HR, which is generally all behavioral questions, and technical phone screens.

:::note
Behavioral questions assess soft skills (e.g., communication, leadership, adaptability), your skill level, and how you fit into the company’s data engineering team.
:::

### Round 1: HR

The HR phone screen is usually 15–30 minutes and conducted by non-technical staff at the company, such as a recruiter. You’ll be asked soft questions such as Why do you want to be a Data Engineer? Where do you see yourself in 5 years? Why do you want to work at our company? And importantly, what salary are you expecting? These questions can seem boring or odd if you don’t know the real reason for them behind the scenes: HR wants to find the right fit for their team. They want a candidate who will be communicating well with their peers and managers and stay at the company for a long time because hiring and onboarding are expensive!

They are looking for clear communication, a pleasant person to work with, someone who is enthusiastic about the company and has done their research, ideally translating into a loyal employee willing to stay and be happy at their company.

To prepare:

1. Write and practice a script for your background.
2. Do a deep dive into company values and tweak your answer accordingly.
3. Practice with your peers over the phone (we know it can be awkward).
4. Settle in a quiet place with a good Internet connection at least 10 minutes before the interview.

### Round 2: Technical

Just as the HR phone screen is a filter for basic communication ability, the technical phone screen is a filter for basic technical ability. On-site interviews are very costly in terms of time and team resources, so companies don’t want to spend hours on a candidate who can’t code well. An assessment of basic SWE knowledge and the ability to break down complicated ideas to smaller understandable pieces are the most essential reasons for technical phone screens.

Expect a 30–60 minute teleconference call answering basic DE concepts or classic SWE questions, usually from a member of the engineering team.

They are looking for people with basic knowledge in SWE and DE, problem-solving skills, and ability to communicate technical information.

Example questions include what are linked lists? How would you code them in your language of choice? Find all duplicates in a list. When would you use SQL vs. NoSQL databases?

Interviewers use easy technical questions designed to weed out candidates without the right experience. This question assesses your experience level, comfort with specific tools, and the depth of your domain expertise. Data management, SQL and Python questions are there. Data management questions include Data modeling, Data warehousing and Data pipelines. In SQL, you’ll need to know how to use window functions, aggregate functions, subqueries, joins, and sub-selects, as well as handle performance tuning and optimization. In Python, you’ll need to know how to manipulate data structures and use dictionaries, loops and lists, while showing a good understanding of strings, set operations, etc.

Technical questions can be primarily divided into these categories: SQL, Python, Data Modeling, Data Warehousing, Big Data & Cloud, Data Pipelining, Project-related and Software Engineering.

To prepare:

1. Read [Data Engineering Cookbook](https://github.com/andkret/Cookbook) and answer at least 50 questions.
2. Practice random questions from the book with your peers.
3. Do 50 easy LeetCode problems.
4. Settle in a quiet place with good Internet connection at least 10 minutes before the interview.

## Take-Home Exam

Your resume says you have many years of experience, leading multiple projects and being a rock star. How do companies know if you’re really that good? In most cases, there is no access to your old company GitHub repository, and it takes time to read and understand personal GitHub projects — not to mention they won’t know for sure that you wrote the code. A take-home coding challenge is the easiest and fastest way to assess how production-ready your code is, how you account for edge cases and exception handling, and whether you can solve a given problem in an optimal way. There are two main types of exams:

### Timed HackerRank

Expect 1.5–2 hours exam with 3–5 easy-medium HackerRank questions
including SQL, regular expressions, algorithms, and data structures

They are looking for engineers who know efficient algorithms and data structures for solving standard computer science questions, take edge cases into account, and provide the solution quickly

To prepare:

1. Solve at least 100 LeetCode/HackerRank problems
2. Practice with [Virtual Leetcode Contests](https://leetcode.com/contest/) — all free past contest that you can take any time, and try to solve problems quickly and correctly on the first try
3. Block off a chunk of time where you’ll be in a comfortable environment where you usually do technical work and make sure you won’t be interrupted and have plenty of water and snacks (if needed).

### Coding challenge

Expect 1–7 days to write code to answer 1–10 questions on 1–3 datasets, push it to your GitHub repository and submit the link.

They are looking for clean and modular code, good README with clear delivered ideas, unit tests, and exception handling.

Example question: Clean and analyze a dataset of employee salaries and locations. What is the distribution of salaries at different locations? Write a SQL query to do the equivalent task.

To prepare:

1. Read and internalize the Google style guide.
2. Practice using the unittest library in Python or equivalent.
3. Read GitHub best practices.

## On-Site Interview

You should feel very accomplished if you get to the on-site interview, but the hardest part is yet to come! On-sites can be grueling affairs of interviewing with 4–10 people in 3–6 hours, especially if you’re not prepared. Knowing what to expect and doing realistic preparation beforehand go a long way toward reducing fear and nervousness.

### Round 1: Problem Solving - SQL and Programming

You will be given a problem to solve and you need to apply **Think Out Loud** strategy to solve it. Both Python and SQL could be asked. It can also be performed on a whiteboard instead of IDE. Expect 30–45 minutes interview with 1–2 medium-hard questions to solve on the fly on a whiteboard or on IDE, constantly communicating requirements and solutions with the interviewer.

The coding interview for data engineer roles is usually lighter on the algorithm side but heavier on the data side, and the interview questions are usually more practical. For instance, write a function to transform the input data and produce the desired output data. You will still be expected to use the most optimal data structures and algorithms possible and gracefully handle all the potential data issues. Since data engineers don’t just use the built-in libraries to process data in the real world, the coding interview might also require you to implement solutions using popular open-sourced libraries, such as Spark and pandas. You are generally allowed to look up documentation during the interview if needed. If the job requires proficiency in specific frameworks, be prepared to use those frameworks in your coding interviews.

A good data engineer should be capable of translating complicated business questions into SQL queries and data models with good performance. In order to write efficient queries that process as little data as possible, you need to understand how the query engine and optimizer work. For example, sometimes using CASE statements combined with aggregation functions can replace JOIN and UNION and process much less data.

Sometimes, DSA (Data Structures and Algorithms) based questions can also be asked to check your software engineering foundations.

To prepare:

1. Solve 80–150 [LeetCode](https://leetcode.com/) and [HackerRank](https://www.hackerrank.com/) problems.
2. Get at least 20 practice sessions as an interviewee with peers or professionals.
3. Practice writing clean, readable code on a whiteboard.
4. For DSA, follow NeetCode [basic](https://neetcode.io/courses/dsa-for-beginners/0) and [advanced](https://neetcode.io/courses/advanced-algorithms/0) course.

### Round 2: Resume Discussion

You will be asked about the Python, SQL and Big Data projects you worked in. Questions will be asked mainly based on your resume. You need to apply **Don’t be fake** strategy to crack this round. You need to also prepare for the projects you add in resume because the questions around those projects will also be asked.

Your resume is not only the stepping stone to get noticed by recruiters and hiring managers, but also the most important list of projects that you should be ready to discuss in-depth with the interviewers in order to demonstrate your skills, including technical competency, problem-solving, teamwork, communication, and project management.

I strongly recommend practicing talking through your most significant data projects (to someone with an engineering background, if possible) and making sure to answer these questions in your story:

- What was the motivation for the project? (i.e. What data/business problem did your project try to solve?)
- What teams did you collaborate with? How did you work with them?
- If you were the project owner, how did you plan and drive it?
- What are the technical trade-offs made in the system design? (i.e. Why did you use framework X instead of other alternatives?)
- What were some of the technical statistics related to your project? (e.g. What is the throughput and latency of your data pipeline?)
- What was the impact of the project? (e.g. How much revenue did it generate? How many people used your application?)
- What were the challenges you had? How did you solve them?

Numbers are important in telling a great project story. Instead of just saying “it processed a lot of data…”, look up some statistics of your project and include them on your resume. Numbers will showcase the scale, impact, and your deep understanding of the project. They also make your project more believable. (In fact, interviewers might find it suspicious if you can’t even tell how much data your applications can process.)

### Round 3: System Design

As a Data Engineer, on a day to day basis you are going to design entire systems from scratch or add small features to giant existing pipelines. Even you mention these skills on your resume, it’s crucial for companies to check your ability in a real-life. System design data engineer interview questions are often the most challenging part of technical interviews. Expect 30–45 minutes interview to design a data engineering system to spec. You will be asked questions on topics related to Data modeling, warehousing, data lakes, Transformation and data pipelines. The interviewer can ask you to design a data solution from end to end, usually composed of three parts: data storage, data processing, and data modeling. Scenarios will be provided and you need to design the data pipeline/system. You need to apply **Requirement Gathering** process, **4Vs of Big Data** framework and include the **Fault tolerance + Scalability** factors in your system design to crack this round.

The initial interview question is often very short and abstract (e.g. design a data warehouse from end to end) and it’s your job to ask follow-up questions to pin down the requirements and use cases, just like solving a real-life data problem.

In a system design interview, you will design a data solution from end to end, which is usually composed of three parts: data storage, data processing, and data modeling. You have to choose the best combination of data storage systems and data processing frameworks based on the requirements, and sometimes there is more than one optimal solution.

Example questions: Design Twitter — what are the system blocks needed? What database and schema would you use? What about caching and load balancing? What are the tradeoffs of a system? They are looking for your ability to clearly communicate and scope down requirements, design a concept-level pipeline, and knowledge of distributed systems basics.

Data modeling is usually the end piece of a system design interview but sometimes it is a part of the SQL interview instead. One example of a data modeling interview question is to design the backend analytical tables for a reservation system for vet clinics. The most important principle in data modeling is to design your data models based on use cases and query patterns. Again, it is your responsibility to get clarifications on the requirements and use cases so that you can make better design choices.

To prepare:

1. Read Data Engineering Cookbook, the Data Engineering Ecosystem and Grokking the System Design Interview.
2. Follow NeetCode [course](https://neetcode.io/courses/system-design-for-beginners/0) and [Interviews](https://neetcode.io/courses/system-design-interview/0)
2. Practice at least 10 different questions on a whiteboard with peers or mentors.
3. Practice drawing clean, readable systems diagrams on the whiteboard.

### Round 4: Cultural Fit

It’s very important to be technically strong and knowledgeable, but it’s not enough! If you can’t deliver your brilliant ideas, then no one else can understand and use them. Behavioral types of interviews, such as cultural fit, are meant to show how you can tell your story and explain how you’ve handled tough workplace situations.

Interviews are not exams where you just need the right answers to pass, but rather a series of conversations to see if you can learn quickly and work with a team to solve problems together. Therefore, it is very important to be human and be yourself during interviews.

Expect a 30–45 minutes interview with 2–4 questions about your past situations.

They are looking for consistent and complete answers using the STAR (situation, task, action, result) method.

Example questions include tell us about a time at work where you had a big deadline. Tell us about a time when you had a conflict with another team member. How did you handle these situations?

Interviewers will put Random and hypothetical situations in front of you and check your positive mindset and how you are going to approach that particular problem. You need to follow **Recall your Past Experiences** to crack this round.

To prepare:

1. Practice at least 30 cultural fit interview questions alone, writing scripts and recording yourself if needed.
2. Practice at least 10 questions with peers, following the STAR method.
3. Be nice. Nobody wants to work with jerks.
4. Have conversations. The best interviews are usually like conversations. Ask questions if you want information or feedback.
5. Problem-solving, not answers. Just like in real life, you don’t always know the right answer to a problem immediately. It’s more important to show how you would approach the problem instead of only giving an answer.
6. Show your passion for data engineering. What do you do outside your work responsibility to be a better data engineer?

While the interviewers are interviewing you, you are also interviewing them. Would you enjoy working with them? Would this team provide opportunities for you to grow? Do you agree with the manager’s view and managing style? Finding a good team is hard so ask your questions wisely.

:::tip
Interviewing is very stressful. It is an imperfect process where strangers judge your professional competency only based on one hour of interactions with you and sometimes the interview result is not fair. It is frustrating when you just can’t get any further on interview questions and you feel like the interviewers are looking down at you. Getting rejected over and over again can be devastating to your self-esteem and you may start to think you’re not good enough. I have been there too: never hearing back from most job applications and failing all the coding interviews I could get. I thought I would never be an engineer. But I am glad I didn’t give up.

If you are feeling overwhelmed, frustrated, or hopeless because of interviews, I want to let you know that you are not alone. If you get rejected for a job, it is their loss. Be patient with yourself and stay hopeful, because things will get better and your just need to keep trying! Always show up to your interviews with confidence, because you are good enough!
:::

## SQL Questions

#### What does the COALESCE function do?

#### What is the difference between WHERE and HAVING? Example of where one should use one over the other?

#### What are top RDBMS engines?

#### How is an RDBMS different from a NoSQL database?

#### What do DDL, DCL and DML stand for? Give examples of commands for each

#### What are common data types in SQL?

#### What are attribute constraints, and explain them?

#### What is the difference between inner join and left outer join?

#### What is the difference between UNION and UNION ALL?

#### When should one use a CTE over a subquery?

#### What are window functions?

## Python Questions

#### Write a function to sort an array so it produces only odd numbers.

#### Write a function to find non duplicate numbers in the first list and preserve the order of the list: [1,1,3,2,5,6,5] --> [1,3,2,5,6]

#### Given a list, return the numbers which have maximum count.

#### Given a json object with nested objects, write a function that flattens all the objects to a single key value dictionary.

#### Write code to find the sum of any two numbers in a given array that could be equal to x.

#### Write code to find the maximum number of combinations of infinite coins of {1,2,5} that can add up to make 20 rupees.

#### How do you implement a stack using a linked list?

#### What is your experience with X skill on Python?

General experience questions like this are jump-off points for more technical case studies. And typically, The interviewer will tailor questions as they pertain to the role. However, you should be comfortable with standard Python and supplemental libraries like Matplotlib, Pandas, and NumPy, know what’s available, and understand when it’s appropriate to use each library.

One note: Don’t fake it. If you don’t have much experience, be honest. You can also describe a related skill or talk about your comfort level in quickly picking up new Python skills (with an example).

## Data Modeling Questions

#### How do you create a schema that would keep track of a customer address where the address changes?

#### Design a data model in order to track product from the vendor to the Amazon warehouse to delivery to the customer.

#### Design a data model for a retail store.

#### Create the required tables for an online store: define the necessary relations, identify primary and foreign keys, etc.

#### How do you manage a table with a large number of updates, while maintaining the availability of the table for a large number of users?

#### Should we apply normalization rules on a star schema?

#### What's a chasm trap?

#### What is CAP theorem?

#### What is Data Modeling and Why you should care?

#### What are the advantages of Data Modeling?

#### What is Conceptual Data Model?

#### What is Logical Data Model?

#### What is Physical Data Model?

#### What is Entity-Relation (ER) Model?

#### What is Star Schema?

#### What are the differences between Star Schema and Snowflake Schema?

“Star schema is a type of data warehouse schema that is optimized for query performance. The snowflake schema is a type of data warehouse schema that is normalized for storage efficiency.”

#### Explain the Relational Data Modeling with an example

#### Explain the Non-Relational Data Modeling with an example

#### Explain the Kimball's Four Step Process to Dimensional Data Modeling

#### What is Inmon Data Modeling Approach?

#### What are the differences between Kimball and Inmon Data Modeling Approach?

#### What is the difference between Fact and Dimension Tables?

#### What are Slowly Changing Dimensions (SCDs)?

#### Explain Different Types of Slowly Changing Dimensions (SCDs)

#### What is Data Normalization?

#### What is Data Denormalization?

#### What are the Pros and Cons of Data Normalization?

#### What are the Pros and Cons of Data Denormalization?

#### What is the difference among 1NF, 2NF and 3NF?

#### What are the different categories of NoSQL Databases?

#### What are the ACID properties and where these are applied?

#### What are the BASE properties and where these are applied?

#### What are the differences between SQL and NoSQL data modeling?

#### Describe a time you had difficulty merging data. How did you solve this issue?

#### Describe a time you had difficulty merging data. How did you solve this issue?

Data cleaning and data processing are key job responsibilities in engineering roles. Inevitably unexpected issues will come up. Interviewers ask questions like these to determine:

- How well do you adapt?
- The depth of your experience.
- Your technical problem-solving ability.
- Clearly explain the issue, what you proposed, the steps you took to solve the problem, and the outcome.

#### What are the design schemas of data modeling?

#### What’s the difference between structured and unstructured data?

With a fundamental question like this, be prepared to answer with a quick definition and then provide an example.

You could say: “Structured data consists of clearly defined data types and easily searchable information. An example would be customer purchase information stored in a relational database. Unstructured data, on the other hand, does not have a clearly defined format, and therefore, a relational database can’t store it in a relational database. An example would be video or image files.”

## Data Warehousing Questions

#### Give a schema for a data warehouse.

#### Design a data warehouse to capture sales.

#### Design a data warehouse to help a customer support team manage tickets.

#### Can you design a simple OLTP architecture that will convince the Redbus team to give X project to you?

#### What is Data Warehouse?

#### Why is Data Warehouse needed?

#### What are the differences between Databases and Data Warehouses?

#### What are the differences between Operational and Analytical Systems?

#### What is Data Mart?

#### What is the Main Difference between View and Materialized View?

#### What is OLTP?

#### What is OLAP?

#### What are the differences between OLTP and OLAP?

#### What are the Pros and Cons of OLTP?

#### What are the Pros and Cons of OLAP?

#### What is the difference between a data warehouse and an operational database?

If you took a database course in college, then you probably learned about how to set up a standard normalized database. This style of database is optimized for transactions that involve Insert, Update, and Delete SQL statements. These are standard operational databases. They need to focus on making transactions quickly without getting bogged down by calculations and data manipulations. Thus, their design is a little more cumbersome for an analysis. Generally, you will have to join several tables just to get a single data point.

A data warehouse is not concerned as much with dealing with millions of fast transactions every second. Instead, a data warehouse is usually built to support a data analytics product and analysis. This means performance is not geared towards transactions — instead, it’s aimed at aggregations, calculations, and select statements. A data warehouse will have a slightly denormalized structure compared to an operational database. In most data warehouses, a majority of tables will take on two different attributes: a historical transaction table and tables that contain categorical style data. We reference these as fact and dimension tables.

The fact table is essentially in the center, unlike in a normalized database where you might have to join across several tables to get one data point. A standard data warehouse usually has a focus on the fact tables, and all the dimension tables join to provide categorical information to the fact table. It’s also typically bad practice to join fact table to the fact table, but sometimes it can occur if the data is created correctly.

These are not the only tables that exist in a data warehouse. There are aggregate tables, snapshots, partitions, and more. The goal is usually a report or dashboard that can be automatically updated quickly.

#### How would you design a data warehouse given X criteria?

This example is a fundamental case study question in data engineering, and it requires you to provide a high-level design for a database based on criteria. To answer questions like this:

- Start with clarifying questions and state your assumptions
- Provide a hypothesis or high-level overview of your design
- Then describe how your design would work

## Big Data & Cloud Questions

#### What are big data’s four Vs?

#### What are the key features of Hadoop?

Some of the Hadoop features you might talk about in a data engineering interview include:

- Fault tolerance
- Distributed processing
- Scalability
- Reliability

#### What are the key features of PySpark?

#### How PySpark is different from Python?

#### What ETL tools do you have experience using? What tools do you prefer?

There are many variations to this type of question. A different version would be about a specific ETL tool, “Have you had experienced with Apache Spark or Amazon Redshift?” If a tool is in the job description, it might come up in a question like this. One tip: Include any training, how long you’ve used the tech, and specific tasks you can perform.

#### What experience do you have with cloud technologies?

If cloud technology is in the job description, chances are it will show up in the interview. Some of the most common cloud technologies for data engineer interviews include Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform, and IBM Cloud. Additionally, be prepared to discuss specific tools for each platform, like AWS Glue, EMR, and AWS Athena.

#### What are some challenges unique to cloud computing?

A broad question like this can quickly assess your experience with cloud technologies in data engineering. Some of the challenges you should be prepared to talk about include:

- Security and Compliance
- Cost
- Governance and control
- Performance

## Data Pipelining Questions

#### Given scenario A, how would you design the pipeline for ingesting this data?

#### Given a schema, create a script from scratch for an ETL to provide certain data, writing a function for each step of the process.

#### How would you build a data pipeline around an AWS product, which is able to handle increasing data volume?

#### Which tools you would use to build data pipelines in cloud?

#### How would you design a data pipeline?

A broad, beginner case study question like this wants to know how you approach a problem. With all case study questions, you should ask clarifying questions like:

- What type of data is processed?
- How will the information be used?
- What are the requirements for the project?
- How much will data be pulled? How frequently?

These questions will provide insights into the type of response the interviewer seeks. Then, you can describe your design process, starting with choosing data sources and data ingestion strategies, before moving into your developing data processing and implementation plans.

#### Tell me About a Time You Had Performance Issues With an ETL and How Did You Fix It?

As a data engineer, you will run into performance issues. Either you developed an ETL when the data was smaller and it didn’t scale, or you’re maintaining older architecture that is not scaling. ETLs feature multiple components, multiple table inserts, merges, and updates. This makes it difficult to tell exactly where the ETL issue is occurring. The first step is identifying the problem, so you need to figure out where the bottleneck is occurring.

Hopefully, whoever set up your ETL has an ETL log table somewhere that tracks when components finish. This makes it easy to spot bottlenecks and the biggest time sucks. If not, it will not be easy to find the issue. Depending on the urgency of the issue, we would recommend setting up an ETL log table and then rerunning to identify the issue. If the fix is needed right away, then you will probably just have to go piece-by-piece through the ETL to try to track down the long-running component. This also depends on how long the ETL takes to run. There are ways you can approach that as well depending on what the component relies on.

Issues can vary wildly, and they can include table locks, slow transactions, loops getting stuck, and etc. Once you have identified the issue, then you need to figure out a fix. This depends on the problem, but the solutions could require adding an index, removing an index, partitioning tables, and batching the data in smaller pieces (or sometimes even larger pieces — it seems counterintuitive, but this would depend on table scans and indexes). Depending on the storage system you are using, it’s good to look into the activity monitor to see what is happening on an I/O level. This will give you a better idea of the problem.

When you look at the activity monitor, you can see if there is any data being processed at all. Is there too much data being processed, none, or table locks? Any of these issues can choke an ETL and would need to be addressed.

If you Google some of the performance issues, then you will find some people blaming the architecture for a lot of the problems. We don’t disagree with them. However, this doesn’t mean you should throw in the towel. There are always various ways to manage performance if you can’t touch the actual structure. Even beyond indexes, there are some parallel processing methods that can be used to speed up the ETL. You can also add temporary support tables to lighten the load.

#### **How Would You Approach Developing a New Analytical Product as a Data Engineer?**

As a data engineer, you control what is possible in the final product. A data scientist can’t build algorithms or metrics without having the right data and the data at the right granularity.

This means a data engineer needs to understand the entire product. A data engineer can’t just get away with building systems based off of requirements. They need to ask why they are building certain tables and objects.

It’s helpful if the stakeholders already have a general outline of what they want. If they don’t have an outline, we would want to work with them to develop a general idea of what metrics and algorithms will exist. This drives all the major decisions, including what data should be pulled, how long should it be stored, if should it be archived, and etc.

Once a general outline exists, the next step would be drilling into the why of each metric. This is because as you’re building different tables at different data granularities, certain issues might arise. Should the unique key be on columns A and B, or A, B, and C. Well, that depends, why is this important? What does that row signify? Is it customer level, store level, or maybe brand level?

Once your team has gone through the process of working on the outline with your stakeholders and gained an understanding of the why, the next step is to think through as many operational scenarios as possible.

Will you ever need to reload data? Do your ETLs allow for it? Is it efficient? What happens when X occurs? How do you handle case Y?

You can’t spend all day doing this, but trying to think of all the issues that could occur will help you develop a more robust system. It also helps create a system that actually meets requirements.

From there, it’s about developing the design, creating test cases, and testing the tables, stored procedures, and scripts, and then pushing to production. How that occurs usually changes from team to team.

## Project-related Questions

#### Walk me through a project you worked on from start to finish

#### What algorithm(s) did you use on the project?

#### What tools did you use on the project?

## Software Engineering Questions

#### Describe a situation where you used git

#### How you version control your codebase

#### What is your experience with Bash shell?

#### What is agile methodology

## Airflow

#### What is Airflow?
Apache Airflow is an open-source workflow management platform. It began in October 2014 at Airbnb as a solution for managing the company's increasingly complex workflows. Airbnb's creation of Airflow enabled them to programmatically author, schedule, and monitor their workflows via the built-in Airflow user interface. Airflow is a data transformation pipeline ETL (Extract, Transform, Load) workflow orchestration tool.

#### What issues does Airflow resolve?
Crons are an old technique of task scheduling.
Scalable
Cron requires external assistance to log, track, and manage tasks. The Airflow UI is used to track and monitor the workflow's execution.
Creating and maintaining a relationship between tasks in cron is a challenge, whereas it is as simple as writing Python code in Airflow.
Cron jobs are not reproducible until they are configured externally. Airflow maintains an audit trail of all tasks completed.

#### Explain how workflow is designed in Airflow?
A directed acyclic graph (DAG) is used to design an Airflow workflow. That is to say, when creating a workflow, consider how it can be divided into tasks that can be completed independently. The tasks can then be combined into a graph to form a logical whole.
The overall logic of your workflow is based on the shape of the graph. An Airflow DAG can have multiple branches, and you can choose which ones to follow and which to skip during workflow execution.
Airflow Pipeline DAG
Airflow could be completely stopped, and able to run workflows would then resume through restarting the last unfinished task.
It is important to remember that airflow operators can be run more than once when designing airflow operators. Each task should be idempotent, or capable of being performed multiple times without causing unintended consequences.

#### Explain Airflow Architecture and its components?
There are four major components to airflow.
+ Webserver
    + This is the Airflow UI built on the Flask, which provides an overview of the overall health of various DAGs and helps visualise various components and states of every DAG. For the Airflow setup, the Web Server also allows you to manage users, roles, and different configurations.
+ Scheduler
    + Every n seconds, the scheduler walks over the DAGs and schedules the task to be executed.Executor
+ Executor is another internal component of the scheduler.
    + The executors are the components that actually execute the tasks, while the Scheduler orchestrates them. Airflow has different types of executors, including SequentialExecutor, LocalExecutor, CeleryExecutor and KubernetesExecutor. People generally choose the executor which is best for their use case.
+ Worker
    + Workers are responsible to run the task that the executor has given them.
+ Metadata Database
Airflow supports a wide range of metadata storage databases. This database contains information about DAGs, their runs, and other Airflow configurations such as users, roles, and connections.
The DAGs' states and runs are shown by the Web Server from the database. This information is also updated in the metadata database by the Scheduler.

#### What are the types of Executors in Airflow?
The executors are the components that actually execute the tasks, while the Scheduler orchestrates them. Airflow has different types of executors, including SequentialExecutor, LocalExecutor, CeleryExecutor and KubernetesExecutor. People generally choose the executor which is best for their use case.
Types of Executor
+ SequentialExecutor
    + Only one task is executed at a time by SequentialExecutor. The scheduler and the workers both use the same machine.
+ LocalExecutor
    + LocalExecutor is the same as the Sequential Executor, except it can run multiple tasks at a time.
+ CeleryExecutor
    + Celery is a Python framework for running distributed asynchronous tasks.
As a result, CeleryExecutor has long been a part of Airflow, even before Kubernetes.
CeleryExecutors has a fixed number of workers on standby to take on tasks when they become available.
+ KubernetesExecutor
    + Each task is run by KubernetesExecutor in its own Kubernetes pod. It, unlike Celery, spins up worker pods on demand, allowing for the most efficient use of resources.

#### What are the pros and cons of SequentialExecutor?
Pros:
+ It's simple and straightforward to set up.
+ It's a good way to test DAGs while they're being developed.
Pros:
It isn't scalable.
It is not possible to perform many tasks at the same time.
Unsuitable for use in production

#### What are the pros and cons of LocalExecutor?
Pros:
+ Able to perform multiple tasks.
+ Can be used to run DAGs during development.
Cons:
+ The product isn't scalable.
+ There is only one point of failure.
+ Unsuitable for use in production.

#### What are the pros and cons of CeleryExecutor?
Pros:
+ It allows for scalability.
+ Celery is responsible for managing the workers. Celery creates a new one in the case of a failure.
Cons:
+ Celery requires RabbitMQ/Redis for task queuing, which is redundant with what Airflow already supports.
+ The setup is also complicated due to the above-mentioned dependencies.

#### What are the pros and cons of KubernetesExecutor?
Pros:
It combines the benefits of CeleryExecutor and LocalExecutor in terms of scalability and simplicity.
Fine-grained control over task-allocation resources. At the task level, the amount of CPU/memory needed can be configured.
Cons:
Airflow is newer to Kubernetes, and the documentation is complicated.

#### How to define a workflow in Airflow?
Python files are used to define workflows.
DAG (Directed Acyclic Graph)
The DAG Python class in Airflow allows you to generate a Directed Acyclic Graph, which is a representation of the workflow.
from Airflow.models import DAG
from airflow.utils.dates import days_ago
​
args = {
'start_date': days_ago(0),
}
​
dag = DAG(
dag_id='bash_operator_example',
default_args=args,
schedule_interval='* * * * *',
)
You can use the start date to launch a task on a specific date.
The schedule interval specifies how often each workflow is scheduled to run. '* * * * *' indicates that the tasks must run every minute.


#### How do you make the module available to airflow if you're using Docker Compose?
If we are using Docker Compose, then we will need to use a custom image with our own additional dependencies in order to make the module available to Airflow. Refer to the following Airflow Documentation for reasons why we need it and how to do it.

#### How to schedule DAG in Airflow?
DAGs could be scheduled by passing a timedelta or a cron expression (or one of the @ presets), which works well enough for DAGs that need to run on a regular basis, but there are many more use cases that are presently difficult to express "natively" in Airflow, or that require some complicated workarounds. You can refer Airflow Improvements Proposals (AIP).
Simply use the following command to start a scheduler:
+ airflow scheduler

#### What is XComs In Airflow?
XCom (short for cross-communication) are messages that allow data to be sent between tasks. The key, value, timestamp, and task/DAG id are all defined.

#### What is xcom_pull in XCom Airflow?
The xcom push and xcom pull methods on Task Instances are used to explicitly "push" and "pull" XComs to and from their storage. Whereas if do xcom push parameter is set to True (as it is by default), many operators and @task functions will auto-push their results into an XCom key named return value.
If no key is supplied to xcom pull, it will use this key by default, allowing you to write code like this:
 Pulls the return_value XCOM from "pushing_task"
value = task_instance.xcom_pull(task_ids='pushing_task')

#### What is Jinja templates?
Jinja is a templating engine that is quick, expressive, and extendable. The template has special placeholders that allow you to write code that looks like Python syntax. After that, data is passed to the template in order to render the final document.

#### How to use Airflow XComs in Jinja templates?
We can use XComs in Jinja templates as given below:
+ SELECT * FROM {{ task_instance.xcom_pull(task_ids='foo', key='table_name') }}

## AWS

#### What is EC2?
EC2, a Virtual Machine in the cloud on which you have OS-level control. You can run this cloud server whenever you want and can be used when you need to deploy your own servers in the cloud, similar to your on-premises servers, and when you want to have full control over the choice of hardware and the updates on the machine.

#### What is SnowBall?
SnowBall is a small application that enables you to transfer terabytes of data inside and outside of the AWS environment.

#### What is CloudWatch?
CloudWatch helps you to monitor AWS environments like EC2, RDS Instances, and CPU utilization. It also triggers alarms depending on various metrics.

#### What is Elastic Transcoder?
Elastic Transcoder is an AWS Service Tool that helps you in changing a video’s format and resolution to support various devices like tablets, smartphones, and laptops of different resolutions.

#### What do you understand by VPC?
VPC stands for Virtual Private Cloud. It allows you to customize your networking configuration. VPC is a network that is logically isolated from other networks in the cloud. It allows you to have your private IP Address range, internet gateways, subnets, and security groups.

#### DNS and Load Balancer Services come under which type of Cloud Service?
DNS and Load Balancer are a part of IaaS-Storage Cloud Service.

#### What are the Storage Classes available in Amazon S3?
Storage Classes available with Amazon S3 are:
+ Amazon S3 Standard
+ Amazon S3 Standard-Infrequent Access
+ Amazon S3 Reduced Redundancy Storage
+ Amazon Glacier

#### Explain what T2 instances are?
T2 Instances are designed to provide moderate baseline performance and the capability to burst to higher performance as required by the workload.

#### What are Key-Pairs in AWS?
Key-Pairs are secure login information for your Virtual Machines. To connect to the instances, you can use Key-Pairs which contain a Public Key and a Private Key.

#### How many Subnets can you have per VPC?
You can have 200 Subnets per VPC.

#### List different types of Cloud Services.
Different types of Cloud Services are:
+ Software as a Service (SaaS)
+ Data as a Service (DaaS)
+ Platform as a Service (PaaS)
+ Infrastructure as a Service (IaaS)

#### Explain what S3 is?
S3 stands for Simple Storage Service. You can use the S3 interface to store and retrieve any amount of data, at any time and from anywhere on the web. For S3, the payment model is “pay as you go”.

#### How does Amazon Route 53 provide high availability and low latency?
Amazon Route 53 uses the following to provide high availability and low latency:
+ Globally Distributed Servers - Amazon is a global service and consequently has DNS Servers globally. Any customer creating a query from any part of the world gets to reach a DNS Server local to them that provides low latency.
+ Dependency - Route 53 provides a high level of dependability required by critical applications.
+ Optimal Locations - Route 53 serves the requests from the nearest data center to the client sending the request. AWS has data-centers across the world. The data can be cached on different data-centers located in different regions of the world depending on the requirements and the configuration chosen. Route 53 enables any server in any data-center which has the required data to respond. This way, it enables the nearest server to serve the client request, thus reducing the time taken to serve.

#### How can you send a request to Amazon S3?
Amazon S3 is a REST Service, and you can send a request by using the REST API or the AWS SDK wrapper libraries that wrap the underlying Amazon S3 REST API.

#### What does AMI include?
An AMI includes the following things:
+ A template for the root volume for the instance.
+ Launch permissions to decide which AWS accounts can avail the AMI to launch instances.
+ A block device mapping that determines the volumes to attach to the instance when it is launched.

#### What are the different types of Instances?
+ Following are the types of instances:
+ Compute Optimized
+ Memory-Optimized
+ Storage Optimized
+ Accelerated Computing

#### What is the relation between the Availability Zone and Region?
An AWS Availability Zone is a physical location where an Amazon data center is located. On the other hand, an AWS Region is a collection or group of Availability Zones or Data Centers.
This setup helps your services to be more available as you can place your VMs in different data centers within an AWS Region. If one of the data centers fails in a Region, the client requests still get served from the other data centers located in the same Region. This arrangement, thus, helps your service to be available even if a Data Center goes down.

#### How do you monitor Amazon VPC?
You can monitor Amazon VPC using:
+ CloudWatch
+ VPC Flow Logs

#### What are the different types of EC2 instances based on their costs?
The three types of EC2 instances based on the costs are:
+ On-Demand Instance - These instances are prepared as and when needed. Whenever you feel the need for a new EC2 instance, you can go ahead and create an on-demand instance. It is cheap for the short-time but not when taken for the long term.
+ Spot Instance - These types of instances can be bought through the bidding model. These are comparatively cheaper than On-Demand Instances.
+ Reserved Instance - On AWS, you can create instances that you can reserve for a year or so. These types of instances are especially useful when you know in advance that you will be needing an instance for the long term. In such cases, you can create a reserved instance and save heavily on costs.

#### What do you understand by stopping and terminating an EC2 Instance?
Stopping an EC2 instance means to shut it down as you would normally do on your Personal Computer. This will not delete any volumes attached to the instance and the instance can be started again when needed.
On the other hand, terminating an instance is equivalent to deleting an instance. All the volumes attached to the instance get deleted and it is not possible to restart the instance if needed at a later point in time.

#### What are the consistency models for modern DBs offered by AWS?
Eventual Consistency - It means that the data will be consistent eventually, but may not be immediate. This will serve the client requests faster, but chances are that some of the initial read requests may read the stale data. This type of consistency is preferred in systems where data need not be real-time. For example, if you don’t see the recent tweets on Twitter or recent posts on Facebook for a couple of seconds, it is acceptable.
Strong Consistency - It provides an immediate consistency where the data will be consistent across all the DB Servers immediately. Accordingly. This model may take some time to make the data consistent and subsequently start serving the requests again. However, in this model, it is guaranteed that all the responses will always have consistent data.

#### What is Geo-Targeting in CloudFront?
Geo-Targeting enables the creation of customized content based on the geographic location of the user. This allows you to serve the content which is more relevant to a user. For example, using Geo-Targeting, you can show the news related to local body elections to a user sitting in India, which you may not want to show to a user sitting in the US. Similarly, the news related to Baseball Tournament can be more relevant to a user sitting in the US, and not so relevant for a user sitting in India.

#### What are the advantages of AWS IAM?
AWS IAM enables an administrator to provide granular level access to different users and groups. Different users and user groups may need different levels of access to different resources created. With IAM, you can create roles with specific access-levels and assign the roles to the users.
It also allows you to provide access to the resources to users and applications without creating the IAM Roles, which is known as Federated Access.

#### What do you understand by a Security Group?
When you create an instance in AWS, you may or may not want that instance to be accessible from the public network. Moreover, you may want that instance to be accessible from some networks and not from others.
Security Groups are a type of rule-based Virtual Firewall using which you can control access to your instances. You can create rules defining the Port Numbers, Networks, or protocols from which you want to allow access or deny access.

#### What are Spot Instances and On-Demand Instances?
When AWS creates EC2 instances, there are some blocks of computing capacity and processing power left unused. AWS releases these blocks as Spot Instances. Spot Instances run whenever capacity is available. These are a good option if you are flexible about when your applications can run and if your applications can be interrupted.
On the other hand, On-Demand Instances can be created as and when needed. The prices of such instances are static. Such instances will always be available unless you explicitly terminate them.

#### Explain Connection Draining.
Connection Draining is a feature provided by AWS which enables your servers which are either going to be updated or removed, to serve the current requests.
If Connection Draining is enabled, the Load Balancer will allow an outgoing instance to complete the current requests for a specific period but will not send any new request to it. Without Connection Draining, an outgoing instance will immediately go off and the requests pending on that instance will error out.

#### What is a Stateful and a Stateless Firewall?
A Stateful Firewall is the one that maintains the state of the rules defined. It requires you to define only inbound rules. Based on the inbound rules defined, it automatically allows the outbound traffic to flow.
On the other hand, a Stateless Firewall requires you to explicitly define rules for inbound as well as outbound traffic.
For example, if you allow inbound traffic from Port 80, a Stateful Firewall will allow outbound traffic to Port 80, but a Stateless Firewall will not do so.

#### What is a Power User Access in AWS?
An Administrator User will be similar to the owner of the AWS Resources. He can create, delete, modify or view the resources and also grant permissions to other users for the AWS Resources.
A Power User Access provides Administrator Access without the capability to manage the users and permissions. In other words, a user with Power User Access can create, delete, modify or see the resources, but he cannot grant permissions to other users.

#### What is an Instance Store Volume and an EBS Volume?
An Instance Store Volume is temporary storage that is used to store the temporary data required by an instance to function. The data is available as long as the instance is running. As soon as the instance is turned off, the Instance Store Volume gets removed and the data gets deleted.
On the other hand, an EBS Volume represents a persistent storage disk. The data stored in an EBS Volume will be available even after the instance is turned off.

#### What are Recovery Time Objective and Recovery Point Objective in AWS?
Recovery Time Objective - It is the maximum acceptable delay between the interruption of service and restoration of service. This translates to an acceptable time window when the service can be unavailable.
Recover Point Objective - It is the maximum acceptable amount of time since the last data restore point. It translates to the acceptable amount of data loss which lies between the last recovery point and the interruption of service.

#### Is there a way to upload a file that is greater than 100 Megabytes in Amazon S3?
Yes, it is possible by using the Multipart Upload Utility from AWS. With the Multipart Upload Utility, larger files can be uploaded in multiple parts that are uploaded independently. You can also decrease upload time by uploading these parts in parallel. After the upload is done, the parts are merged into a single object or file to create the original file from which the parts were created.

#### Can you change the Private IP Address of an EC2 instance while it is running or in a stopped state?
No, a Private IP Address of an EC2 instance cannot be changed. When an EC2 instance is launched, a private IP Address is assigned to that instance at the boot time. This private IP Address is attached to the instance for its entire lifetime and can never be changed.

#### What is the use of lifecycle hooks is Autoscaling?
Lifecycle hooks are used for Auto-scaling to put an additional wait time to a scale-in or a scale-out event.

#### What are the policies that you can set for your user’s passwords?
Following are the policies that can be set for user’s passwords:
+ You can set a minimum length of the password.
+ You can ask the users to add at least one number or special character to the password.
+ Assigning the requirements of particular character types, including uppercase letters, lowercase letters, numbers, and non-alphanumeric characters.
+ You can enforce automatic password expiration, prevent the reuse of old passwords, and request for a password reset upon their next AWS sign-in.
+ You can have the AWS users contact an account administrator when the user has allowed the password to expire.

#### What do tou know about the Amazon Database?
Amazon database is one of the Amazon Web Services that offers managed database along with managed service and NoSQL. It is also a fully managed petabyte-scale data warehouse service and in-memory caching as a service. There are four AWS database services, the user can choose to use one or multiple that meet the requirements. Amazon database services are – DynamoDB, RDS, RedShift, and Elastic ache.

#### Explain Amazon Relational Database?
Amazon relational database is a service that helps users with a number of services such as operation, lining up, and scaling an on-line database within the cloud. It automates the admin tasks such as info setup, hardware provisioning, backups, and mending. Amazon relational database provides users with resizable and cost-effective capability. By automating the tasks, it saves time and thus let user concentrate on the applications and provide them high availableness, quick performance, compatibility, and security.
There are a number of AWS RDS engines, such as:
+ Mysql
+ Oracle
+ PostgreSQL
+ SQL Server
+ MariaDB
+ Amazon Aurora

#### What are the Features of Amazon Database?
Following are the important features of Amazon Database:
+ Easy to administer
+ Highly scalable
+ Durable and reliable
+ Faster performance
+ Highly available
+ More secure
+ Cost-effective

#### Which of the Aws Db Service is a Nosql Database and Serverless and Delivers Consistent singledigit Millisecond Latency at any scale?
Amazon DynamoDB.

#### What is  Key Value Store?
Key-value store is a database service which facilitates the storing, updating, and querying of the objects which are generally identified with the key and values. These objects consist of the keys and values which constitutes the actual content that is stored.

#### What is Dynamodb?
DynamoDB is a NoSQL database service that provides an inevitable and faster performance. DynamoDB is superintendent and offers a high level of scalability. DynamoDB makes users not to worry about the configuration, setup, hardware provisioning, throughput capacity, replication, software patching or cluster scaling. It helps users in offloading the scaling and operating distributed databases to AWS.

#### List of the benefits of using Amazon Dynamodb?
Amazon DynamoDB is the NoSQL service that provides a number of benefits to the users.
Some benefits of AWS DynamoDB are:
+ Being a self-managed service, DynamoDB doesn’t require the experts for setup, installation, cluster etc.
+ It provides inevitable and faster performance.
+ It is highly scalable, available, and durable.
+ It provides very high throughput at the low latency.
+ It is highly cost-effective.
+ It supports and allows the creation of dynamic tables with multi-values attributes i.e. it’s flexible in nature.

#### What is a Dynamodbmapper Class?
The mapper class is the entry point of the DynamoDB. It allows users to enter the DynamoDB and access the endpoint. DynamoDB mapper class helps users access the data stored in various tables, then execute queries, scan them against the tables, and perform CRUD operations on the data items.

#### What are the Data Types supported by Dynamodb?
DynamoDB supports different types of data types such as collection data types, scalar data types, and even null values.
Scalar Data Types – The scalar data types supported by DynamoDB are:
+ Binary
+ Number
+ Boolean
+ String

Collection Data Types – The collection data types supported by DynamoDB are:
+ Binary Set
+ Number Set
+ String Set
+ Heterogeneous Map
+ Heterogeneous List

####  What do you understand by Dynamodb Auto Scaling?
DynamoDB Auto scaling specifies its specialized feature to automatically scale up and down its own read and write capacity or global secondary index.

#### What is a Data Warehouse and how Aws Redshift can play a vital role in the Storage?
A data warehouse can be thought of a repository where the data generated from the company’s systems and other sources is collected and stored. So a data warehouse has three-tier architecture:
In the bottom tier, we have the tools which cleanse and collect the data.
In the middle tier, we have tools which transform the data using Online Analytical Processing Server.
In the top tier, we have different tools where data analysis and data mining is performed at the front end.
Setting up and managing a data warehouse involves a lot of money as the data in an organization continuously increases and the organization has to continuously upgrade their data storage servers. So here AWS RedShift comes into existence where the companies store their data in the cloud-based warehouses provided by Amazon.

#### What is Amazon Redshift and why is it popular among other Cloud Data Warehouses?
Amazon RedShift is a fast and scalable data warehouse which is easy to use and is cost-effective to manage all the organization’s data. The database is ranged from gigabytes to 100’s of petabyte of cloud data storage. A person does not need knowledge of any programming language to use this feature, just upload the cluster and tools which are already known to the user he can start using RedShift.
AWS RedShift is popular due to the following reasons:
+ AWS RedShift is very easy to use: In the console of AWS RedShift, you will find an option of creating a cluster. Just click on that and leave the rest on the machine programming of RedShift. Just fill the correct details as asked and launch the cluster. Now the cluster is ready to be used as RedShift automated most of the task like managing, monitoring and scaling.
+ Scaling of Warehouse is very easy: You just have to resize the cluster size by increasing the number of compute nodes.
+ RedShift gives 10x times better and fast performance: It makes use of specific strategies like columnar storage and massive parallel processing strategies to deliver high throughput and response time.
+ Economical: As it does not require any setup so cost reduces down to 1/10th of the traditional data warehouse.

#### What is Redshift Spectrum?
The RedShift Spectrum allows you to run queries alongside petabyte of data which is unstructured and that too with no requirement of loading ETL. Spectrum scales millions of queries and allows you to allocate and store the data wherever you want and whatever the type of format is suitable for you.

#### What is a Leader Node and Compute Node?
In a leader node the queries from the client application are received and then the queries are parsed and the execution plan is developed. The steps to process these queries are developed and the result is sent back to the client application.
In a compute node the steps assigned in the leader node are executed and the data is transmitted. The result is then sent back to the leader node before sending it to the client application.

#### How to load data iIn Amazon Redshift?
Amazon DynamoDB, Amazon EMR, AWS Glue, AWS Data Pipeline are some of the data sources by which you can load data in RedShift data warehouse. The clients can also connect to RedShift with the help of ODBC or JDBC and give the SQL command insert to load the data.

#### Mention the database engines which are supported by Amazon Rds?
The database engines that are supported by Amazon RDS are Amazon Aurora, Mysql, MariaDB, Oracle, SQL Server, and PostgreSQL database engine.

#### What is the work of Amazon Rds?
When a user wants to set up a relational database then Amazon RDS is used. It provisions the infrastructure capacity that a user requests to install the database software. Once the database is set up and functional RDS automates the tasks like patching up of the software, taking the backup of the data and management of synchronous data replication with automatic failover.

#### What is the purpose of standby Rds Instance?
The main purpose of launching a standby RDS instance is to prevent the infrastructure failure (in case failure occurs) so it is stored in a different availability zone which is a totally different infrastructure physically and independent.

#### Are Rds instances upgradable or down gradable according to the Need?
Yes, you can upgrade the RDS instances with the help of following command: modify-db-instance. If you are unable to detect the amount of CPU needed to upgrade then start with db.m1.small DB instance class and monitor the utilization of CPU with the help of tool Amazon Cloud Watch Service.

#### What is Amazon Elastic Ache?
Amazon Elastic ache is an in-memory key-value store which is capable of supporting two key-value engines – Redis and Memcached. It is a fully managed and zero administrations which are hardened by Amazon. With the help of Amazon Elastic ache, you can either build a new high-performance application or improve the existing application. You can find the various application of Elastic ache in the field of Gaming, Healthcare, etc.

#### What is the use of Amazon Elastic Ache?
The performance of web applications could be improved with the help of the caching of information that is used again and again. The information can be accessed very fast using in-memory-caching. With Elastic ache there is no need of managing a separate caching server. You can easily deploy or run an open source compatible in-memory data source with high throughput and low latency.

#### What are the Benefits of Amazon Elastic Ache?
There are various benefits of using Amazon Elastic ache some of which are discussed below:
+ The cache node failures are automatically detected and recovered.
+ It can be easily integrated with other AWS to provide a high performance and secured in-memory cache.
+ As most of the data is managed by Elastic ache such as setup, configuration, and monitoring so that the user can focus on other high-value applications.
+ The performance is enhanced greatly as it only supports the applications which require a very less response time.
+ The Elastic ache can easily scale itself up or scale down according to the need.

#### Explain the Types of Engines in Elastic Ache?
There is two type of engine supported in Elastic ache: Memcached and Redis.
+ Memcached:
  + It is a popular in-memory data store which the developers use for the high-performance cache to speed up applications. By storing the data in memory instead of disk Memcached can retrieve the data in less than a millisecond. It works by keeping every value of the key for every other data to be stored and uniquely identifies each data and lets Memcached quickly find the record.
+ Redis:
  + Today’s applications need low latency and high throughput performance for real-time processing. Due to the performance, simplicity, and capability of redis, it is most favored by the developers. It provides high performance for real-time apps and sub-millisecond latency. It supports complex data types i.n. string, hashes, etc and has a backup and restore capabilities. While Memcached supports key names and values up to 1 MB only redis supports up to 512 MB.

#### Is it possible to run Multiple Db Instances for free for Amazon Rds?
Yes, it is possible to run more than one Single-AZ micro DB instance for Amazon RDS and that’s for free. However, if the usage exceeds 750 instance hours across all the RDS Single-AZ micro DB instances, billing will be done at the standard Amazon RDS pricing across all the regions and database engines.
For example, consider we are running 2 Single-AZ micro DB instances for 400 hours each in one month only; the accumulated usage will be 800 instance hours from which 750 instance hours will be free. In this case, you will be billed for the remaining 50 hours at the standard pricing of Amazon RDS.

#### Which Aws Services will you choose for collecting and processing Ecommerce Data for Realtime Analysis?
I’ll use DynamoDB for collecting and processing e-commerce data for real-time analysis. DynamoDB is a fully managed NoSQL database service that can be used for any type of unstructured data. It can even be used for the e-commerce data taken from e-commerce websites. On this retrieved e-commerce data, analysis can be then performed using RedShift. Elastic MapReduce can also be used for analysis but we’ll avoid it here as real-time analysis if required.

#### What will happen to the Db Snapshots and Backups if any user deletes Db Instance?
When a dB instance is deleted, the user receives an option of making a final dB snapshot. If you do that it will restore your information from that snapshot. AWS RDS keeps all these dB snapshots together that are created by the user along with the all other manually created dB snapshots when the dB instance is deleted. At the same time, automated backups are deleted while manually created dB snapshots are preserved.

## Cassandra

#### Explain what is Cassandra?
Cassandra is an open source data storage system developed at Facebook for inbox search and designed for storing and managing large amounts of data across commodity servers. It can server as both Real time data store system for online applications Also as a read intensive database for business intelligence system

#### List the benefits of using Cassandra?
Unlike traditional or any other database, Apache Cassandra delivers near real-time performance simplifying the work of Developers, Administrators, Data Analysts and Software Engineers.
Instead of master-slave architecture, Cassandra is established on peer-to-peer architecture ensuring no failure.
It also assures phenomenal flexibility as it allows insertion of multiple nodes to any Cassandra cluster in any datacenter. Further, any client can forward its request to any server.
Cassandra facilitates extensible scalability and can be easily scaled up and scaled down as per the requirements. With a high throughput for read and write operations, this NoSQL application need not be restarted while scaling.
Cassandra is also revered for its strong data replication capability as it allows data storage at multiple locations enabling users to retrieve data from another location if one node fails. Users have the option to set up the number of replicas they want to create.
Shows brilliant performance when used for massive datasets and thus, the most preferable NoSQL DB by most organizations.
Operates on column-oriented structure and thus, quickens and simplifies the process of slicing. Even data access and retrieval becomes more efficient with column-based data model.
Further, Apache Cassandra supports schema-free/schema-optional data model, which un-necessitate the purpose of showing all the columns required by your application.

#### What is the use of Cassandra and why to use Cassandra?
Cassandra was designed to handle big data workloads across multiple nodes without any single point of failure. The various factors responsible for using Cassandra are
+ It is fault tolerant and consistent
+ Gigabytes to petabytes scalabilities
+ It is a column-oriented database
+ No single point of failure
+ No need for separate caching layer
+ Flexible schema design
+ It has flexible data storage, easy data distribution, and fast writes
+ It supports ACID (Atomicity, Consistency, Isolation, and Durability)properties
+ Multi-data center and cloud capable
+ Data compression

#### Explain the concept of tunable consistency in Cassandra?
Tunable Consistency is a phenomenal characteristic that makes Cassandra a favored database choice of Developers, Analysts and Big data Architects. Consistency refers to the up-to-date and synchronized data rows on all their replicas. Cassandra’s Tunable Consistency allows users to select the consistency level best suited for their use cases. It supports two consistencies -Eventual and Consistency and Strong Consistency.
The former guarantees consistency when no new updates are made on a given data item, all accesses return the last updated value eventually. Systems with eventual consistency are known to have achieved replica convergence.
For Strong consistency, Cassandra supports the following condition:
R + W > N, where
N – Number of replicas
W – Number of nodes that need to agree for a successful write
R – Number of nodes that need to agree for a successful read

#### Explain what is composite type in Cassandra?
In Cassandra, composite type allows to defined key or a column name with a concatenation of data of different type. You can use two types of Composite Type
Row Key
Column Name

#### How does Cassandra write?
Cassandra performs the write function by applying two commits-first it writes to a commit log on disk and then commits to an in-memory structured known as memtable. Once the two commits are successful, the write is achieved. Writes are written in the table structure as SSTable (sorted string table). Cassandra offers speedier write performance.

#### How Cassandra stores data?
All data stored as bytes
When you specify validator, Cassandra ensures those bytes are encoded as per requirement
Then a comparator orders the column based on the ordering specific to the encoding
While composite are just byte arrays with a specific encoding, for each component it stores a two byte length followed by the byte encoded component followed by a termination bit.

#### Define the management tools in Cassandra?
DataStaxOpsCenter: internet-based management and monitoring solution for Cassandra cluster and DataStax. It is free to download and includes an additional Edition of OpsCenter
SPM primarily administers Cassandra metrics and various OS and JVM metrics. Besides Cassandra, SPM also monitors Hadoop, Spark, Solr, Storm, zookeeper and other Big Data platforms. The main features of SPM include correlation of events and metrics, distributed transaction tracing, creating real-time graphs with zooming, anomaly detection and heartbeat alerting.

#### Mention what are the main components of Cassandra data model?
The main components of Cassandra Data Model are
+ Cluster
+ Keyspace
+ Column
+ Column & Family

#### Define Memtable?
Similar to table, memtable is in-memory/write-back cache space consisting of content in key and column format. The data in memtable is sorted by key, and each ColumnFamily consist of a distinct memtable that retrieves column data via key. It stores the writes until it is full, and then flushed out.

#### Explain what is a Column Family in Cassandra?
Column family in Cassandra is referred for a collection of Rows.

#### What is SStable and how is it different from other relational tables?
SSTable expands to ‘Sorted String Table,’ which refers to an important data file in Cassandra and accepts regular written memtables. They are stored on disk and exist for each Cassandra table. Exhibiting immutability, SStables do not allow any further addition and removal of data items once written. For each SSTable, Cassandra creates three separate files like partition index, partition summary and a bloom filter.

#### Explain what is a Cluster in Cassandra?
A cluster is a container for keyspaces. Cassandra database is segmented over several machines that operate together. The cluster is the outermost container which arranges the nodes in a ring format and assigns data to them. These nodes have a replica which takes charge in case of data handling failure.

#### Explain the concept of Bloom Filter?
Associated with SSTable, Bloom filter is an off-heap (off the Java heap to native memory) data structure to check whether there is any data available in the SSTable before performing any I/O disk operation.

#### List out the other components of Cassandra?
The other components of Cassandra are
+ Node
+ Data Center
+ Cluster
+ Commit log
+ Mem-table
+ SSTable
+ Bloom Filter

#### Explain Cap Theorem?
With a strong requirement to scale systems when additional resources are needed, CAP Theorem plays a major role in maintaining the scaling strategy. It is an efficient way to handle scaling in distributed systems. Consistency Availability and Partition tolerance (CAP) theorem states that in distributed systems like Cassandra, users can enjoy only two out of these three characteristics.
One of them needs to be sacrificed. Consistency guarantees the return of most recent write for the client, Availability returns a rational response within minimum time and in Partition Tolerance, the system will continue its operations when network partitions occur. The two options available are AP and CP.

#### Explain what is a Keyspace in Cassandra?
In Cassandra, a keyspace is a namespace that determines data replication on nodes. A cluster consist of one keyspace per node.

#### State the differences between Node and Cluster And DataCenter in Cassandra?
While a node is a single machine running Cassandra, cluster is a collection of nodes that have similar type of data grouped together. DataCentersare useful components when serving customers in different geographical areas. You can group different nodes of a cluster into different data centers.

#### Mention what are the values stored in the Cassandra Column?
In Cassandra Column, basically there are three values
+ Column Name
+ Value
+ Time Stamp

#### How to write a Query in Cassandra?
Using CQL (Cassandra Query Language).Cqlsh is used for interacting with database.

#### Mention when you can use Alter Keyspace?
ALTER KEYSPACE can be used to change properties such as the number of replicas and the durable_write of a keyspace.

#### What os Cassandra supports?
Windows and Linux.

#### Explain what is Cassandra cqlsh?
Cassandra-Cqlsh is a query language that enables users to communicate with its database. By using Cassandra cqlsh, you can do following things
+ Define a schema
+ Insert a data and
+ Execute a query

#### What is Cassandra Data Model?
Cassandra Data Model consists of four main components:
+ Cluster: Made up of multiple nodes and keyspaces
+ Keyspace: a namespace to group multiple column families, especially one per partition
+ Column: consists of a column name, value and timestamp
+ ColumnFamily: multiple columns with row key reference.

#### Mention what does the Shell Commands capture And consistency determines?
There are various Cqlsh shell commands in Cassandra. Command “Capture”, captures the output of a command and adds it to a file while, command “Consistency” display the current consistency level or set a new consistency level.

#### What is Cql?
CQL is Cassandra Query language to access and query the Apache distributed database. It consists of a CQL parser that incites all the implementation details to the server. The syntax of CQL is similar to SQL but it does not alter the Cassandra data model.

#### What is mandatory while creating a table in Cassandra?
While creating a table primary key is mandatory, it is made up of one or more columns of a table.

#### Explain the concept of compaction in Cassandra?
Compaction refers to a maintenance process in Cassandra , in which, the SSTables are reorganized for data optimization of data structure son the disk. The compaction process is useful during interactive with memtable. There are two type sof compaction in Cassandra:
+ Minor compaction: started automatically when a new sstable is created. Here, Cassandra condenses all the equally sized sstables into one.
+ Major compaction : is triggered manually using nodetool. Compacts all sstables of a ColumnFamily into one.

#### Mention what needs to be taken care while adding a Column?
+ While adding a column you need to take care that the Column name is not conflicting with the existing column names 
+ Table is not defined with compact storage option

#### Does Cassandra support ACID transactions?
Unlike relational databases, Cassandra does not support ACID transactions.

#### Explain how Cassandra writes data?
Cassandra writes data in three components
+ Commitlog write
+ Memtable write
+ SStable write

#### Explain what is Memtable in Cassandra?
Cassandra writes the data to a in memory structure known as Memtable.
It is an in-memory cache with content stored as key/column.
By key Memtable data are sorted.
There is a separate Memtable for each ColumnFamily, and it retrieves column data from the key.

#### Define the Consistency Levels for Read Operations in Cassandra?
+ ALL: Highly consistent. A write must be written to commitlog and memtable on all replica nodes in the cluster
+ EACH_QUORUM: A write must be written to commitlog and memtable on quorum of replica nodes in all data centers.
+ LOCAL_QUORUM:A write must be written to commitlog and memtable on quorum of replica nodes in the same center.
+ ONE: A write must be written to commitlog and memtableof at least one replica node.
+ TWO, Three: Same as One but at least two and three replica nodes, respectively
+ LOCAL_ONE: A write must be written for at least one replica node in the local data center ANY
+ SERIAL: Linearizable Consistency to prevent unconditional updates
+ LOCAL_SERIAL: Same as Serial but restricted to local data center

#### Explain how Cassandra writes changed data into Commitlog?
Cassandra concatenate changed data to commitlog
Commitlog acts as a crash recovery log for data
Until the changed data is concatenated to commitlog write operation will be never considered successful
Data will not be lost once commitlog is flushed out to file.

#### What is difference between Column and Super Column?
Both elements work on the principle of tuple having name and value. However, the former‘s value is a string while the value in latter is a Map of Columns with different data types.
Unlike Columns, Super Columns do not contain the third component of timestamp.

#### What is ColumnFamily?
As the name suggests, ColumnFamily refers to a structure having infinite number of rows. That are referred by a key-value pair, where key is the name of the column and value represents the column data. It is much similar to a hashmap in java or dictionary in Python. Rememeber, the rows are not limited to a predefined list of Columns here. Also, the ColumnFamily is absolutely flexible with one row having 100 Columns while the other only 2 columns.

#### Explain how Cassandra delete data?
SSTables are immutable and cannot remove a row from SSTables. When a row needs to be deleted, Cassandra assigns the column value with a special value called Tombstone. When the data is read, the Tombstone value is considered as deleted.

#### Define the use of Source Command in Cassandra?
Source command is used to execute a file consisting of CQL statements.

#### What is Thrift?
Thrift is a legacy RPC protocol or API unified with a code generation tool for CQL. The purpose of using Thrift in Cassandra is to facilitate access to the DB across the programming language.

#### Explain Tombstone in Cassandra?
Tombstone is row marker indicating a column deletion. These marked columns are deleted during compaction. Tombstones are of great significance as Cassnadra supports eventual consistency, where the data must respond before any successful operation.

#### What Platforms Cassandra runs on?
Since Cassandra is a Java application, it can successfully run on any Java-driven platform or Java Runtime Environment (JRE) or Java Virtual Machine (JVM). Cassandra also runs on RedHat, CentOS, Debian and Ubuntu Linux platforms.

#### Name the ports Cassandra uses?
The default settings state that Cassandra uses 7000 ports for Cluster Management, 9160 for Thrift Clients, 8080 for JMX. These are all TCP ports and can be edited in the configuration file: bin/Cassandra.in.sh

#### Can you Add Or Remove column families in a working cluster?
Yes, but keeping in mind the following processes.
Do not forget to clear the commitlog with ‘nodetool drain’
Turn off Cassandra to check that there is no data left in commitlog
Delete the sstable files for the removed CFs

#### What is Replication Factor in Cassandra?
Replication Factor is the measure of number of data copies existing. It is important to increase the replication factor to log into the cluster.

#### Can we change Replication Factor on a Live Cluster?
Yes, but it will require running repair to alter the replica count of existing data.

#### How to Iterate all rows in ColumnFamily?
Using get_range_slices. You can start iteration with the empty string and after each iteration, the last key read serves as the start key for next iteration.

#### Explain Cassandra.
Cassandra is a popular NOSQL database management system used to handle large amount of data. It is free and open source distributed database that provides high availability without any failure.

#### In which language Cassandra is written?
Cassandra is written in Java. It is originally designed by Facebook consisting of flexible schemas. It is highly scalable for big data.

#### Which query language is used in Cassandra database?
Cassandra introduced its own Cassandra Query Language (CQL). CQL is a simple interface for accessing Cassandra, as an alternative to the traditional Structured Query Language (SQL).

#### What are the benefits and advantages of Cassandra?
Cassandra delivers real-time performance simplifying the work of Developers, Administrators, Data Analysts and Software Engineers.
It provides extensible scalability and can be easily scaled up and scaled down as per the requirements.
Data can be replicated to several nodes for fault-tolerance.
Being a distributed management system, there is no single point of failure.
Every node in a cluster contains different data and able to serve any request.

#### Where Cassandra stores its data?
Cassandra stores its data in the data dictionary.

#### What was the design goal of Cassandra?
The main design goal of Cassandra was to handle big data workloads across multiple nodes without a single point of failure.

#### How many types of NoSQL databases and give some examples.
There are mainly 4 types of NoSQL databases:
+ Document store types ( MongoDB and CouchDB)
+ Key-Value store types ( Redis and Voldemort)
+ Column store types ( Cassandra)
+ Graph store types ( Neo4j and Giraph)

#### What is keyspace in Cassandra?
In Cassandra, a keyspace is a namespace that determines data replication on nodes. A cluster contains of one keyspace per node.

#### What are the different composite keys in Cassandra?
In Cassandra, composite keys are used to define key or a column name with a concatenation of data of different type. There are two types of Composite key in Cassandra:
+ Row Key
+ Column Name

#### What is data replication in Cassandra?
Data replication is an electronic copying of data from a database in one computer or server to a database in another so that all users can share the same level of information. Cassandra stores replicas on multiple nodes to ensure reliability and fault tolerance. The replication strategy decides the nodes where replicas are placed.

#### What is node in Cassandra?
In Cassandra, node is a place where data is stored.

#### What do you mean by data center in Cassandra?
Data center is a complete data of clusters.

#### What do you mean by commit log in Cassandra?
In Cassandra, commit log is a crash-recovery mechanism. Every write operation is written to the commit log.

#### What do you mean by column family in Cassandra?
Column family is a table in RDMS that contains an ordered collection of rows.

#### What do you mean by consistency in Cassandra?
Consistency in Cassandra specifies how to synchronize and up to date a row of Cassandra data and its replicas.

#### How does Cassandra perform write function?
Cassandra performs the write function by applying two commits:
First commit is applied on disk and then second commit to an in-memory structure known as memtable.
When the both commits are applied successfully, to write is achieved.
Writes are written in the table structure as SSTable (sorted string table).

#### What is SSTable?
SSTable is a short form of 'Sorted String Table'. It refers to an important data file in Cassandra and accepts regular written memtables. They are stored on disk and exist for each Cassandra table.

#### How the SSTable is different from other relational tables?
SStables do not allow any further addition and removal of data items once written. For each SSTable, Cassandra creates three separate files like partition index, partition summary and a bloom filter.

#### What is the role of ALTER KEYSPACE?
ALTER KEYSPACE is used to change the value of DURABLE_WRITES with its related properties.

#### What are the differences between node and cluster and datacenter in Cassandra?
+ Node: A node is a single machine running Cassandra.
+ Cluster: A cluster is a collection of nodes that contains similar types of data together.
+ Datacenter: A datacenter is a useful component when serving customers in different geographical areas. Different nodes of a cluster can be grouped into different data centers.

#### What is the use of Cassandra CQL collection?
Cassandra CQL collection is used to collect the data and store it in a column where each collection represents the same type of data. CQL consist of three types of types:
+ SET: It is a collection of unordered list of unique elements.
+ List: It is a collection of elements arranged in an order and can contain duplicate values.
+ MAP: It is a collection of unique elements in a form of key-value pair.

#### What is the use of Bloom Filter in Cassandra?
On a request of a data, before doing any disk I/O Bloom filter checks whether the requested data exist in the row of SSTable.

#### How does Cassandra delete data?
In Cassandra, to delete a row, it is required to associate the value of column to Tombstone (where Tombstone is a special value).

#### What is SuperColumn in Cassandra?
In Cassandra, SuperColumn is a unique element containing similar collection of data. They are actually key-value pairs with values as columns.

#### What are the Hadoop and HBase and Hive and Cassandra?
Hadoop, HBase, Hive and Cassandra all are Apache products.
Apache Hadoop supports file storage, grid compute processing via Map reduce. Apache Hive is a SQL like interface on the top of Hadoop. 
Apache HBase follows column family storage built like Big Table. 
Apache Cassandra also follows column family storage built like Big Table with Dynamo topology and consistency.

#### What is the usage of void close method?
In Cassandra, the void close() method is used to close the current session instance.

#### Which command is used to start the cqlsh prompt?
The cqlsh command is used to start the cqlsh prompt.

#### What is the usage of cqlsh version command?
The "cqlsh-version" command is used to provide the version of the cqlsh you are using.

#### Does Cassandra work on Windows?
Yes. Cassandra is compatible on Windows and works pretty well. Now its Linux and Window compatible version are available.

#### What is Kundera in Cassandra?
In Cassandra, Kundera is an object-relational mapping (ORM) implementation which is written using Java annotations.

#### What do you mean by Thrift in Cassandra?
Thrift is the name of RPC client which is used to communicate with the Cassandra Server.

#### What is Hector in Cassandra?
Hector was one of the early Cassandra clients. It is an open source project written in Java using the MIT license.

## Apache Kafka

#### Mention what is Apache Kafka?
Apache Kafka is a publish-subscribe messaging system developed by Apache written in Scala. It is a distributed, p#artitioned and replicated log service.

#### Mention what is the traditional method of message transfer?
The traditional method of message transfer includes two methods
+ Queuing: In a queuing, a pool of consumers may read message from the server and each message goes to one of them
+ Publish-Subscribe: In this model, messages are broadcasted to all consumers

Kafka caters single consumer abstraction that generalized b#oth of the above- the consumer group.

#### Mention what is the benefits of Apache Kafka over the traditional technique?
Apache Kafka has following benefits above traditional messaging technique
+ Fast: A single Kafka broker can serve thousands of clients by handling megabytes of reads and writes per second
+ Scalable: Data are partitioned and streamlined over a cluster of machines to enable larger data
+ Durable: Messages are persistent and is replicated within the cluster to prevent data loss
+ Distributed by Design: It provides fault tolerance g#uarantees and durability

#### Mention what is the meaning of Broker in Kafka?
I#n Kafka cluster, broker term is used to refer Server.

#### Mention what is the Maximum Size of the Message does Kafka server can Receive?
The maximum size of the message that Kafka server can r#eceive is 1000000 bytes.

#### Explain what is Zookeeper in Kafka and can we use Kafka without Zookeeper?
Zookeeper is an open source, high-performance co-ordination service used for distributed applications adapted by Kafka.
No, it is not possible to bye-pass Zookeeper and connect straight to the Kafka broker. Once the Zookeeper is down, it cannot serve client request.
Zookeeper is basically used to communicate between different nodes in a cluster
In Kafka, it is used to commit offset, so if node fails in any case it can be retrieved from the previously committed offset
Apart from this it also does other activities like leader detection, distributed synchronization, configuration management, identifies when a new node leaves or joins, t#he cluster, node status in real time, etc.

#### Explain how message is consumed by Consumer in Kafka?
Transfer of messages in Kafka is done by using sendfile API. It enables the transfer of bytes from the socket to disk via kernel space saving copies and call between k#ernel user back to the kernel.

#### Explain how you can improve the throughput of a remote consumer?
If the consumer is located in a different data center from the broker, you may require to tune the socket buffer size t#o amortize the long network latency.

#### Explain how you can get Exactly Once Messaging from Kafka during data production?
During data, production to get exactly once messaging from Kafka you have to follow two things avoiding duplicates during data consumption and avoiding duplication during data production.
Here are the two ways to get exactly one semantics while data production:
Avail a single writer per partition, every time you get a network error checks the last message in that partition to see if your last write succeeded
In the message include a primary key (UUID or something) a#nd de-duplicate on the consumer

#### Explain how you can reduce churn in Isr and when does Broker leave the Isr?
ISR is a set of message replicas that are completely synced up with the leaders, in other word ISR has all messages that are committed. ISR should always include all replicas until there is a real failure. A replica will be d#ropped out of ISR if it deviates from the leader.

#### Why Replication is required in Kafka?
Replication of message in Kafka ensures that any published message does not lose and can be consumed in case of machine error, program error or more common software u#pgrades.

#### What does it indicate if replica stays out of Isr for a long time?
If a replica remains out of ISR for an extended time, it indicates that the follower is unable to fetch data as f#ast as data accumulated at the leader.

#### Mention what happens if the preferred replica is not in the Isr?
If the preferred replica is not in the ISR, the controller w#ill fail to move leadership to the preferred replica.

#### Is it possible to get the Message Offset after Producing?
You cannot do that from a class that behaves as a producer like in most queue systems, its role is to fire and forget the messages. The broker will do the rest of the work like appropriate metadata handling with id’s, offsets, etc.
As a consumer of the message, you can get the offset from a Kafka broker. If you gaze in the SimpleConsumer class, you will notice it fetches MultiFetchResponse objects that include offsets as a list. In addition to that, when you iterate the Kafka Message, you will have MessageAndOffset o#bjects that include both, the offset and the message sent.

#### Mention what is the difference between Apache Kafka and Apache Storm?
Apach Kafeka: It is a distributed and robust messaging system that can handle huge amount of data and allows passage of messages from one end-point to another.
Apache Storm: It is a real time message processing system, and you can edit or manipulate data in real time. Apache storm pulls the data from Kafka and applies some required m#anipulation.

#### List the various components in Kafka?
The four major components of Kafka are:
+ Topic – a stream of messages belonging to the same type
+ Producer – that can publish messages to a topic
+ Brokers – a set of servers where the publishes messages are stored
+ Consumer – that subscribes to various topics and pulls d#ata from the brokers.

#### Explain the role of the Offset?
Messages contained in the partitions are assigned a unique ID number that is called the offset. The role of the offset is to uniquely identify every message within the p#artition.

#### Explain the concept of Leader and Follower?
Every partition in Kafka has one server which plays the role of a Leader, and none or more servers that act as Followers. The Leader performs the task of all read and write requests for the partition, while the role of the Followers is to passively replicate the leader. In the event of the Leader failing, one of the Followers will take on the role of the Leader. This ensures load b#alancing of the server.

#### How do you define a Partitioning Key?
Within the Producer, the role of a Partitioning Key is to indicate the destination partition of the message. By default, a hashing-based Partitioner is used to determine the partition ID given the key. Alternatively, users can a#lso use customized Partitions.

#### In the Producer when does Queuefullexception occur?
QueueFullException typically occurs when the Producer attempts to send messages at a pace that the Broker cannot handle. Since the Producer doesn’t block, users will need to add enough brokers to collaboratively handle the i#ncreased load.

#### Explain the role of the Kafka Producer Api.
The role of Kafka’s Producer API is to wrap the two producers – kafka.producer.SyncProducer and the kafka.producer.async.AsyncProducer. The goal is to expose all the producer functionality through a single API to the client.

## Snowflake

#### What is a stored procedure and how it works?

A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

So if you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.

You can also pass parameters to a stored procedure, so that the stored procedure can act based on the parameter value(s) that is passed.

The JavaScript API for stored procedures is similar to, but not identical to, the APIs in Snowflake connectors and drivers (Node.js, JDBC, Python, etc.).

The API enables you to perform operations such as:

- Execute a SQL statement.
- Retrieve the results of a query (i.e. a result set).
- Retrieve metadata about the result set (number of columns, data types of the columns, etc.)

To create a stored procedure we use the below syntax:

```sql
CREATE OR REPLACE PROCEDURE procedure_name
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
sql_statements;
RETURN 'Success';
END;
$$;
```

To run/execute the stored procedure we use the below command:

```sql
EXEC procedure_name;
```

#### What so you mean by a task in Snowflake?

A task in snowflake is a piece of SQL code that runs either when we call it manually or schedule it to run on specific intervals of time.

Snowflake Tasks are schedulers that can assist you in scheduling a single SQL Query or Stored Procedure. When paired with streams to create an end-to-end Data Pipeline, a job can be quite beneficial.

Tasks can execute a single SQL statement or a stored procedure.

A task can also be scheduled to run at any instance of time. Currently, a task is not able to run multiple SQL statements.

Since a snowflake task can execute a stored procedure, we can add that stored procedure within that task and schedule that task to run at specific intervals of time.

```sql
CREATE OR REPLACE task_name
WAREHOUSE = COMPUTE_WH
SCHEDULE = '1 MINUTE'
AS
call procedure_name;
```

#### What are analytical functions? Can you explain with an example?

Analytical functions are used to calculate an aggregated value from the dataset but are based on a specific set of rows instead of the entire dataset. As compared to aggregate functions like SUM, COUNT, AVG, etc. which return scalar records, these functions can return multiple records based on the conditions. The most common examples of using these functions are to find moving averages, running totals, etc. SQL Server supports the following analytic functions.

a. CUME_DIST — Find the cumulative distribution of a numerical column
b. FIRST_VALUE — Finds the first value of a column from the group and prints the same for each row
c. LAST_VALUE — Finds the last value of a column from the group and prints the same for each row
d. LAG — Reads values after the specified number of rows for a column
e. LEAD — Reads values before the specified number of rows for a column
f. rank() and dense_rank()

#### What are the different types of warehouses in Snowflake?

Warehouses are required for queries, as well as all DML operations, including loading data into tables. A warehouse is defined by its size, as well as the other properties that can be set to help control and automate warehouse activity.

Warehouses can be started and stopped at any time. They can also be resized at any time, even while running, to accommodate the need for more or less compute resources, based on the type of operations being performed by the warehouse.

#### What do you mean my micro partition?

Traditional data warehouses rely on static partitioning of large tables to achieve acceptable performance and enable better scaling. In these systems, a partition is a unit of management that is manipulated independently using specialized DDL and syntax; however, static partitioning has a number of well-known limitations, such as maintenance overhead and data skew, which can result in disproportionately-sized partitions.

In contrast to a data warehouse, the Snowflake Data Platform implements a powerful and unique form of partitioning, called micro-partitioning, that delivers all the advantages of static partitioning without the known limitations, as well as providing additional significant benefits.

**Benefits of Micro-partitioning:**

a. Snowflake micro-partitions are derived automatically; they don’t need to be explicitly defined up-front or maintained by users.
b. As the name suggests, these are small partitions 50MB to 500MB, which enables extremely efficient DML and fine-grained pruning for faster queries.
c. Helps prevent skew.
d. As the data is stored independently and in columnar storage, only the columns referenced in the query are scanned.
e. Columns are also compressed individually within micro-partitions. Snowflake automatically determines the most efficient compression algorithm for the columns in each micro-partition.

#### What is QUALIFY function in Snowflake?

In a SELECT statement, the QUALIFY clause filters the results of window functions.

QUALIFY does with window functions what HAVING does with aggregate functions and GROUP BY clauses.

In the execution order of a query, QUALIFY is therefore evaluated after window functions are computed. Typically, a SELECT statement’s clauses are evaluated in the order shown below:

- From
- Where
- Group by
- Having
- Window
- QUALIFY
- Distinct
- Order by
- Limit

#### Can you tell me something about query optimization practices in Snowflake?

Query optimization simply means that tuning the query such that the database doesn’t become slower. Also the queries might return results faster. Following are the techniques of query optimization,

a. Maximizing Caching
b. Using materialized views wherever possible.
c. Scaling up, means increasing the size of the warehouse for complex queries.
d. Scaling out, means adding more and more data warehouses of the same size.

#### Tell me something about storage integration object.

Creates a new storage integration in the account or replaces an existing integration.

A storage integration is a Snowflake object that stores a generated identity and access management (IAM) entity for your external cloud storage, along with an optional set of allowed or blocked storage locations (Amazon S3, Google Cloud Storage, or Microsoft Azure).

What this means is that if we define the storage integration object for Amazon S3 (below code), we are able to access the files from s3 into snowflake. The storage integration object is an object defining the configuration and what is allowed and what is not allowed.

```sql
//Creating an integration object. 
CREATE OR REPLACE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE 
  STORAGE_AWS_ROLE_ARN = ''
  STORAGE_ALLOWED_LOCATIONS = ('s3://<your-bucket-name>/<your-path>/', 's3://<your-bucket-name>/<your-path>/')
   COMMENT = 'This is an optional comment'
//Describing the integration object.
DESC INTEGRATION s3_int;
```

#### How do you create a user ?

A user in snowflake is a person having access to snowflake and also has a role associate to it. To create a user and assign a role to it, we need to create a role first. (If the role is already created then we can just create a user and assign role to it.)

To create a user type in the following command:

```sql
CREATE USER 'JOHN' PASSWORD = 'Notasimplepassword123!@'
```

#### How do you share objects to different users in Snowflake?

Since in snowflake each newly created user has a default PUBLIC role assigned to him, we can now directly start giving privileges if we want to.

```sql
//Granting usage permission to warehouse
GRANT USAGE ON WAREHOUSE READ_WH TO ROLE PUBLIC;

//Granting usage permissions to database.
GRANT USAGE ON DATABASE READ_DB TO ROLE PUBLIC;

//Grant usage permissions to schema.
GRANT USAGE ON SCHEMA INFORMATION_SCHEMA TO ROLE PUBLIC;

//Grant usage permissions to tables.
GRANT SELECT ON ALL TABLES IN SCHEMA INFORMATION_SCHEMA TO ROLE PUBLIC;
```

#### What is the difference between permanent, transient and temporary table?

There are 3 types of tables in Snowflake.

a. Permanent Table — Permanent table is like a normal table which will be stored in a database and dropped until explicitly stated. These have time travel and fail safe functionality depending on which edition you are using.
b. Transient Table — Snowflake supports creating transient tables that persist until explicitly dropped and are available to all users with the appropriate privileges. Transient tables are similar to permanent tables with the key difference that they do not have a Fail-safe period.
As a result, transient tables are specifically designed for transitory data that needs to be maintained beyond each session (in contrast to temporary tables), but does not need the same level of data protection and recovery provided by permanent tables.
c. Temporary Table — Snowflake supports creating temporary tables for storing non-permanent, transitory data (e.g. ETL data, session-specific data). Temporary tables only exist within the session in which they were created and persist only for the remainder of the session. As such, they are not visible to other users or sessions. Once the session ends, data stored in the table is purged completely from the system and, therefore, is not recoverable, either by the user who created the table or Snowflake.

:::note
Snowflake also supports creating transient databases and schemas. All tables created in a transient schema, as well as all schemas created in a transient database, are transient by definition.
:::

#### Can you perform DML operations on views?

DML operations could be performed through a simple view. DML operations could not always be performed through a complex view. INSERT, DELETE and UPDATE are directly possible on a simple view. We cannot apply INSERT, DELETE and UPDATE on complex view directly.

#### What is the difference between views and materialized views?

Similar to views, materialized views are also database objects which are formed based on a SQL Query however unlike views, the contents or data of the materialized views are periodically refreshed based on its configuration.

The contents of view will get updated automatically when the underlying table (forming the query) data gets changed. However, materialized views can be configured to refresh its contents periodically or can be manually refreshed when needed.

Creating materialized views can be a very good approach for performance tuning especially when dealing with remote tables.

```sql
create materialized view mymv
    comment='Test view'
    as
    select col1, col2 from mytable;
```

#### What is a merge statement?

Merge is part of the DML commands in SQL which can be used either perform INSERT or UPDATE based on the data in the respective table.

If the desired data is present then merge will update the records. If desired data is not present then merge will insert the records.

Sample merge statement is shown below. Here if the managers and directors table have matching records based the ID field then UPDATE command will be run else if there are no matching records then INSERT statement will be executed.

```sql
MERGE INTO managers m
USING directors d  ON (m.id = d.id)
WHEN MATCHED THEN
    UPDATE SET name = 'TEST'
WHEN NOT MATCHED THEN
    INSERT VALUES (d.id, d.name, 0);
```

#### What is a trigger?

Trigger is a database object which is similar to a stored procedure which will automatically get invoked or executed when the specified event occurs in the database.

The most common type of triggers are DML triggers, DDL triggers and Database triggers (also referred as Logon triggers).

DML triggers are invoked when a DML operation (INSERT, UPDATE, DELETE) occurs on the respective table (table on which the trigger was created). Trigger can be configured to invoke either before the DML operation or after the DML operation.

DDL triggers are invoked when a DDL operation (CREATE, ALTER, DROP) occurs on the respective table (table on which the trigger was created).

Database trigger is invoked when the database session is established or shut down.

#### What is difference between WHERE and HAVING clause?

WHERE clause is used to filter records from the table. We can also specify join conditions between two tables in the WHERE clause. If a SQL query has both WHERE and GROUP BY clause then the records will first get filtered based on the conditions mentioned in WHERE clause before the data gets grouped as per the GROUP BY clause.

Whereas HAVING clause is used to filter records returned from the GROUP BY clause. So if a SQL query has WHERE, GROUP BY and HAVING clause then first the data gets filtered based on WHERE condition, only after this grouping of data takes place. Finally based on the conditions in HAVING clause the grouped data again gets filtered.

#### What is an external table in Snowflake?

In a typical table, the data is stored in the database; however, in an external table, the data is stored in files in an external stage. External tables store file-level metadata about the data files, such as the filename, a version identifier and related properties. This enables querying data stored in files in an external stage as if it were inside a database. External tables can access data stored in any format supported by COPY INTO <table_name> statements.

External tables are read-only, therefore no DML operations can be performed on them.

However, external tables can be used for query and join operations. Views can be created against external tables.

Querying data stored external to the database is likely to be slower than querying native database tables; however, materialized views based on external tables can improve query performance.

#### What is the difference between a secure view and a normal view?

A normal view is when a view is created from a table and then everyone who has access to the view can see all the data in the view along with “THE SQL QUERY THAT HAS BEEN USED TO CREATE THE VIEW”. If the user can see the SQL query then the user will know that something has been filtered in the WHERE clause and the view is not as complete as the table.

In this scenario, we can make use of secure view.

A secure view only allows a role to see whatever is written in the SELECT statement “WITHOUT ACTUALLY SEEING THE SQL QUERY THAT HAS BEEN USED TO CREATE THE VIEW”. So that user will see the view but will not know what has been filtered out as he cannot see the SQL query.

Also you can see a boolean value for a column “is_secure” when you see all the views by using the below query.

True means that the view is secure.

False means that the view is not secure. In short the view is normal.

:::note
Don’t confuse this with Dynamic data masking policy. In a dynamic data masking policy we are showing all the columns but using some sort of special characters like `***-**` in the column data to hide the data from the user.

In secure view we are showing all columns already filtered out.
:::

## Apache Spark

#### What are the main features of Apache Spark?
Main features of Apache Spark are as follows:
+ Performance: The key feature of Apache Spark is its Performance. With Apache Spark we can run programs up to 100 times faster than Hadoop MapReduce in memory. On disk we can run it 10 times faster than Hadoop.
+ Ease of Use: Spark supports Java, Python, R, Scala etc. languages. So it makes it much easier to develop applications for Apache Spark.
+ Integrated Solution: In Spark we can create an integrated solution that combines the power of SQL, Streaming and data analytics.
  R+ un Everywhere: Apache Spark can run on many platforms. It can run on Hadoop, Mesos, in Cloud or standalone. It can also connect to many data sources like HDFS, Cassandra, HBase, S3 etc.
+ Stream Processing: Apache Spark also supports real time stream processing. With real time streaming we can provide real time analytics solutions. This is very useful for real-time data.

#### What is a Resilient Distribution Dataset in Apache Spark?
Resilient Distribution Dataset (RDD) is an abstraction of data in Apache Spark. It is a distributed and resilient collection of records spread over many partitions. RDD hides the data partitioning and distribution behind the scenes. Main	features of RDD 	are as follows:
+ Distributed: Data in a RDD is distributed across multiple nodes.
+ Resilient: RDD is a fault- tolerant dataset. In case of node failure, Spark can re- compute data.
+ Dataset: It is a collection of data similar to collections in Scala.
+ Immutable: Data in RDD cannot be modified after creation. But we can transform it using a Transformation.

#### What is a Transformation in Apache Spark?
Transformation in Apache Spark is a function that can be applied to a RDD. Output of a Transformation is another RDD. Transformation in Spark is a lazy operation. It means it is not executed immediately. Once we call an action, transformation is executed. A Transformation does not change the input RDD. We can also create a pipeline of certain Transformations to create a Data flow.

#### What are security options in Apache Spark?
Apache Spark provides following security options:
Encryption: Apache Spark supports encryption by SSL. We can use HTTPS protocol for secure data transfer. Therefore data is transmitted in encrypted mode. We can use spark.ssl parameters to set the SSL configuration.

Authentication: We can perform authentication by a shared secret in Apache Spark. We can use spark.authenticate	to configure authentication in Spark.
Event Logging: If we use Event Logging, then we can set the permissions on the directory where event logs are	stored.	These permissions can ensure access control for Event log.

#### How will you monitor Apache Spark?
We can use the Web UI provided by SparkContext to monitor Spark. We can access this Web UI at port 4040 to get the useful information. Some of the information that we can monitor is:
+ Scheduler tasks and stages RDD	Sizes	and	Memory usage Spark	Environment Information
+ Executors Information
+ Spark also provides a Metrics library. This library can be used to send Spark information to HTTP, JMX, CSV files etc.This is another option to collect Spark runtime information for monitoring another dashboard tool.

#### What are the main libraries of Apache Spark?
Main libraries of Apache Spark are as follows:
+ MLib: This is Spark’s Machine Learning library. We can use it to create scalable machine learning system. We can use various machine learning algorithms as well as features like pipelining etc with this library.
+ GraphX: This library is used for computation of Graphs. It helps in creating a Graph abstraction of data and then use various Graph operators like- SubGraph, joinVertices etc.
+ Structured Streaming: This library is used for handling streams in Spark. It is a fault tolerant system built on top of Spark SQL Engine to process streams.
+ Spark SQL: This is another popular component that is used	for	processing	SQL queries on Spark platform.
+ SparkR: This is a package in Spark to use Spark from R language. We can use R data frames, dplyr etc from this package. We can also start SparkR from RStudio.

#### What are the main functions of Spark Core in Apache Spark?
Spark Core is the central component of Apache Spark. It serves following functions:
+ Distributed Task Dispatching
+ Job Scheduling
+ I/O Functions

#### How will you do memory tuning in Spark?
In case of memory tuning we have to take care of these points.
Amount of memory used by objects Cost of accessing objects Overhead	of Garbage Collection
Apache Spark stores objects in memory for caching. So it becomes important to perform memory tuning in a Spark application. First we determine the memory usage by the application. To do this we first create a RDD and put it in cache. Now we can see the size of the RDD in storage page of Web UI. This will tell the amount of memory consumed by RDD. Based on the memory usage, we can estimate the amount of memory needed for our task. In case we need tuning, we can follow these practices to reduce memory usage:
Use data structures like Array of objects or primitives instead of Linked list or HashMap. Fastutil library provides convenient collection classes for primitive types compatible with Java.
We have to reduce the usage of nested data structures with a large number of small objects and pointes. E.g. Linked list has pointers within each node.
It is a good practice to use numeric IDs instead of Strings for keys.
We can also use JVM flag - XX:+UseCompressedOops to	make pointers be four bytes instead of eight.

#### What are the two ways to create RDD in Spark?
We can create RDD in Spark in following two ways:
+ Internal: We can parallelize an existing collection of data within our Spark Driver program and create a RDD out of it.
+ External: We can also create RDD by referencing a Dataset in an external data source like AWS S3, HDFS, HBASE etc.

#### What are the main operations that can be done on a RDD in Apache Spark?
There are two main operations that can be performed on a RDD in Spark:
+ Transformation: This is a function that is used to create a new RDD out of an existing RDD.
+ Action: This is a function that returns a value to Driver program after running a computation on RDD.

#### What are the common Transformations in Apache Spark?
Some common transformations in Apache Spark are as follows:
+ Map(func): This is a basic transformation that returns a new dataset by passing each element of input dataset through func function.
+ Filter(func):	This transformation returns a new dataset of elements that return true for func function. It is used to filter elements in a dataset based on criteria in func function.
+ Union(other Dataset): This is used to combine a dataset with another dataset to form a union of two datasets.
+ Intersection(other Dataset):	This transformation gives the elements common to two datasets.
+ Pipe(command, [envVars]): This transformation passes each partition of the dataset through a shell command.

#### What are the common Actions in Apache Spark?
Some commonly used Actions in Apache Spark are as follows:
+ Reduce(func): This Action aggregates the elements of a dataset by using func function.
+ Count(): This action gives the total number of elements in a Dataset.
+ Collect(): This action will return all the elements of a dataset as an Array to the driver program.
+ First(): This action gives the first element of a collection.
+ Take(n): This action gives the first n elements of dataset.
+ Foreach(func): This action runs each element in dataset through a for loop and executes function func on each element.

#### What is a Shuffle operation in Spark?
Shuffle operation is used in Spark to re-distribute data across multiple partitions. It is a costly and complex operation. In general a single task in Spark operates on elements in one partition. To execute shuffle, we have to run an operation on all elements of all partitions. It is also called all-to-all operation.

#### What are the operations that can cause a shuffle in Spark?
Some of the common operations that can cause a shuffle internally in Spark are as follows:
+ Repartition
+ Coalesce
+ GroupByKey
+ ReduceByKey
+ Cogroup
+ Join

#### What is purpose of Spark SQL?
Spark SQL is used for running SQL queries. We can use Spark SQL to interact with SQL as well as Dataset API in Spark. During execution, Spark SQL uses same computation engine for SQL as well as Dataset API. With Spark SQL we can get more information about the structure of data as well as computation being performed. We can also use Spark SQL to read data from an existing Hive installation. Spark SQL can also be accessed by using JDBC/ODBC API as well as command line.

#### What is a DataFrame in Spark SQL?
A DataFrame in SparkSQL is a Dataset organized into names columns. It is conceptually like a table in SQL.In Java and Scala, a DataFrame is a represented by a DataSet of rows. We can create a DataFrame from an existing RDD, a Hive table or from other Spark data sources.

#### What is a Parquet file in Spark?
Apache Parquet is a columnar storage format that is available to any project in Hadoop ecosystem. Any data processing framework, data model or programming language can use it. It is a compressed, efficient and encoding format common to Hadoop system projects. Spark SQL supports both reading and writing of parquet files. Parquet files also automatically preserves the schema of the original data. During write operations, by default all columns in a parquet file are converted to nullable column.

#### What is the difference between Apache Spark and Apache Hadoop MapReduce?
Some of the main differences between Apache Spark and Hadoop MapReduce are follows:
+ Speed: Apache Spark is 10X to 100X faster than Hadoop due to its usage of in memory processing.
+ Memory: Apache Spark stores data in memory, whereas	Hadoop MapReduce stores data in hard disk.
+ RDD: Spark uses Resilient Distributed Dataset (RDD) that guarantee fault tolerance. Where Apache Hadoop uses replication of data in multiple copies to achieve fault tolerance.
+ Streaming: Apache Spark supports Streaming with very less administration. This makes it much easier to use than Hadoop for real-time stream processing.
+ API: Spark provides a versatile API that can be used with multiple data sources as well as languages. It is more extensible than the API provided by Apache Hadoop.

#### What are the main languages supported by Apache Spark?
Some of the main languages supported by Apache Spark are as follows:
+ Java: We can use JavaSparkContext object to work with Java in Spark.
+ Scala: To use Scala with Spark, we have to create SparkContext	object	in Scala.
+ Python: We also used SparkContext to work with Python in Spark.
+ R: We can use SparkR module to work with R language in Spark ecosystem.
+ SQL: We can also SparkSQL to work with SQL language in Spark.

#### What are the file systems supported by Spark?
Some of the popular file systems supported by Apache Spark are as follows:
+ HDFS
+ S3
+ Local File System
+ Cassandra
+ OpenStack Swift
+ MapR File System

#### What is a Spark Driver?
Spark Driver is a program that runs on the master node machine. It takes care of declaring any operation- Transformation or Action on a RDD. With Spark Driver was can keep track of all the operations on a Dataset. It can also be used to rebuild a RDD in Spark.

#### What is an RDD Lineage?
Resilient Distributed Dataset (RDD) Lineage is a graph of all the parent RDD of a RDD. Since Spark does not replicate data, it is possible to lose some data. In case some Dataset is lost, it is possible to use RDD Lineage to recreate the lost Dataset. Therefore RDD Lineage provides solution for better performance of Spark as well as it helps in building a resilient system.

#### What are the two main types of Vector in Spark?
There are two main types of Vector in Spark:
Dense Vector: A dense vector is backed by an array of double data type. This array contains the values.
E.g. {1.0 , 0.0, 3.0} Sparse Vector: A sparse vector is backed by two parallel arrays. One array is for indices and the other array is for values. E.g. {3, [0,2], [1.0,3.0]} In this array, the first element is the number of elements in vector. Second element is the array of indices of non-zero values. Third element is the array of non-zero values.

#### What are the different deployment modes of Apache Spark?
Some popular deployment modes of Apache Spark are as follows:
+ Amazon EC2: We can use AWS cloud product Elastic Compute Cloud (EC2) to deploy and run a Spark cluster.
+ Mesos: We can deploy a Spark application in a private cluster by using Apache Mesos.
+ YARN: We can also deploy Spark on Apache YARN (Hadoop NextGen)
+ Standalone: This is the mode in which we can start Spark by hand. We can launch standalone cluster manually.

#### What is lazy evaluation in Apache Spark?
Apache Spark uses lazy evaluation as a performance optimization technique. In Laze evaluation as transformation is not applied immediately to a RDD. Spark records the transformations that have to be applied to a RDD. Once an Action is called, Spark executes all the transformations. Since Spark does not perform immediate execution based on transformation, it is	called lazy evaluation.

#### What are the core components of a distributed application in Apache Spark?
Core components of a distributed application in Apache Spark are as follows:
+ Cluster Manager: This is the component responsible for launching executors and drivers on multiple nodes. We can use different types of cluster managers based on our requirements. Some of the common types are Standalone, YARN, Mesos etc.
+ Driver: This is the main program in Spark that runs the main() function of an application. A Driver program creates the SparkConetxt.	Driver program listens and accepts incoming connections from its executors. Driver program can schedule tasks on the cluster. It runs closer to worker nodes.
+ Executor: This is a process on worker node. It is launched on the node to run an application. It can run tasks and use data in memory or disk storage to perform the task.

#### What is the difference in cache() and persist() methods in Apache Spark?
Both cache() and persist() functions are used for persisting a RDD in memory across operations. The key difference between persist() and cache() is that in persist() we can specify the Storage level that we select for persisting. Where as in cache(), default strategy is used for persisting. The default storage strategy is MEMORY_ONLY.

#### How will you remove data from cache in Apache Spark?
In general, Apache Spark automatically removes the unused objects from cache. It uses Least Recently Used (LRU) algorithm to drop old partitions. There are automatic monitoring mechanisms in Spark to monitor cache usage on each node. In case   we   want   to   forcibly remove an object from cache in Apache Spark, we can use RDD.unpersist() method.

#### What is the use of SparkContext in Apache Spark?
SparkContext is the central object in Spark that coordinates different Spark applications in a cluster. In a cluster we can use SparkContext to connect to multiple Cluster Managers that allocate resources to multiple applications. For any Spark program we first create SparkContext object. We can access a cluster by using this object. To create a SparkContext object, we first create a SparkConf object. This object contains the configuration information of our application. In Spark Shell, by default we get a SparkContext for the shell.

#### Do we need HDFS for running Spark application?
This is a trick question. Spark supports multiple file-systems. Spark supports HDFS, HBase, local file system, S3, Cassandra etc. So HDFS is not the only file system for running Spark application.

#### What is Spark Streaming?
Spark Streaming is a very popular feature of Spark for processing live streams with a large amount of data. Spark Streaming uses Spark API to create a highly scalable, high throughput and fault tolerant system to handle live data streams. Spark Streaming supports ingestion of data from popular sources like- Kafka, Kinesis, Flume etc. We can apply popular functions like map, reduce, join etc on data processed through Spark Streams. The processed data can be written to a file system or sent to databases and live dashboards.

#### How does Spark Streaming work internally?
Spark Streams listen to live data streams from various sources. On receiving data, it is divided into small batches that can be handled by Spark engine. These small batches of data are processed by Spark Engine to generate another output stream of resultant data. Internally, Spark uses an abstraction called DStream or discretized stream. A DStream is a continuous stream of data. We can create DStream from Kafka, Flume, Kinesis etc. A DStream is nothing but a sequence of RDDs in Spark. We can apply transformations and actions on this sequence of RDDs to create further RDDs.

#### What is a Pipeline in Apache Spark?
Pipeline is a concept from Machine learning. It is a sequence of algorithms that are executed for processing and learning from data. Pipeline is similar to a workflow. There can be one or more stages in a Pipeline.

#### How does Pipeline work in Apache Spark?
A Pipeline is a sequence of stages. Each stage in Pipeline can be a Transformer or an Estimator. We run these stages in an order. Initially a DataFrame is passed as an input to Pipeline. This DataFrame keeps on transforming with each stage of Pipeline. Most of the time, Runtime checking is done on DataFrame passing through the Pipeline. We can also save a Pipeline to a disk. It can be re-read from disk a later point of time.

#### What is the difference between Transformer and Estimator in Apache Spark?
A Transformer is an abstraction for feature transformer and learned model. A Transformer implements transform() method. It converts one DataFrame to another DataFrame. It appends one or more columns to a DataFrame. In a feature transformer a DataFrame is the input and the output is a new DataFrame with a new mapped column. An Estimator is an abstraction for a learning algorithm that fits or trains on data. An Estimator implements fit() method. The fit() method takes a DataFrame as input and results in a Model.

#### What are the different types of Cluster Managers in Apache Spark?
Main types of Cluster Managers for Apache Spark are as follows:
+ Standalone: It is a simple cluster manager that is included with Spark. We can start Spark manually by hand in this mode.
+ Spark	on Mesos: In this mode, Mesos master replaces Spark master as the cluster manager. When driver creates a job, Mesos will determine which machine will handle the task.
+ Hadoop YARN: In this setup, Hadoop YARN is used in cluster. There are two modes in this setup. In cluster mode, Spark driver runs inside a master process managed by YARN on cluster. In client mode, the Spark driver runs in the client process and application master is used for requesting resources from YARN.

#### How will you minimize data transfer while working with Apache Spark?
Generally Shuffle operation in Spark leads to a large amount of data transfer. We can configure Spark Shuffle process for optimum data transfer. Some of the main points are as follows:
+ spark.shuffle.compress: This configuration can be set to true to compress map output files. This reduces the amount of data transfer due to compression.
+ ByKey operations: We can minimize the use of ByKey operations to minimize the shuffle calls.

#### What is the main use of MLib in Apache Spark?
MLib is a machine-learning library in Apache Spark. Some of the main uses of MLib in Spark are as follows:
+ ML Algorithms: It contains Machine Learning algorithms such as classification, regression, clustering, and collaborative filtering. Featurization:
+ MLib provides algorithms to work with features. Some of these are	feature	extraction, transformation, dimensionality		reduction, and selection.
+ Pipelines: It contains tools for constructing, evaluating, and tuning ML Pipelines.
+ Persistence: It also provides methods for saving and load algorithms, models, and Pipelines.
+ Utilities: It contains utilities for linear algebra, statistics, data handling, etc.

#### What is the Checkpointing in Apache Spark?
In Spark Streaming, there is a concept of Checkpointing to add resiliency in the application. In case of a failure, a streaming application needs a checkpoint to recover. Due to this Spark provides Checkpointing. There are two types of Checkpointing:
+ Metadata Checkpointing: Metadata is the configuration information and other information that defines a Streaming application. We can create a Metadata checkpoint for a node to recover from the failure while running the driver application.		Metadata includes	configuration, DStream operations and incomplete batches etc.
+ Data Checkpointing: In this checkpoint we save RDD to a reliable storage. This is useful	in stateful transformations where generated RDD depends on RDD   of   previous   batch. There can be a long chain of RDDs in some cases. To avoid such a large recovery time, it is easier to create Data Checkpoint with RDDs at intermediate steps.

#### What is an Accumulator in Apache Spark?
An Accumulator is a variable in Spark that can be added only through an associative and commutative operation. An Accumulator can be supported in parallel. It is generally used to implement a counter or cumulative sum. We can create numeric type Accumulators by default in Spark.An Accumulator variable can be named as well as unnamed.

#### What is a Broadcast variable in Apache Spark?
As per Spark online documentation, “A Broadcast variable allows a programmer to keep a read-only variable cached on each machine rather than shipping a copy of it with tasks.” Spark can also distribute broadcast variable with an efficient broadcast algorithm to reduce communication cost. In Shuffle operations, there is a need of common data. This common data is broadcast by Spark as a Broadcast variable. The data in these variables is serialized and de-serialized before running a task.
We can	use SparkContext.broadcast(v) to create a broadcast variable. It is recommended that we should use broadcast variable in place of original variable for running a function on cluster.

#### What is Structured Streaming in Apache Spark?
Structured Streaming is a new feature in Spark 2.1. It is a scalable and fault-tolerant stream- processing engine. It is built on Spark SQL engine. We can use Dataset or DataFrame API to express streaming aggregations, event-time windows etc. The computations are done on the optimized Spark SQL engine.

#### How will you pass functions to Apache Spark?
In Spark API, we pass functions to driver program so that it can be run on a cluster. Two common ways to pass functions in Spark are as follows:
+ Anonymous	Function Syntax: This is used for passing short pieces of code in an anonymous function.
+ Static	Methods in a Singleton object: We can also define static methods in an object with only once instance i.e. Singleton. This object along with its methods can be passed to cluster nodes.

#### What is a Property Graph?
A Property Graph is a directed multigraph. We can attach an object on each vertex and edge of a Property Graph.In a directed multigraph, we can have multiple parallel edges that share same source and destination vertex. During modeling the data, the option of parallel edges helps in creating multiple relationships between same pair of vertices. E.g. Two persons can have two relationships Boss as well as Mentor.

#### What is Neighborhood Aggregation in Spark?
Neighborhood Aggregation is a concept in Graph module of Spark. It refers to the task of aggregating information	about	the neighborhood of each vertex. E.g. We want to know the number of books referenced in a book. Or number of times a Tweet is retweeted. This concept is used in iterative graph algorithms. Some of the popular uses of this concept are in Page Rank, Shortest Path etc.
We can use aggregateMessages[] and mergeMsg[] operations in Spark for implementing Neighborhood Aggregation.

#### What are different Persistence levels in Apache Spark?
Different Persistence levels in Apache Spark are as follows:
+ MEMORY_ONLY: In this level, RDD object is stored as a de-serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be recomputed.
+ MEMORY_AND_DISK: In this level, RDD object is stored as a de-serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be stored on the Disk.
+ MEMORY_ONLY_SER: In this level, RDD object is stored as a serialized Java object in JVM. It is more efficient than de-serialized object.
+ MEMORY_AND_DISK_SE In this level, RDD object is stored as a serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be stored on the Disk.
+ DISK_ONLY: In this level, RDD object is stored only on Disk.

#### How will you select the storage level in Apache Spark?
We use storage level to maintain balance between CPU efficiency and Memory usage. If our RDD objects fit in memory, we use MEMORY_ONLY option. In this option, the performance is very good due to objects being in Memory only. In case our RDD objects cannot fit in memory, we go for MEMORY_ONLY_SER option and select a serialization library that can provide space savings with serialization. This option is also quite fast in performance. In case our RDD object cannot fit in memory with a big gap in memory vs. total object size, we go for MEMORY_AND_DISK option. In this option some RDD object are stored on Disk. For fast fault recovery we use replication of objects to multiple partitions.

#### What are the options in Spark to create a Graph?
We can create a Graph in Spark from a collection of vertices and edges. Some of the options in Spark to create a Graph are as follows:
+ Graph.apply: This is the simplest option to create graph. We use this option to create a graph from RDDs of vertices and edges.
+ Graph.fromEdges: We can also create a graph from RDD of edges. In this option, vertices are created automatically and a default value is assigned to each vertex.
+ Graph.fromEdgeTuples: We can also create a graph from only an RDD of tuples.

#### What are the basic Graph operators in Spark?
Some common Graph operators in Apache Spark are as follows:
+ numEdges
+ numVertices
+ inDegrees
+ outDegrees
+ degrees
+ vertices
+ edges
+ persist
+ cache
+ unpersistVertices
+ partitionBy

#### What is the partitioning approach used in GraphX of Apache Spark?
GraphX uses Vertex-cut approach to distributed graph partitioning. In this approach, a graph is not split along edges. Rather we partition graph along vertices. These vertices can span on multiple machines. This approach reduces communication and storage overheads. Edges are assigned to different partitions based on the partition strategy that we select.

#### What is RDD?
RDD (Resilient Distribution Datasets) is a fault-tolerant collection of operational elements that run parallel. The partitioned data in RDD is immutable and distributed.

#### Name the different types of RDD
There are primarily two types of RDD – parallelized collection and Hadoop datasets.

#### What are the methods of creating RDDs in Spark?
There are two methods :
+ By paralleling a collection in your Driver program.
+ By loading an external dataset from external storage like HDFS, HBase, shared file system.

#### What is a Sparse Vector?
A sparse vector has two parallel arrays –one for indices and the other for values.

#### What are the languages supported by Apache Spark and which is the most popular one, What is JDBC and why it is popular?
There are four languages supported by Apache Spark – Scala, Java, Python, and R. Scala is the most popular one.
**Java Database Connectivity (JDBC)** is an application programming interface (API) that defines database connections in Java environments. Spark is written in Scala, which runs on the Java Virtual Machine (JVM). This makes JDBC the preferred method for connecting to data whenever possible. Hadoop, Hive, and MySQL all run on Java and easily interface with Spark clusters.
Databases are advanced technologies that benefit from decades of research and development. To leverage the inherent efficiencies of database engines, Spark uses an optimization called predicate pushdown. Predicate pushdown uses the database itself to handle certain parts of a query (the predicates). In mathematics and functional programming, a predicate is anything that returns a Boolean. In SQL terms, this often refers to the WHERE clause. Since the database is filtering data before it arrives on the Spark cluster, there less data transfer across the network and fewer records for Spark to process. Spark's Catalyst Optimizer includes predicate pushdown communicated through the JDBC API, making JDBC an ideal data source for Spark workloads.

#### What is Yarn?
Yarn is one of the key features in Spark, providing a central and resource management platform to deliver scalable operations across the cluster.

#### Do you need to install Spark on all nodes of Yarn cluster? Why?
No, because Spark runs on top of Yarn.

#### Is it possible to run Apache Spark on Apache Mesos?
Yes.

#### What is lineage graph?
The RDDs in Spark, depend on one or more other RDDs. The representation of dependencies in between RDDs is known as the lineage graph.

#### Define Partitions in Apache Spark
Partition is a smaller and logical division of data similar to split in MapReduce. It is a logical chunk of a large distributed data set. Partitioning is the process to derive logical units of data to speed up the processing process.

#### What is a DStream?
Discretized Stream (DStream) is a sequence of Resilient Distributed Databases that represent a stream of data.

#### What is a Catalyst framework?
Catalyst framework is an optimization framework present in Spark SQL. It allows Spark to automatically transform SQL queries by adding new optimizations to build a faster processing system.

#### What are Actions in Spark?
An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations.

#### What is a Parquet file?
Parquet is a columnar format file supported by many other data processing systems.

#### What is GraphX?
Spark uses GraphX for graph processing to build and transform interactive graphs.

#### What file systems does Spark support?
Hadoop distributed file system (HDFS), local file system, and Amazon S3.

#### What are the different types of transformations on DStreams? Explain.
+ Stateless Transformations – Processing of the batch does not depend on the output of the previous batch. Examples – map (), reduceByKey (), filter ().
+ Stateful Transformations – Processing of the batch depends on the intermediary results of the previous batch. Examples –Transformations that depend on sliding windows.

#### What is the difference between persist () and cache ()?
Persist () allows the user to specify the storage level whereas cache () uses the default storage level.

#### What do you understand by SchemaRDD?
SchemaRDD is an RDD that consists of row objects (wrappers around the basic string or integer arrays) with schema information about the type of data in each column.
These are some popular questions asked in an Apache Spark interview. Always be prepared to answer all types of questions — technical skills, interpersonal, leadership or methodology. If you are someone who has recently started your career in big data, you can always get certified in Apache Spark to get the techniques and skills required to be an expert in the field.

#### What is Apache Spark?
Spark is a fast, easy-to-use and flexible data processing framework. It has an advanced execution engine supporting cyclic data  flow and in-memory computing. Spark can run on Hadoop, standalone or in the cloud and is capable of accessing diverse data sources including HDFS, HBase, Cassandra and others.

#### Explain key features of Spark.
Allows Integration with Hadoop and files included in HDFS.
Spark has an interactive language shell as it has an independent Scala (the language in which Spark is written) interpreter.
Spark consists of RDD’s (Resilient Distributed Datasets), which can be cached across computing nodes in a cluster.
Spark supports multiple analytic tools that are used for interactive query analysis , real-time analysis and graph      processing

#### Define RDD?
RDD is the acronym for Resilient Distribution Datasets – a fault-tolerant collection of operational elements that run parallel. The partitioned data in RDD is immutable and distributed. There are primarily two types of RDD:
+ Parallelized Collections : The existing RDD’s running parallel with one another.
+ Hadoop datasets : perform function on each file record in HDFS or other storage system

#### What does a Spark Engine do?
Spark Engine is responsible for scheduling, distributing and monitoring the data application across the cluster.

#### Define Partitions?
As the name suggests, partition is a smaller and logical division of data  similar to split in MapReduce. Partitioning is the process to derive logical units of data to speed up the processing process. Everything in Spark is a partitioned RDD.

#### What do you understand by Transformations in Spark?
Transformations are functions applied on RDD, resulting into another RDD. It does not execute until an action occurs. map() and filer() are examples of transformations, where the former applies the function passed to it on each element of RDD and results into another RDD. The filter() creates a new RDD by selecting elements form current RDD that pass function argument.

#### Define Actions.
An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations. reduce() is an action that implements the function passed again and again until one value if left. take() action takes all the values from RDD to local node.

#### Define functions of SparkCore?
Serving as the base engine, SparkCore performs various important functions like memory management, monitoring jobs, fault-tolerance, job scheduling and interaction with storage systems.

#### What is RDD Lineage?
Spark does not support data replication in the memory and thus, if any data is lost, it is rebuild using RDD lineage. RDD lineage is a process that reconstructs lost data partitions. The best is that RDD always remembers how to build from other datasets.

#### What is Spark Driver?
Spark Driver is the program that runs on the master node of the machine and declares transformations and actions on data RDDs. In simple terms, driver in Spark creates SparkContext, connected to a given Spark Master.
The driver also delivers the RDD graphs to Master, where the standalone cluster manager runs.

#### What is Hive on Spark?
Hive contains significant support for Apache Spark, wherein Hive execution is configured to Spark:
hive> set spark.home=/location/to/sparkHome;
hive> set hive.execution.engine=spark;

Name commonly-used Spark Ecosystems.
+ Spark SQL (Shark)- for developers.
+ Spark Streaming for processing live data streams.
+ GraphX for generating and computing graphs.
+ MLlib (Machine Learning Algorithms).
+ SparkR to promote R Programming in Spark engine.

#### Define Spark Streaming.
Spark supports stream processing – an extension to the Spark API , allowing stream processing of live data streams. The data from different sources like Flume, HDFS is streamed and finally processed to file systems, live dashboards and databases. It is similar to batch processing as the input data is divided into streams like batches.

#### What is Spark SQL?
SQL Spark, better known as Shark is a novel module introduced in Spark to work with structured data and perform structured data processing. Through this module, Spark executes relational SQL queries on the data. The core of the component supports an altogether different RDD called SchemaRDD, composed of rows objects and schema objects defining data type of each column in the row. It is similar to a table in relational database.

#### List the functions of Spark SQL?
Spark SQL is capable of:
+ Loading data from a variety of structured sources.
+ Querying data using SQL statements, both inside a Spark program and from external tools that connect to Spark SQL through standard database connectors (JDBC/ODBC). For instance, using business intelligence tools like Tableau.
+ Providing rich integration between SQL and regular Python/Java/Scala code, including the ability to join RDDs and SQL tables, expose custom functions in SQL, and more.

#### What are benefits of Spark over MapReduce?
Due to the availability of in-memory processing, Spark implements the processing around 10-100x faster than Hadoop MapReduce. MapReduce makes use of persistence storage for any of the data processing tasks.
Unlike Hadoop, Spark provides in-built libraries to perform multiple tasks form the same core like batch processing, Steaming, Machine learning, Interactive SQL queries. However, Hadoop only supports batch processing.
Hadoop is highly disk-dependent whereas Spark promotes caching and in-memory data storage.
Spark is capable of performing computations multiple times on the same dataset. This is called iterative computation while there is no iterative computing implemented by Hadoop.

#### What is Spark Executor?
When SparkContext connect to a cluster manager, it acquires an Executor on nodes in the cluster. Executors are Spark processes that run computations and store the data on the worker node. The final tasks by SparkContext are transferred to executors for their execution.

#### What do you understand by worker node?
Worker node refers to any node that can run the application code in a cluster.

#### Illustrate some demerits of using Spark.
Since Spark utilizes more storage space compared to Hadoop and MapReduce, there may arise certain problems. Developers need to be careful while running their applications in Spark. Instead of running everything on a single node, the work must be distributed over multiple clusters.

#### What is the advantage of a Parquet file?
Parquet file is a columnar format file that helps :
+ Limit I/O operations
+ Consumes less space
+ Fetches only required columns.

#### What are different o/p methods to get result?
+ collect()
+ show()
+ take()
+ foreach(println)

#### What are two ways to attain a schema from data?
Allow Spark to infer a schema from your data or provide a user defined schema. Schema inference is the recommended first step; however, you can customize this schema to your use case with a user defined schema.

Providing a schema increases performance two to three times, depending on the size of the cluster used. Since Spark doesn't infer the schema, it doesn't have to read through all of the data. This is also why  there are fewer jobs when a schema is provided: Spark doesn't need one job for each partition of the data to infer the schema.

#### Why should you define your own schema?
Benefits of user defined schemas include:
-   Avoiding the extra scan of your data needed to infer the schema
-   Providing alternative data types
-   Parsing only the fields you need

#### Why is JSON a common format in big data pipelines?
Semi-structured data works well with hierarchical data and where schemas need to evolve over time. It also easily contains composite data types such as arrays and maps.

#### By default, how are corrupt records dealt with using  spark.read.json()?
They appear in a column called  _corrupt_record. These are the records that Spark can't read (e.g. when characters are missing from a JSON string).

#### Explain the key features of Apache Spark.
+ Polyglot: Spark provides high-level APIs in Java, Scala, Python and R. Spark code can be written in any of these four languages. It provides a shell in Scala and Python. The Scala shell can be accessed through ./bin/spark-shell and Python shell through ./bin/pyspark from the installed directory.
+ Speed: Spark runs upto 100 times faster than Hadoop MapReduce for large-scale data processing. Spark is able to achieve this speed through controlled partitioning. It manages data using partitions that help parallelize distributed data processing with minimal network traffic.
+ Multiple Formats: Spark supports multiple data sources such as Parquet, JSON, Hive and Cassandra. The Data Sources API provides a pluggable mechanism for accessing structured data though Spark SQL. Data sources can be more than just simple pipes that convert data and pull it into Spark.
+ Lazy Evaluation: Apache Spark delays its evaluation till it is absolutely necessary. This is one of the key factors contributing to its speed. For transformations, Spark adds them to a DAG of computation and only when the driver requests some data, does this DAG actually gets executed.
+ Real Time Computation: Spark’s computation is real-time and has less latency because of its in-memory computation. Spark is designed for massive scalability and the Spark team has documented users of the system running production clusters with thousands of nodes and supports several computational models.
+ Hadoop Integration: Apache Spark provides smooth compatibility with Hadoop. This is a great boon for all the Big Data engineers who started their careers with Hadoop. Spark is a potential replacement for the MapReduce functions of Hadoop, while Spark has the ability to run on top of an existing Hadoop cluster using YARN for resource scheduling.
+ Machine Learning: Spark’s MLlib is the machine learning component which is handy when it comes to big data processing. It eradicates the need to use multiple tools, one for processing and one for machine learning. Spark provides data engineers and data scientists with a powerful, unified engine that is both fast and easy to use.

#### What are benefits of Spark over MapReduce?
Spark has the following benefits over MapReduce:
Due to the availability of in-memory processing, Spark implements the processing around 10 to 100 times faster than Hadoop MapReduce whereas MapReduce makes use of persistence storage for any of the data processing tasks.
Unlike Hadoop, Spark provides inbuilt libraries to perform multiple tasks from the same core like batch processing, Steaming, Machine learning, Interactive SQL queries. However, Hadoop only supports batch processing.
Hadoop is highly disk-dependent whereas Spark promotes caching and in-memory data storage.
Spark is capable of performing computations multiple times on the same dataset. This is called iterative computation while there is no iterative computing implemented by Hadoop.

#### What is YARN?
Similar to Hadoop, YARN is one of the key features in Spark, providing a central and resource management platform to deliver scalable operations across the cluster. YARN is a distributed container manager, like Mesos for example, whereas Spark is a data processing tool. Spark can run on YARN, the same way Hadoop Map Reduce can run on YARN. Running Spark on YARN necessitates a binary distribution of Spark as built on YARN support.

#### Do you need to install Spark on all nodes of YARN cluster?
No, because Spark runs on top of YARN. Spark runs independently from its installation. Spark has some options to use YARN when dispatching jobs to the cluster, rather than its own built-in manager, or Mesos. Further, there are some configurations to run YARN. They include master, deploy-mode, driver-memory, executor-memory, executor-cores, and queue.

#### Is there any benefit of learning MapReduce if Spark is better than MapReduce?
Yes, MapReduce is a paradigm used by many big data tools including Spark as well. It is extremely relevant to use MapReduce when the data grows bigger and bigger. Most tools like Pig and Hive convert their queries into MapReduce phases to optimize them better.

#### Explain the concept of Resilient Distributed Dataset (RDD).
RDD stands for Resilient Distribution Datasets. An RDD is a fault-tolerant collection of operational elements that run in parallel. The partitioned data in RDD is immutable and distributed in nature. There are primarily two types of RDD:
+ Parallelized Collections: Here, the existing RDDs running parallel with one another.
+ Hadoop Datasets: They perform functions on each file record in HDFS or other storage systems.
+ RDDs are basically parts of data that are stored in the memory distributed across many nodes. RDDs are lazily evaluated in Spark. This lazy evaluation is what contributes to Spark’s speed.

#### How do we create RDDs in Spark?
Spark provides two methods to create RDD:
1. By parallelizing a collection in your Driver program.
2. This makes use of SparkContext’s parallelize
3. By loading an external dataset from external storage like HDFS, HBase, shared file system.

#### What is Executor Memory in a Spark application?
Every spark application has same fixed heap size and fixed number of cores for a spark executor. The heap size is what referred to as the Spark executor memory which is controlled with the spark.executor.memory property of the –executor-memory flag. Every spark application will have one executor on each worker node. The executor memory is basically a measure on how much memory of the worker node will the application utilize.

#### Define Partitions in Apache Spark.
As the name suggests, partition is a smaller and logical division of data similar to split in MapReduce. It is a logical chunk of a large distributed data set. Partitioning is the process to derive logical units of data to speed up the processing process. Spark manages data using partitions that help parallelize distributed data processing with minimal network traffic for sending data between executors. By default, Spark tries to read data into an RDD from the nodes that are close to it. Since Spark usually accesses distributed partitioned data, to optimize transformation operations it creates partitions to hold the data chunks. Everything in Spark is a partitioned RDD.

#### What operations does RDD support?
RDD (Resilient Distributed Dataset) is main logical data unit in Spark. An RDD has distributed a collection of objects. Distributed means, each RDD is divided into multiple partitions. Each of these partitions can reside in memory or stored on the disk of different machines in a cluster. RDDs are immutable (Read Only) data structure. You can’t change original RDD, but you can always transform it into different RDD with all changes you want.
RDDs support two types of operations: transformations and actions.
Transformations: Transformations create new RDD from existing RDD like map, reduceByKey and filter we just saw. Transformations are executed on demand. That means they are computed lazily.
Actions: Actions return final results of RDD computations. Actions triggers execution using lineage graph to load the data into original RDD, carry out all intermediate transformations and return final results to Driver program or write it out to file system.

#### What do you understand by Transformations in Spark?
Transformations are functions applied on RDD, resulting into another RDD. It does not execute until an action occurs. map() and filter() are examples of transformations, where the former applies the function passed to it on each element of RDD and results into another RDD. The filter() creates a new RDD by selecting elements from current RDD that pass function argument.
val rawData=sc.textFile("path to/movies.txt")
val moviesData=rawData.map(x=>x.split("  "))
As we can see here, rawData RDD is transformed into moviesData RDD. Transformations are lazily evaluated.

#### Define Actions in Spark.
An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations. Actions triggers execution using lineage graph to load the data into original RDD, carry out all intermediate transformations and return final results to Driver program or write it out to file system.
reduce() is an action that implements the function passed again and again until one value if left. take() action takes all the values from RDD to a local node.
moviesData.saveAsTextFile(“MoviesData.txt”)
As we can see here, moviesData RDD is saved into a text file called MoviesData.txt.

#### Define functions of SparkCore.
Spark Core is the base engine for large-scale parallel and distributed data processing. The core is the distributed execution engine and the Java, Scala, and Python APIs offer a platform for distributed ETL application development. SparkCore performs various important functions like memory management, monitoring jobs, fault-tolerance, job scheduling and interaction with storage systems. Further, additional libraries, built atop the core allow diverse workloads for streaming, SQL, and machine learning. It is responsible for:

#### Memory management and fault recovery
Scheduling, distributing and monitoring jobs on a cluster Interacting with storage systems

#### What do you understand by Pair RDD?
Apache defines PairRDD functions class as class PairRDDFunctions[K, V] extends Logging with HadoopMapReduceUtil with Serializable
Special operations can be performed on RDDs in Spark using key/value pairs and such RDDs are referred to as Pair RDDs. Pair RDDs allow users to access each key in parallel. They have a reduceByKey() method that collects data based on each key and a join() method that combines different RDDs together, based on the elements having the same key.

#### How is Streaming implemented in Spark? Explain with examples.
Spark Streaming is used for processing real-time streaming data. Thus it is a useful addition to the core Spark API. It enables high-throughput and fault-tolerant stream processing of live data streams. The fundamental stream unit is DStream which is basically a series of RDDs (Resilient Distributed Datasets) to process the real-time data. The data from different sources like Flume, HDFS is streamed and finally processed to file systems, live dashboards and databases. It is similar to batch processing as the input data is divided into streams like batches.

#### Is there an API for implementing graphs in Spark?
GraphX is the Spark API for graphs and graph-parallel computation. Thus, it extends the Spark RDD with a Resilient Distributed Property Graph.
The property graph is a directed multi-graph which can have multiple edges in parallel. Every edge and vertex have user defined properties associated with it. Here, the parallel edges allow multiple relationships between the same vertices. At a high-level, GraphX extends the Spark RDD abstraction by introducing the Resilient Distributed Property Graph: a directed multigraph with properties attached to each vertex and edge.
To support graph computation, GraphX exposes a set of fundamental operators (e.g., subgraph, joinVertices, and mapReduceTriplets) as well as an optimized variant of the Pregel API. In addition, GraphX includes a growing collection of graph algorithms and builders to simplify graph analytics tasks.

#### What is PageRank in GraphX?
PageRank measures the importance of each vertex in a graph, assuming an edge from u to v represents an endorsement of v’s importance by u. For example, if a Twitter user is followed by many others, the user will be ranked highly.
GraphX comes with static and dynamic implementations of PageRank as methods on the PageRank Object. Static PageRank runs for a fixed number of iterations, while dynamic PageRank runs until the ranks converge (i.e., stop changing by more than a specified tolerance). GraphOps allows calling these algorithms directly as methods on Graph.

#### How is machine learning implemented in Spark?
MLlib is scalable machine learning library provided by Spark. It aims at making machine learning easy and scalable with common learning algorithms and use cases like clustering, regression filtering, dimensional reduction, and alike.

#### Is there a module to implement SQL in Spark? How does it work?
Spark SQL is a new module in Spark which integrates relational processing with Spark’s functional programming API. It supports querying data either via SQL or via the Hive Query Language. For those of you familiar with RDBMS, Spark SQL will be an easy transition from your earlier tools where you can extend the boundaries of traditional relational data processing.
Spark SQL integrates relational processing with Spark’s functional programming. Further, it provides support for various data sources and makes it possible to weave SQL queries with code transformations thus resulting in a very powerful tool.
The following are the four libraries of Spark SQL.
+ Data Source API
+ DataFrame API
+ Interpreter & Optimizer
+ SQL Service

#### What are receivers in Apache Spark Streaming?
Receivers are those entities that consume data from different data sources and then move them to Spark for processing. They are created by using streaming contexts in the form of long-running tasks that are scheduled for operating in a round-robin fashion. Each receiver is configured to use up only a single core. The receivers are made to run on various executors to accomplish the task of data streaming. There are two types of receivers depending on how the data is sent to Spark:
+ Reliable receivers: Here, the receiver sends an acknowledegment to the data sources post successful reception of data and its replication on the Spark storage space.
+ Unreliable receiver: Here, there is no acknowledgement sent to the data sources.

+ What is the difference between repartition and coalesce?
+ Repartition
    + Usage repartition can increase/decrease the number of data partitions.
    + Repartition creates new data partitions and performs a full shuffle of evenly distributed data.
    + Repartition internally calls coalesce with shuffle parameter thereby making it slower than coalesce.

+ Coalesce
    + Spark coalesce can only reduce the number of data partitions.
    + Coalesce makes use of already existing partitions to reduce the amount of shuffled data unevenly.
    + Coalesce is faster than repartition. However, if there are unequal-sized data partitions, the speed might be slightly slower.
+ What are the data formats supported by Spark?
  Spark supports both the raw files and the structured file formats for efficient reading and processing. File formats like paraquet, JSON, XML, CSV, RC, Avro, TSV, etc are supported by Spark.

#### What do you understand by Shuffling in Spark?
The process of redistribution of data across different partitions which might or might not cause data movement across the JVM processes or the executors on the separate machines is known as shuffling/repartitioning. Partition is nothing but a smaller logical division of data.
It is to be noted that Spark has no control over what partition the data gets distributed across.

#### How is Apache Spark different from MapReduce?
+ MapReduce
    + MapReduce does only batch-wise processing of data.
    + MapReduce does slow processing of large data.
    + MapReduce stores data in HDFS (Hadoop Distributed File System) which makes it take a long time to get the data.
    + MapReduce highly depends on disk which makes it to be a high latency framework.
    + MapReduce requires an external scheduler for jobs.

+ Apache Spark
    + Apache Spark can process the data both in real-time and in batches.
    + Apache Spark runs approximately 100 times faster than MapReduce for big data processing.
    + Spark stores data in memory (RAM) which makes it easier and faster to retrieve data when needed.
    + Spark supports in-memory data storage and caching and makes it a low latency computation framework.
    + Spark has its own job scheduler due to the in-memory data computation.

#### Explain the working of Spark with the help of its architecture.
Spark applications are run in the form of independent processes that are well coordinated by the Driver program by means of a SparkSession object. The cluster manager or the resource manager entity of Spark assigns the tasks of running the Spark jobs to the worker nodes as per one task per partition principle. There are various iterations algorithms that are repeatedly applied to the data to cache the datasets across various iterations. Every task applies its unit of operations to the dataset within its partition and results in the new partitioned dataset. These results are sent back to the main driver application for further processing or to store the data on the disk. The following diagram illustrates this working as described above:

#### What is the working of DAG in Spark?
DAG stands for Direct Acyclic Graph which has a set of finite vertices and edges. The vertices represent RDDs and the edges represent the operations to be performed on RDDs sequentially. The DAG created is submitted to the DAG Scheduler which splits the graphs into stages of tasks based on the transformations applied to the data. The stage view has the details of the RDDs of that stage.
The working of DAG in spark is defined as per the workflow diagram below:
The first task is to interpret the code with the help of an interpreter. If you use the Scala code, then the Scala interpreter interprets the code.
Spark then creates an operator graph when the code is entered in the Spark console.
When the action is called on Spark RDD, the operator graph is submitted to the DAG Scheduler.
The operators are divided into stages of task by the DAG Scheduler. The stage consists of detailed step-by-step operation on the input data. The operators are then pipelined together.
The stages are then passed to the Task Scheduler which launches the task via the cluster manager to work on independently without the dependencies between the stages.
The worker nodes then execute the task.
Each RDD keeps track of the pointer to one/more parent RDD along with its relationship with the parent. For example, consider the operation val childB=parentA.map() on RDD, then we have the RDD childB that keeps track of its parentA which is called RDD lineage.

#### Under what scenarios do you use Client and Cluster modes for deployment?
In case the client machines are not close to the cluster, then the Cluster mode should be used for deployment. This is done to avoid the network latency caused while communication between the executors which would occur in the Client mode. Also, in Client mode, the entire process is lost if the machine goes offline.
If we have the client machine inside the cluster, then the Client mode can be used for deployment. Since the machine is inside the cluster, there won’t be issues of network latency and since the maintenance of the cluster is already handled, there is no cause of worry in cases of failure.

#### What is Spark Streaming and how is it implemented in Spark?
Spark Streaming is one of the most important features provided by Spark. It is nothing but a Spark API extension for supporting stream processing of data from different sources.
Data from sources like Kafka, Kinesis, Flume, etc are processed and pushed to various destinations like databases, dashboards, machine learning APIs, or as simple as file systems. The data is divided into various streams (similar to batches) and is processed accordingly.
Spark streaming supports highly scalable, fault-tolerant continuous stream processing which is mostly used in cases like fraud detection, website monitoring, website click baits, IoT (Internet of Things) sensors, etc.
Spark Streaming first divides the data from the data stream into batches of X seconds which are called Dstreams or Discretized Streams. They are internally nothing but a sequence of multiple RDDs. The Spark application does the task of processing these RDDs using various Spark APIs and the results of this processing are again returned as batches. The following diagram explains the workflow of the spark streaming process.

#### What can you say about Spark Datasets?
Spark Datasets are those data structures of SparkSQL that provide JVM objects with all the benefits (such as data manipulation using lambda functions) of RDDs alongside Spark SQL-optimised execution engine. This was introduced as part of Spark since version 1.6.
Spark datasets are strongly typed structures that represent the structured queries along with their encoders.
They provide type safety to the data and also give an object-oriented programming interface.
The datasets are more structured and have the lazy query expression which helps in triggering the action. Datasets have the combined powers of both RDD and Dataframes. Internally, each dataset symbolizes a logical plan which informs the computational query about the need for data production. Once the logical plan is analyzed and resolved, then the physical query plan is formed that does the actual query execution.
Datasets have the following features:
Optimized Query feature: Spark datasets provide optimized queries using Tungsten and Catalyst Query Optimizer frameworks. The Catalyst Query Optimizer represents and manipulates a data flow graph (graph of expressions and relational operators). The Tungsten improves and optimizes the speed of execution of Spark job by emphasizing the hardware architecture of the Spark execution platform.
Compile-Time Analysis: Datasets have the flexibility of analyzing and checking the syntaxes at the compile-time which is not technically possible in RDDs or Dataframes or the regular SQL queries.
Interconvertible: The type-safe feature of datasets can be converted to “untyped” Dataframes by making use of the following methods provided by the Datasetholder:
toDS():Dataset[T]
toDF():DataFrame
toDF(columName:String*):DataFrame
Faster Computation: Datasets implementation are much faster than those of the RDDs which helps in increasing the system performance.
Persistent storage qualified: Since the datasets are both queryable and serializable, they can be easily stored in any persistent storages.
Less Memory Consumed: Spark uses the feature of caching to create a more optimal data layout. Hence, less memory is consumed.
Single Interface Multiple Languages: Single API is provided for both Java and Scala languages. These are widely used languages for using Apache Spark. This results in a lesser burden of using libraries for different types of inputs.

#### Define Spark DataFrames.
Spark Dataframes are the distributed collection of datasets organized into columns similar to SQL. It is equivalent to a table in the relational database and is mainly optimized for big data operations.
Dataframes can be created from an array of data from different data sources such as external databases, existing RDDs, Hive Tables, etc. Following are the features of Spark Dataframes:
Spark Dataframes have the ability of processing data in sizes ranging from Kilobytes to Petabytes on a single node to large clusters.
They support different data formats like CSV, Avro, elastic search, etc, and various storage systems like HDFS, Cassandra, MySQL, etc.
By making use of SparkSQL catalyst optimizer, state of art optimization is achieved.
It is possible to easily integrate Spark Dataframes with major Big Data tools using SparkCore.

#### Define Executor Memory in Spark
The applications developed in Spark have the same fixed cores count and fixed heap size defined for spark executors. The heap size refers to the memory of the Spark executor that is controlled by making use of the property spark.executor.memory that belongs to the -executor-memory flag. Every Spark applications have one allocated executor on each worker node it runs. The executor memory is a measure of the memory consumed by the worker node that the application utilizes.

#### What are the functions of SparkCore?
SparkCore is the main engine that is meant for large-scale distributed and parallel data processing. The Spark core consists of the distributed execution engine that offers various APIs in Java, Python, and Scala for developing distributed ETL applications.
Spark Core does important functions such as memory management, job monitoring, fault-tolerance, storage system interactions, job scheduling, and providing support for all the basic I/O functionalities. There are various additional libraries built on top of Spark Core which allows diverse workloads for SQL, streaming, and machine learning. They are responsible for:
Fault recovery
Memory management and Storage system interactions
Job monitoring, scheduling, and distribution
Basic I/O functions

#### What do you understand by worker node?
Worker nodes are those nodes that run the Spark application in a cluster. The Spark driver program listens for the incoming connections and accepts them from the executors addresses them to the worker nodes for execution. A worker node is like a slave node where it gets the work from its master node and actually executes them. The worker nodes do data processing and report the resources used to the master. The master decides what amount of resources needs to be allocated and then based on their availability, the tasks are scheduled for the worker nodes by the master.

#### What are some demerits of using Spark in applications?
Despite Spark being the powerful data processing engine, there are certain demerits to using Apache Spark in applications. Some of them are:

Spark makes use of more storage space when compared to MapReduce or Hadoop which may lead to certain memory-based problems.
Care must be taken by the developers while running the applications. The work should be distributed across multiple clusters instead of running everything on a single node.
Since Spark makes use of “in-memory” computations, they can be a bottleneck to cost-efficient big data processing.
While using files present on the path of the local filesystem, the files must be accessible at the same location on all the worker nodes when working on cluster mode as the task execution shuffles between various worker nodes based on the resource availabilities. The files need to be copied on all worker nodes or a separate network-mounted file-sharing system needs to be in place.
One of the biggest problems while using Spark is when using a large number of small files. When Spark is used with Hadoop, we know that HDFS gives a limited number of large files instead of a large number of small files. When there is a large number of small gzipped files, Spark needs to uncompress these files by keeping them on its memory and network. So large amount of time is spent in burning core capacities for unzipping the files in sequence and performing partitions of the resulting RDDs to get data in a manageable format which would require extensive shuffling overall. This impacts the performance of Spark as much time is spent preparing the data instead of processing them.
Spark doesn’t work well in multi-user environments as it is not capable of handling many users concurrently.

#### How can the data transfers be minimized while working with Spark?
Data transfers correspond to the process of shuffling. Minimizing these transfers results in faster and reliable running Spark applications. There are various ways in which these can be minimized. They are:
+ Usage of Broadcast Variables: Broadcast variables increases the efficiency of the join between large and small RDDs.
+ Usage of Accumulators: These help to update the variable values parallelly during execution.
  Another common way is to avoid the operations which trigger these reshuffles.

#### What is SchemaRDD in Spark RDD?
SchemaRDD is an RDD consisting of row objects that are wrappers around integer arrays or strings that has schema information regarding the data type of each column. They were designed to ease the lives of developers while debugging the code and while running unit test cases on the SparkSQL modules. They represent the description of the RDD which is similar to the schema of relational databases. SchemaRDD also provides the basic functionalities of the common RDDs along with some relational query interfaces of SparkSQL.
Consider an example. If you have an RDD named Person that represents a person’s data. Then SchemaRDD represents what data each row of Person RDD represents. If the Person has attributes like name and age, then they are represented in SchemaRDD.

#### What module is used for implementing SQL in Apache Spark?
Spark provides a powerful module called SparkSQL which performs relational data processing combined with the power of the functional programming feature of Spark. This module also supports either by means of SQL or Hive Query Language. It also provides support for different data sources and helps developers write powerful SQL queries using code transformations.
The four major libraries of SparkSQL are:
+ Data Source API
+ DataFrame API
+ Interpreter & Catalyst Optimizer
+ SQL Services
  Spark SQL supports the usage of structured and semi-structured data in the following ways:
+ Spark supports DataFrame abstraction in various languages like Python, Scala, and Java along with providing good optimization techniques.
+ SparkSQL supports data read and writes operations in various structured formats like JSON, Hive, Parquet, etc.
  S+ parkSQL allows data querying inside the Spark program and via external tools that do the JDBC/ODBC connections.

It is recommended to use SparkSQL inside the Spark applications as it empowers the developers to load the data, query the data from databases and write the results to the destination.

#### What are the steps to calculate the executor memory?
Consider you have the below details regarding the cluster:
Number of nodes = 10
Number of cores in each node = 15 cores
RAM of each node = 61GB
To identify the number of cores, we follow the approach:
Number of Cores = number of concurrent tasks that can be run parallelly by the executor. The optimal value as part of a general rule of thumb is 5.
Hence to calculate the number of executors, we follow the below approach:

Number of executors = Number of cores/Concurrent Task = 15/5 = 3
Number of executors = Number of nodes * Number of executor in each node = 10 * 3 = 30 executors per Spark job

#### Why do we need broadcast variables in Spark?
Broadcast variables let the developers maintain read-only variables cached on each machine instead of shipping a copy of it with tasks. They are used to give every node copy of a large input dataset efficiently. These variables are broadcasted to the nodes using different algorithms to reduce the cost of communication.
Differentiate between Spark Datasets, Dataframes and RDDs.
Criteria	Spark Datasets	Spark Dataframes	Spark RDDs
Representation of Data	Spark Datasets is a combination of Dataframes and RDDs with features like static type safety and object-oriented interfaces.	Spark Dataframe is a distributed collection of data that is organized into named columns.	Spark RDDs are a distributed collection of data without schema.
Optimization	Datasets make use of catalyst optimizers for optimization.	Dataframes also makes use of catalyst optimizer for optimization.	There is no built-in optimization engine.
Schema Projection	Datasets find out schema automatically using SQL Engine.	Dataframes also find the schema automatically.	Schema needs to be defined manually in RDDs.
Aggregation Speed	Dataset aggregation is faster than RDD but slower than Dataframes.	Aggregations are faster in Dataframes due to the provision of easy and powerful APIs.	RDDs are slower than both the Dataframes and the Datasets while performing even simple operations like data grouping.

#### Can Apache Spark be used along with Hadoop? If yes, then how?
Yes! The main feature of Spark is its compatibility with Hadoop. This makes it a powerful framework as using the combination of these two helps to leverage the processing capacity of Spark by making use of the best of Hadoop’s YARN and HDFS features.
Hadoop can be integrated with Spark in the following ways:
HDFS: Spark can be configured to run atop HDFS to leverage the feature of distributed replicated storage.
MapReduce: Spark can also be configured to run alongside the MapReduce in the same or different processing framework or Hadoop cluster. Spark and MapReduce can be used together to perform real-time and batch processing respectively.
YARN: Spark applications can be configured to run on YARN which acts as the cluster management framework.

#### What are Sparse Vectors? How are they different from dense vectors?
Sparse vectors consist of two parallel arrays where one array is for storing indices and the other for storing values. These vectors are used to store non-zero values for saving space.

val sparseVec: Vector = Vectors.sparse(5, Array(0, 4), Array(1.0, 2.0))
In the above example, we have the vector of size 5, but the non-zero values are there only at indices 0 and 4.
Sparse vectors are particularly useful when there are very few non-zero values. If there are cases that have only a few zero values, then it is recommended to use dense vectors as usage of sparse vectors would introduce the overhead of indices which could impact the performance.
Dense vectors can be defines as follows:
val denseVec = Vectors.dense(4405d,260100d,400d,5.0,4.0,198.0,9070d,1.0,1.0,2.0,0.0)
Usage of sparse or dense vectors does not impact the results of calculations but when used inappropriately, they impact the memory consumed and the speed of calculation.

#### How are automatic clean-ups triggered in Spark for handling the accumulated metadata?
The clean-up tasks can be triggered automatically either by setting spark.cleaner.ttl parameter or by doing the batch-wise division of the long-running jobs and then writing the intermediary results on the disk.

#### How is Caching relevant in Spark Streaming?
Spark Streaming involves the division of data stream’s data into batches of X seconds called DStreams. These DStreams let the developers cache the data into the memory which can be very useful in case the data of DStream is used for multiple computations. The caching of data can be done using the cache() method or using persist() method by using appropriate persistence levels. The default persistence level value for input streams receiving data over the networks such as Kafka, Flume, etc is set to achieve data replication on 2 nodes to accomplish fault tolerance.
Caching using cache method:
val cacheDf = dframe.cache()
Caching using persist method:
val persistDf = dframe.persist(StorageLevel.MEMORY_ONLY)
The main advantages of caching are:
+ Cost efficiency: Since Spark computations are expensive, caching helps to achieve reusing of data and this leads to reuse computations which can save the cost of operations.
+ Time-efficient: The computation reusage leads to saving a lot of time.
+ More Jobs Achieved: By saving time of computation execution, the worker nodes can perform/execute more jobs.

#### Define Piping in Spark.
Apache Spark provides the pipe() method on RDDs which gives the opportunity to compose different parts of occupations that can utilize any language as needed as per the UNIX Standard Streams. Using the pipe() method, the RDD transformation can be written which can be used for reading each element of the RDD as String. These can be manipulated as required and the results can be displayed as String.

#### What API is used for Graph Implementation in Spark?
Spark provides a powerful API called GraphX that extends Spark RDD for supporting graphs and graph-based computations. The extended property of Spark RDD is called as Resilient Distributed Property Graph which is a directed multi-graph that has multiple parallel edges. Each edge and the vertex has associated user-defined properties. The presence of parallel edges indicates multiple relationships between the same set of vertices. GraphX has a set of operators such as subgraph, mapReduceTriplets, joinVertices, etc that can support graph computation. It also includes a large collection of graph builders and algorithms for simplifying tasks related to graph analytics.

#### How can you achieve machine learning in Spark?
Spark provides a very robust, scalable machine learning-based library called MLlib. This library aims at implementing easy and scalable common ML-based algorithms and has the features like classification, clustering, dimensional reduction, regression filtering, etc. More information about this library can be obtained in detail from Spark’s official documentation site here: https://spark.apache.org/docs/latest/ml-guide.html

#### What are the limitations of Spark?
Does not have its file management system. Thus, it needs to integrate with Hadoop or other cloud-based data platforms.
In-memory capability can become a bottleneck. Especially when it comes to cost-efficient processing of Bigdata.
Memory consumption is very high. And the issues for the same are not handled in a user-friendly manner. d. It requires large data.
MLlib lack in some available algorithms, for example, Tanimoto distance.
Read more Apache Spark Limitations in detail.

#### Compare Hadoop and Spark.
+ Cost Efficient – In Hadoop, during replication, a large number of servers, huge amount of storage, and the large data center is required. Thus, installing and using Apache Hadoop is expensive. While using Apache Spark is a cost effective solution for big data environment.
+ Performance – The basic idea behind Spark was to improve the performance of data processing. And Spark did this to 10x-100x times. And all the credit of faster processing in Spark goes to in-memory processing of data. In Hadoop, the data processing takes place in disc while in Spark the data processing takes place in memory. It moves to the disc only when needed. The Spark in-memory computation is beneficial for iterative algorithms. When it comes to performance, because of batch processing in Hadoop it’s processing is quite slow while the processing speed of Apache is faster as it supports micro-batching.
+ Ease of development – The core in Spark is the distributed execution engine. Various languages are supported by Apache Spark for distributed application development. For example, Java, Scala, Python, and R. On the top of spark core, various libraries are built that enables workload. they make use of streaming, SQL, graph and machine learning. Hadoop also supports some of these workloads but Spark eases the development by combining all into the same application. d. Failure recovery: The method of Fault
+ Failure recovery – The method of Fault Recovery is different in both Apache Hadoop and Apache Spark. In Hadoop after every operation data is written to disk. The data objects are stored in Spark in RDD distributed across data cluster. The RDDs are either in memory or on disk and provides full recovery from faults or failure.
+ File Management System – Hadoop has its own File Management System called HDFS (Hadoop Distributed File System). While Apache Spark an integration with one, it may be even HDFS. Thus, Hadoop can run over Apache Spark.
+ Computation model – Apache Hadoop uses batch processing model i.e. it takes a large amount of data and processes it. But Apache Spark adopts micro-batching. Must for handling near real time processing data model. When it comes to performance, because of batch processing in Hadoop it’s processing is quite slow. The processing speed of Apache is faster as it supports micro-batching.
+ Lines of code – Apache Hadoop has near about 23, 00,000 lines of code while Apache Spark has 20,000 lines of code.
+ Caching – By caching partial result in memory of distributed workers Spark ensures low latency computations. While MapReduce is completely disk oriented, there is no provision of caching.
+ Scheduler – Because of in-memory computation in Spark, it acts as its own flow scheduler. While with Hadoop MapReduce we need an extra job scheduler like Azkaban or Oozie so that we can schedule complex flows.
+ Spark API – Because of very Strict API in Hadoop MapReduce, it is not versatile. But since Spark discards many low-level details it is more productive.
+ Window criteria – Apache Spark has time-based window criteria. But Apache Hadoop does not have window criteria since it does not support streaming.
+ Faster – Apache Hadoop executes job 10 to 100 times faster than Apache Hadoop MapReduce.
+ License – Both Apache Hadoop and Apache MapReduce has a License Version 2.0.
+ DAG() – In Apache Spark, there is cyclic data flow in machine learning algorithm, which is a direct acyclic graph. While in Hadoop MapReduce data flow does not have any loops, rather it is a chain of the image.
+ Memory Management – Apache Spark has automatic memory management system. While Memory Management in Apache Hadoop can be either statistic or dynamic.
+ Iterative Processing – In Apache Spark, the data iterates in batches. Here processing and scheduling of each iteration are separate. While in Apache Hadoop there is no provision for iterative processing.
+ Latency – The time taken for processing by Apache Spark is less as compared to Hadoop since it caches its data on memory by means of RDD, thus the latency of Apache Spark is less as compared to Hadoop.

#### What is lazy evaluation in Spark?
lazy evaluation known as call-by-need is a strategy that delays the execution until one requires a value. The transformation in Spark is lazy in nature. Spark evaluate them lazily. When we call some operation in RDD it does not execute immediately; Spark maintains the graph of which operation it demands. We can execute the operation at any instance by calling the action on the data. The data does not loads until it is necessary.

#### What are the benefits of lazy evaluation?
Using lazy evaluation we can:
+ Increase the manageability of the program.
+ Saves computation overhead and increases the speed of the system.
+ Reduces the time and space complexity.
+ provides the optimization by reducing the number of queries.

#### What do you mean by Persistence?
RDD persistence is an optimization technique which saves the result of RDD evaluation. Using this we save the intermediate result for further use. It reduces the computation overhead. We can make persisted RDD through cache() and persist() methods. It is a key tool for the interactive algorithm. Because, when RDD is persisted each node stores any partition of it that it computes in memory. Thus makes it reusable for future use. This process speeds up the further computation ten times.

#### Explain the run time architecture of Spark?
The components of the run-time architecture of Spark are as follows:
+ The Driver – The main() method of the program runs in the driver. The process that runs the user code which creates RDDs performs transformation and action, and also creates SparkContext is called diver. When the Spark Shell is launched, this signifies that we have created a driver program. The application finishes, as the driver terminates. Finally, driver program splits the Spark application into the task and schedules them to run on the executor.
+ Cluster Manager –  Spark depends on cluster manager to launch executors. In some cases, even the drivers are launched by cluster manager. It is a pluggable component in Spark. On the cluster manager, the Spark scheduler schedules the jobs and action within a spark application in FIFO fashion. Alternatively, the scheduling can also be done in Round Robin fashion. The resources used by a Spark application can also be dynamically adjusted based on the workload. Thus, the application can free unused resources and request them again when there is a demand. This is available on all coarse-grained cluster managers, i.e. standalone mode, YARN mode, and Mesos coarse-grained mode.
+ The Executors –  Each task in the Spark job runs in the Spark executors. thus, Executors are launched once in the beginning of Spark Application and then they run for the entire lifetime of an application. Even after the failure of Spark executor, the Spark application can continue with ease.
  There are two main roles of the executors:
+ Runs the task that makes up the application and returns the result to the driver.
+ Provide in-memory storage for RDDs that the user program cache.

#### What is the difference between DSM and RDD?
a) READ
RDD: In RDD the read operation is coarse grained or fine grained. In coarse-grained we can transform the whole dataset but not an individual element. While in fine-grained we do the transformation of an individual element on a dataset.
Distributed Shared Memory: The read operation in Distributed shared memory is fine-grained.
b) Write:
RDD: The write operation is coarse-grained in RDD.
Distributed Shared Memory: In distributed shared system the write operation is fine grained.
c) Consistency:
RDD: The consistency of RDD is trivial meaning it is immutable in nature. Any changes made to an RDD cannot roll back, it is permanent. So the level of consistency is high.
Distributed Shared Memory: The system guarantees that if the programmer follows the rules, the memory will be consistent. It also guarantees that the results of memory operations will be predictable.
d) Fault-recovery mechanism:
RDD: Using lineage graph at any point in time we can easily find the lost data in an RDD.
Distributed Shared Memory: Fault tolerance is achieved by a checkpointing technique. It allows applications to roll back to a recent checkpoint rather than restarting.
e) Straggler mitigation: Stragglers, in general, are those tasks that take more time to complete than their peers.
RDD: in RDD it is possible to mitigate stragglers using backup task.
Distributed Shared Memory: It is quite difficult to achieve straggler mitigation.
f) Behavior if not enough RAM:
RDD: If there is not enough space to store RDD in RAM then the RDDs are shifted to disk.
Distributed Shared Memory: In this type of system the performance decreases if the RAM runs out of storage.

#### How can data transfer be minimized when working with Apache Spark?
By minimizing data transfer and avoiding shuffling of data we can increase the performance. In Apache Spark, we can minimize the data transfer in three ways:
By using a broadcast variable – Since broadcast variable increases the efficiency of joins between small and large RDDs. the broadcast variable allows keeping a read-only variable cached on every machine in place of shipping a copy of it with tasks. We create broadcast variable v by calling SparlContext.broadcast(v) and we can access its value by calling the value method.
Using Accumulator – Using accumulator we can update the value of a variable in parallel while executing. Accumulators can only be added through the associative and commutative operation. We can also implement counters (as in MapReduce) or sums using an accumulator. Users can create named or unnamed accumulator. We can create numeric accumulator by calling SparkContext.longAccumulator() or SparkContext.doubleAccumulator() for Long or Double respectively.
By avoiding operations like ByKey, repartition or any other operation that trigger shuffle. we can minimize the data transfer.

#### How does Apache Spark handles accumulated Metadata?
By triggering automatic cleanup Spark handles the automatic Metadata. We can trigger cleanup by setting the parameter “spark.cleaner.ttl“. the default value for this is infinite. It tells for how much duration Spark will remember the metadata. It is periodic cleaner. And also ensure that metadata older than the set duration will vanish. Thus, with its help, we can run Spark for many hours.

#### What are the common faults of the developer while using Apache Spark?
The common mistake by developers are:
Customer hit web-service several time by using multiple clusters.
Customer runs everything on local node instead of distributing it.

#### Which among the two is preferable for the project- Hadoop MapReduce or Apache Spark?
The answer to this question depends on the type of project one has. As we all know Spark makes use of a large amount of RAM and also needs a dedicated machine to provide an effective result. Thus the answer depends on the project and the budget of the organization.

#### List the popular use cases of Apache Spark.
The most popular use-cases of Apache Spark are:
1. Streaming
2. Machine Learning
3. interactive Analysis
4. fog computing
5. Using Spark in the real world

#### What is Spark.executor.memory in a Spark Application?
The default value for this is 1 GB. It refers to the amount of memory that will be used per executor process.
We have categorized the above Spark Interview Questions and Answers for Freshers and Experienced-
Spark Interview Questions and Answers for Fresher – Q.No.1-8, 37
Spark Interview Questions and Answers for Experienced – Q.No. 9-36, 38
Follow this link to read more Spark Basic interview Questions with Answers.
b. Spark SQL Interview Questions and Answers
In this section, we will discuss some basic Spark SQL Interview Questions and Answers.

#### What is DataFrames?
It is a collection of data which organize in named columns. It is theoretically equivalent to a table in relational database. But it is more optimized. Just like RDD, DataFrames evaluates lazily. Using lazy evaluation we can optimize the execution. It optimizes by applying the techniques such as bytecode generation and predicate push-downs.

#### What are the advantages of DataFrame?
It makes large data set processing even easier. Data Frame also allows developers to impose a structure onto a distributed collection of data. As a result, it allows higher-level abstraction.
Data frame is both space and performance efficient.
It can deal with both structured and unstructured data formats, for example, Avro, CSV etc . And also storage systems like HDFS, HIVE tables, MySQL, etc.
The DataFrame API’s are available in various programming languages. For example Java, Scala, Python, and R.
It provides Hive compatibility. As a result, we can run unmodified Hive queries on existing Hive warehouse.
Catalyst tree transformation uses DataFrame in four phases: a) Analyze logical plan to solve references. b) Logical plan optimization c) Physical planning d) Code generation to compile part of the query to Java bytecode.
It can scale from kilobytes of data on the single laptop to petabytes of data on the large cluster.

#### What is DataSet?
Spark Datasets are the extension of Dataframe API. It creates object-oriented programming interface and type-safety. Dataset is Spark 1.6 release. It makes use of Spark’s catalyst optimizer. It reveals expressions and data fields to a query optimizer. Dataset also influences fast in-memory encoding. It also provides provision for compile time type-safety. We can check for errors in an application when they run.

#### What are the advantages of DataSets?
It provides run-time type safety.
Influences fast in-memory encoding.
It provides a custom view of structured and semi-structured data.
It owns rich semantics and an easy set of domain-specific operations, as a result, it facilitates the use of structured data.
Dataset API decreases the use of memory. As Spark knows the structure of data in the dataset, thus it creates an optimal layout in memory while caching.

#### Explain Catalyst framework.
The Catalyst is a framework which represents and manipulate a DataFrame graph. Data flow graph is a tree of relational operator and expressions. The three main features of catalyst are:
It has a TreeNode library for transforming tree. They are expressed as Scala case classes.
A logical plan representation for relational operator.
Expression library.
The TreeNode builds a query optimizer. It contains a number of the query optimizer. Catalyst Optimizer supports both rule-based and cost-based optimization. In rule-based optimization the optimizer use set of rule to determine how to execute the query. While the cost based optimization finds the most suitable way to carry out SQL statement. In cost-based optimization, many plans are generates using rules. And after this, it computes their cost. Catalyst optimizer makes use of standard features of Scala programming like pattern matching.

#### What is DStream?
DStream is the high-level abstraction provided by Spark Streaming. It represents a continuous stream of data. Thus, DStream is internally a sequence of RDDs. There are two ways to create DStream:
by using data from different sources such as Kafka, Flume, and Kinesis.
by applying high-level operations on other DStreams.

#### Explain different transformation on DStream.
DStream is a basic abstraction of Spark Streaming. It is a continuous sequence of RDD which represents a continuous stream of data. Like RDD, DStream also supports many transformations which are available on normal Spark RDD. For example, map(func), flatMap(func), filter(func) etc.

#### What is written ahead log or journaling?
The write-ahead log is a technique that provides durability in a database system. It works in the way that all the operation that applies on data, we write it to write-ahead log. The logs are durable in nature. Thus, when the failure occurs we can easily recover the data from these logs. When we enable the write-ahead log Spark stores the data in fault-tolerant file system.

#### Explain first operation in Apache Spark RDD.
It is an action and returns the first element of the RDD.

#### Describe join operation. How is outer join supported?
join() is transformation and is in package org.apache.spark.rdd.pairRDDFunction
def join[W](other: RDD[(K, W)]): RDD[(K, (V, W))]Permalink
Return an RDD containing all pairs of elements with matching keys in this and other.
Each pair of elements will returns as a (k, (v1, v2)) tuple, where (k, v1) is in this and (k, v2) is in other. Performs a hash join across the cluster.
It is joining two datasets. When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (V, W)) pairs with all pairs of elements for each key. Outer joins are supported through leftOuterJoin, rightOuterJoin, and fullOuterJoin.

#### Describe coalesce operation. When can you coalesce to a larger number of partitions? Explain.
It is a transformation and it’s in a package org.apache.spark.rdd.ShuffledRDD
Return a new RDD that is reduced into numPartitions partitions.
This results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead, each of the 100 new partitions will claim 10 of the current partitions.
However, if you’re doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can pass shuffle = true. This will add a shuffle step but means the current upstream partitions will execut in parallel (per whatever the current partitioning is).
Note: With shuffle = true, you can actually coalesce to a larger number of partitions. This is useful if you have a small number of partitions, say 100, potentially with a few partitions being abnormally large. Calling coalesce(1000, shuffle = true) will result in 1000 partitions with the data distributed using a hash partitioner.
Coalesce() operation changes a number of the partition where data is stored. It combines original partitions to a new number of partitions, so it reduces the number of partitions. Coalesce() operation is an optimized version of repartition that allows data movement, but only if you are decreasing the number of RDD partitions. It runs operations more efficiently after filtering large datasets.

#### Describe Partition and Partitioner in Apache Spark.
Partition in Spark is similar to split in HDFS. A partition in Spark is a logical division of data stored on a node in the cluster. They are the basic units of parallelism in Apache Spark. RDDs are a collection of partitions. When some actions are executed, a task is launched per partition.
By default, partitions are automatically created by the framework. However, the number of partitions in Spark are configurable to suit the needs. For the number of partitions, if spark.default.parallelism is set, then we should use the value from SparkContext defaultParallelism, othewrwise we should use the max number of upstream partitions. Unless spark.default.parallelism is set, the number of partitions will be the same as that of the largest upstream RDD, as this would least likely cause out-of-memory errors.
A partitioner is an object that defines how the elements in a key-value pair RDD are partitioned by key, maps each key to a partition ID from 0 to numPartitions – 1. It captures the data distribution at the output. With the help of partitioner, the scheduler can optimize the future operations. The contract of partitioner ensures that records for a given key have to reside on a single partition.
We should choose a partitioner to use for a cogroup-like operations. If any of the RDDs already has a partitioner, we should choose that one. Otherwise, we use a default HashPartitioner.

There are three types of partitioners in Spark :
Hash Partitioner
Range Partitioner
Custom Partitioner
Hash – Partitioner: Hash- partitioning attempts to spread the data evenly across various partitions based on the key.
Range – Partitioner: In Range- Partitioning method, tuples having keys with same range will appear on the same machine.
RDDs can create with specific partitioning in two ways :
i) Providing explicit partitioner by calling partitionBy method on an RDD
ii) Applying transformations that return RDDs with specific partitioners.

#### How can you manually partition the RDD?
When we create the RDD from a file stored in HDFS.
data = context.textFile("/user/dataflair/file-name")
By default one partition is created for one block. ie. if we have a file of size 1280 MB (with 128 MB block size) there will be 10 HDFS blocks, hence the similar number of partitions (10) will create.
If you want to create more partitions than the number of blocks, you can specify the same while RDD creation:
data = context.textFile("/user/dataflair/file-name", 20)
It will create 20 partitions for the file. ie for each block 2 partitions will create.
NOTE: It is often recommended to have more no of partitions than no of the block, it improves the performance

#### Explain API create Or Replace TempView.
It’s basic Dataset function and under org.apache.spark.sql
def createOrReplaceTempView(viewName: String): Unit
Creates a temporary view using the given name.
scala> df.createOrReplaceTempView("titanicdata")

#### What are the various advantages of DataFrame over RDD in Apache Spark?
DataFrames are the distributed collection of data. In DataFrame, data is organized into named columns. It is conceptually similar to a table in a relational database.
we can construct DataFrames from a wide array of sources. Such as structured data files, tables in Hive, external databases, or existing RDDs.
As same as RDDs, DataFrames are evaluated lazily(Lazy Evaluation). In other words, computation only happens when an action (e.g. display result, save output) is required.
Out of the box, DataFrame supports reading data from the most popular formats, including JSON files, Parquet files, Hive tables. Also, can read from distributed file systems (HDFS), local file systems, cloud storage (S3), and external relational database systems through JDBC. In addition, through Spark SQL’s external data sources API, DataFrames can extend to support any third-party data formats or sources. Existing third-party extensions already include Avro, CSV, ElasticSearch, and Cassandra.
There is much more to know about DataFrames. Refer link: Spark SQL DataFrame

#### What is a DataSet and what are its advantages over DataFrame and RDD?
In Apache Spark, Datasets are an extension of DataFrame API. It offers object-oriented programming interface. Through Spark SQL, it takes advantage of Spark’s Catalyst optimizer by exposing e data fields to a query planner.
In SparkSQL, Dataset is a data structure which is strongly typed and is a map to a relational schema. Also, represents structured queries with encoders. DataSet has been released in Spark 1.6.
In serialization and deserialization (SerDe) framework, encoder turns out as a primary concept in Spark SQL. Encoders handle all translation process between JVM objects and Spark’s internal binary format. In Spark, we have built-in encoders those are very advanced. Even they generate bytecode to interact with off-heap data.
On-demand access to individual attributes without having to de-serialize an entire object is provided by an encoder. Spark SQL uses a SerDe framework, to make input-output time and space efficient. Due to encoder knows the schema of record, it became possible to achieve serialization as well as deserialization.
Spark Dataset is structured and lazy query expression(lazy Evolution) that triggers the action. Internally dataset represents a logical plan. The logical plan tells the computational query that we need to produce the data. the logical plan is a base catalyst query plan for the logical operator to form a logical query plan. When we analyze this and resolve we can form a physical query plan.
As Dataset introduced after RDD and DataFrame, it clubs the features of both. It offers the following similar features:
1. The convenience of RDD.
2. Performance optimization of DataFrame.
3. Static type-safety of Scala.
   Hence, we have observed that Datasets provides a more functional programming interface to work with structured data.
   To know more detailed information about DataSets, refer link: Spark Dataset

#### On what all basis can you differentiate RDD and DataFrame and DataSet?
DataFrame: A Data Frame is used for storing data into tables. It is equivalent to a table in a relational database but with richer optimization. Spark DataFrame is a data abstraction and domain-specific language (DSL) applicable on a structure and semi-structured data. It is distributed the collection of data in the form of named column and row. It has a matrix-like structure whose column may be different types (numeric, logical, factor, or character ). We can say data frame has the two-dimensional array like structure where each column contains the value of one variable and row contains one set of values for each column and combines feature of list and matrices
RDD is the representation of a set of records, immutable collection of objects with distributed computing. RDD is a large collection of data or RDD is an array of reference of partitioned objects. Each and every dataset in RDD is logically partitioned across many servers so that they can compute on different nodes of the cluster. RDDs are fault tolerant i.e. self-recovered/recomputed in the case of failure. The dataset can load externally by the users which can be in the form of JSON file, CSV file, text file or database via JDBC with no specific data structure.
DataSet in Apache Spark, Datasets are an extension of DataFrame API. It offers object-oriented programming interface. Through Spark SQL, it takes advantage of Spark’s Catalyst optimizer by exposing e data fields to a query planner.

#### Explain the level of parallelism in Spark Streaming.
In order to reduce the processing time, one need to increase the parallelism. In Spark Streaming, there are three ways to increase the parallelism:
Increase the number of receivers : If there are too many records for single receiver (single machine) to read in and distribute so that is bottleneck. So we can increase the no. of receiver depends on scenario.
Re-partition the receive data : If one is not in a position to increase the no. of receivers in that case redistribute the data by re-partitioning.
Increase parallelism in aggregation :
for complete guide on Spark Streaming you may refer to Apache Spark-Streaming guide

#### Discuss writeahead logging in Apache Spark Streaming.
There are two types of failures in any Apache Spark job – Either the driver failure or the worker failure.
When any worker node fails, the executor processes running in that worker node will kill, and the tasks which were scheduled on that worker node will be automatically moved to any of the other running worker nodes, and the tasks will accomplish.
When the driver or master node fails, all of the associated worker nodes running the executors will kill, along with the data in each of the executors’ memory. In the case of files being read from reliable and fault tolerant file systems like HDFS, zero data loss is always guaranteed, as the data is ready to be read anytime from the file system. Checkpointing also ensures fault tolerance in Spark by periodically saving the application data in specific intervals.
In the case of Spark Streaming application, zero data loss is not always guaranteed, as the data will buffer in the executors’ memory until they get processed. If the driver fails, all of the executors will kill, with the data in their memory, and the data cannot recover.
To overcome this data loss scenario, Write Ahead Logging (WAL) has been introduced in Apache Spark 1.2. With WAL enabled, the intention of the operation is first noted down in a log file, such that if the driver fails and is restarted, the noted operations in that log file can apply to the data. For sources that read streaming data, like Kafka or Flume, receivers will be receiving the data, and those will store in the executor’s memory. With WAL enabled, these received data will also store in the log files.
WAL can enable by performing the below:
1. Setting the checkpoint directory, by using streamingContext.checkpoint(path)
2. Enabling the WAL logging, by setting spark.stream.receiver.WriteAheadLog.enable to True.

#### What do you mean by Speculative execution in Apache Spark?
The Speculative task in Apache Spark is task that runs slower than the rest of the task in the job.It is health check process that verifies the task is speculated, meaning the task that runs slower than the median of successfully completed task in the task sheet. Such tasks are submitted to another worker. It runs the new copy in parallel rather than shutting down the slow task.

In the cluster deployment mode, the thread starts as TaskSchedulerImp1with spark.speculation enabled. It executes periodically every spark.speculation.interval after the initial spark.speculation.interval passes.

#### How do you parse data in XML? Which kind of class do you use with java to pass data?
One way to parse the XML data in Java is to use the JDOM library. One can download it and import the JDOM library in your project. You can get help from Google. If still, required help post your problem in the forum. I will try to give you the solution. For Scala, Scala has the inbuilt library for XML parsing. Scala-xml_2.11-1.0.2 jar (please check them for new version if available).

#### Explain Machine Learning library in Spark.
It is a scalable machine learning library. It delivers both blazing speed (up to 100x faster than MapReduce) and high-quality algorithms (e.g., multiple iterations to increase accuracy). We can use this library in Java, Scala, and Python as part of Spark applications so that you can include it incomplete workflows. There are many tools, which are provided by MLlib. Such as-
ML Algorithms: Common learning algorithms such as classification, regression, clustering, and collaborative filtering.
Featurization: Feature extraction, transformation, dimensionality reduction, and selection.
Pipelines: Tools for constructing, evaluating, and tuning ML Pipelines.
Persistence: Saving and load algorithms, models, and Pipelines.
Utilities: Linear algebra, statistics, data handling, etc.
For detailed insights, follow link: Apache Spark MLlib (Machine Learning Library)

#### List various commonly used Machine Learning Algorithm.
Basically, there are three types of Machine Learning Algorithms :
(1) Supervised Learning Algorithm
(2) Unsupervised Learning Algorithm
(3) Reinforcement Learning Algorithm
Most commonly used Machine Learning Algorithm is as follows :
Linear Regression
Logistic Regression
Decision Tree
K-Means
KNN
SVM
Random Forest
Naïve Bayes
Dimensionality Reduction Algorithm
Gradient Boost and Adaboost
For what is MLlib see Apache Spark Ecosystem

#### Explain the Parquet File format in Apache Spark. When is it the best to choose this?
Parquet is the columnar information illustration that is that the best choice for storing long run massive information for analytics functions. It will perform each scan and write operations with Parquet file. It could be a columnar information storage format.

#### What is Lineage Graph?
The RDDs in Spark, depend on one or more other RDDs. The representation of dependencies in between RDDs is known as the lineage graph. Lineage graph information is used to compute each RDD on demand, so that whenever a part of persistent RDD is lost, the data that is lost can be recovered using the lineage graph information.

#### How can you Trigger Automatic Cleanups in Spark to Handle Accumulated Metadata?
You can trigger the clean-ups by setting the parameter spark.cleaner.ttl or by dividing the long running jobs into different batches and writing the intermediary results to the disk.

#### What are the benefits of using Spark With Apache Mesos?
It renders scalable partitioning among various Spark instances and dynamic partitioning between Spark and other big data frameworks.

#### What is the Significance of Sliding Window Operation?
Sliding Window controls transmission of data packets between various computer networks. Spark Streaming library provides windowed computations where the transformations on RDDs are applied over a sliding window of data. Whenever the window slides, the RDDs that fall within the particular window are combined and operated upon to produce new RDDs of the windowed DStream.

#### When running Spark Applications is it necessary to install Spark on all Nodes of Yarn Cluster?
Spark need not be installed when running a job under YARN or Mesos because Spark can execute on top of YARN or Mesos clusters without affecting any change to the cluster.

#### What is Catalyst Framework?
Catalyst framework is a new optimization framework present in Spark SQL. It allows Spark to automatically transform SQL queries by adding new optimizations to build a faster processing system.

#### Which Spark Library allows reliable File Sharing at Memory Speed across different cluster frameworks?
Tachyon

#### Why is Blinkdb used?
BlinkDB is a query engine for executing interactive SQL queries on huge volumes of data and renders query results marked with meaningful error bars. BlinkDB helps users balance query accuracy with response time.

#### How can you compare Hadoop and Spark in terms of ease of use?
Hadoop MapReduce requires programming in Java which is difficult, though Pig and Hive make it considerably easier. Learning Pig and Hive syntax takes time. Spark has interactive APIs for different languages like Java, Python or Scala and also includes Shark i.e. Spark SQL for SQL lovers - making it comparatively easier to use than Hadoop.

#### What are the common mistakes developers make when running Spark Applications?
Developers often make the mistake of:-
Hitting the web service several times by using multiple clusters.
Run everything on the local node instead of distributing it.
Developers need to be careful with this, as Spark makes use of memory for processing.

#### What is the Advantage of a Parquet File?
Parquet file is a columnar format file that helps:
Limit I/O operations
Consumes less space
Fetches only required columns.

#### What are the various Data Sources available in Sparksql?
Parquet file
JSON Datasets
Hive tables

#### What are the Key Features of Apache Spark that you like?
Spark provides advanced analytic options like graph algorithms, machine learning, streaming data, etc
It has built-in APIs in multiple languages like Java, Scala, Python and R
It has good performance gains, as it helps run an application in the Hadoop cluster ten times faster on disk and 100 times faster in memory.

#### What do you understand by Pair Rdd?
Special operations can be performed on RDDs in Spark using key/value pairs and such RDDs are referred to as Pair RDDs. Pair RDDs allow users to access each key in parallel. They have a reduceByKey () method that collects data based on each key and a join () method that combines different RDDs together, based on the elements having the same key.

#### Explain about different Types of Transformations on Dstreams?
Stateless Transformations:- Processing of the batch does not depend on the output of the previous batch.
Examples: map (), reduceByKey (), filter ().
Stateful Transformations:- Processing of the batch depends on the intermediary results of the previous batch.
Examples: Transformations that depend on sliding windows.

#### Explain about popular use cases of Apache Spark?
Apache Spark is mainly used for:
Iterative machine learning.
Interactive data analytics and processing.
Stream processing
Sensor data processing

#### Is Apache Spark a good fit for reinforcement Learning?
No. Apache Spark works well only for simple machine learning algorithms like clustering, regression, classification.

#### What is Spark Core?
It has all the basic functionalities of Spark, like - memory management, fault recovery, interacting with storage systems, scheduling tasks, etc.

#### How can you remove the elements with a Key present in any other Rdd?
Use the subtractByKey () function.

#### What is the difference between Persist and Cache?
persist () allows the user to specify the storage level where as cache () uses the default storage level.

#### How Spark handles Monitoring and Logging in Standalone Mode?
Spark has a web based user interface for monitoring the cluster in standalone mode that shows the cluster and job statistics. The log output for each job is written to the work directory of the slave nodes.

#### Does Apache Spark provide check pointing?
Lineage graphs are always useful to recover RDDs from a failure but this is generally time consuming if the RDDs have long lineage chains. Spark has an API for check pointing i.e. a REPLICATE flag to persist. However, the decision on which data to checkpoint - is decided by the user. Checkpoints are useful when the lineage graphs are long and have wide dependencies.

#### How can you launch Spark Jobs inside Hadoop Mapreduce?
Using SIMR (Spark in MapReduce) users can run any spark job inside MapReduce without requiring any admin rights.

#### How can you achieve High Availability in Apache Spark?
Implementing single node recovery with local file system
Using StandBy Masters with Apache ZooKeeper.

#### Hadoop uses Replication to achieve Fault Tolerance and how is this achieved in Apache Spark?
Data storage model in Apache Spark is based on RDDs. RDDs help achieve fault tolerance through lineage. RDD always has the information on how to build from other datasets. If any partition of a RDD is lost due to failure, lineage helps build only that particular lost partition.

#### Explain about Core Components of a distributed Spark Application?
Driver: The process that runs the main () method of the program to create RDDs and perform transformations and actions on them.
Executor: The worker processes that run the individual tasks of a Spark job.
Cluster Manager: A pluggable component in Spark, to launch Executors and Drivers. The cluster manager allows Spark to run on top of other external managers like Apache Mesos or YARN.

#### What do you understand by Lazy Evaluation?
Spark is intellectual in the manner in which it operates on data. When you tell Spark to operate on a given dataset, it heeds the instructions and makes a note of it, so that it does not forget - but it does nothing, unless asked for the final result.
When a transformation like map () is called on a RDD-the operation is not performed immediately. Transformations in Spark are not evaluated till you perform an action. This helps optimize the overall data processing workflow.

#### Define a Worker Node?
A node that can run the Spark application code in a cluster can be called as a worker node. A worker node can have more than one worker which is configured by setting the SPARK_ WORKER_INSTANCES property in the spark-env.sh file. Only one worker is started if the SPARK_ WORKER_INSTANCES property is not defined.

#### What do you understand by Schemardd?
An RDD that consists of row objects (wrappers around basic string or integer arrays) with schema information about the type of data in each column.

#### What are the disadvantages of using Apache Spark over Hadoop Mapreduce?
Apache spark does not scale well for compute intensive jobs and consumes large number of system resources. Apache Spark’s in-memory capability at times comes a major roadblock for cost efficient processing of big data. Also, Spark does have its own file management system and hence needs to be integrated with other cloud based data platforms or apache hadoop.

#### Is it necessary to install Spark on all Nodes of Yarn Cluster while running Apache Spark on Yarn?
No , it is not necessary because Apache Spark runs on top of YARN.

#### What do you understand by Executor Memory in Spark Application?
Every spark application has same fixed heap size and fixed number of cores for a spark executor. The heap size is what referred to as the Spark executor memory which is controlled with the spark.executor.memory property of the –executor-memory flag.
Every spark application will have one executor on each worker node. The executor memory is basically a measure on how much memory of the worker node will the application utilize.

#### What does the Spark Engine do?
Spark engine schedules, distributes and monitors the data application across the spark cluster.

#### What makes Apache Spark good at Low latency Workloads like Graph Processing and Machine Learning?
Apache Spark stores data in-memory for faster model building and training. Machine learning algorithms require multiple iterations to generate a resulting optimal model and similarly graph algorithms traverse all the nodes and edges.
These low latency workloads that need multiple iterations can lead to increased performance. Less disk access and  controlled network traffic make a huge difference when there is lots of data to be processed.

#### What is Dstream in Apache Spark?
Dstream stands for Discretized Stream. It is a sequence of Resilient Distributed Database (RDD) representing a continuous stream of data. There are several ways to create Dstream from various sources like HDFS, Apache Flume, Apache Kafka, etc.

#### What do you understand by YARN?
Just like in Hadoop, YARN is one of the key features in Apache Spark, which is used to provide a central and resource management platform to deliver scalable operations across the cluster. Spark can run on YARN, as the same way Hadoop Map Reduce can run on YARN.

#### Is it necessary to install Spark on all nodes of the YARN cluster?
No. It doesn't seem necessary to install Spark on all YARN cluster nodes because Spark runs on top of the YARN. Apache Spark runs independently from its installation. Spark provides some options to use YARN when dispatching jobs to the cluster, rather than its built-in manager or Mesos. Besides this, there are also some configurations to run YARN, such as master, deploy-mode, driver-memory, executor-memory, executor-cores, and queue.

#### What are the different data sources available in SparkSQL?
There are the following three data sources available in SparkSQL:
JSON Datasets
Hive tables
Parquet file

#### Which are some important internal daemons used in Apache Spark?
Following are the important internal daemons used in Spark:
Blockmanager
Memestore
DAGscheduler
Driver
Worker
Executor
Tasks etc.

#### What is the method to create a Data frame in Apache Spark?
In Apache Spark, we can create a data frame using Tables in Hive and Structured data files.

#### What do you understand by accumulators in Apache Spark?
Accumulators are the write-only variables that are initialized once and sent to the workers. Then, these workers update based on the logic written, which will send back to the driver.

#### What is the default level of parallelism in Apache Spark?
If it is not specified, then the number of partitions is called the default level of parallelism in Apache Spark.

#### Which companies are using Spark streaming services?
The three most famous companies using Spark Streaming services are:
Uber
Netflix
Pinterest

#### Is it possible to use Spark to access and analyze data stored in Cassandra databases?
Yes, it is possible to use Spark to access and analyze Cassandra databases' data by using Cassandra Connector.

#### Can we run Apache Spark on Apache Mesos?
Yes, we can run Apache Spark on the hardware clusters managed by Mesos.

#### What do you understand by Spark SQL?
Spark SQL is a module for structured data processing, which provides the advantage of SQL queries running on that database.

#### How can you connect Spark to Apache Mesos?
Follow the steps given below to connect Spark to Apache Mesos:
Configure the spark driver program to connect to Mesos.
Set a path location for the Spark binary package that it can be accessible by Mesos.
Install Apache Spark in the same location as that of Apache Mesos and configure the property spark.mesos.executor.home to point to the location where it is installed.

#### What is the best way to minimize data transfers when working with Spark?
To write a fast and reliable Spark program, we have to minimize data transfers and avoid shuffling. There are various ways to minimize data transfers while working with Apache Spark. These are:
Using Broadcast Variable- Broadcast variables enhance the efficiency of joins between small and large RDDs.
Using Accumulators- Accumulators are used to updating the values of variables in parallel while executing.

#### What do you understand by lazy evaluation in Apache Spark?
As the name specifies, lazy evaluation in Apache Spark means that the execution will not start until an action is triggered. In Spark, the lazy evaluation comes into action when Spark transformations occur. Transformations are lazy. When a transformation such as a map() is called on an RDD, it is not performed instantly. Transformations in Spark are not evaluated until you perform an action, which aids in optimizing the overall data processing workflow, known as lazy evaluation. So we can say that in lazy evaluation, data is not loaded until it is necessary.

#### What do you understand by Spark Driver?
Spark Driver is the program that runs on the master node of the machine and is used to declare transformations and actions on data RDDs.

#### What is the Parquet file in Apache Spark?
Parquet is a column format file supported by many data processing systems. Spark SQL facilitates us to perform both read and write operations with the Parquet file.

#### What is the way to store the data in Apache Spark?
Apache Spark is an open-source analytics and processing engine for large-scale data processing, but it does not have any storage engine. It can retrieve data from another storage engine like HDFS, S3.

#### How is it possible to implement machine learning in Apache Spark?
Apache Spark itself provides a versatile machine learning library called MLif. By using this library, we can implement machine learning in Spark.

#### What are some disadvantages or demerits of using Apache Spark?
Following is the list of some disadvantages or demerits of using Apache Spark:
Apache Spark requires more storage space than Hadoop and MapReduce, so that it may create some problems.
Apache Spark consumes a huge amount of data as compared to Hadoop.
Apache Spark requires more attentiveness because developers need to be careful while running their applications in Spark.
Spark runs on multiple clusters on different nodes instead of running everything on a single node. So, the work is distributed over multiple clusters.
The "in-memory" capability of Apache Spark makes it a more costly way for processing big data.

#### What is the use of File system API in Apache Spark?
File system API is used to read data from various storage devices such as HDFS, S3 or Local Files.

#### What are the tasks of a Spark Engine?
The main task of a Spark Engine is handling the process of scheduling, distributing and monitoring the data application across the clusters.

#### What is the use of Apache SparkContext?
The SparkContent is the entry point to Apache Spark. SparkContext facilitates users to create RDDs, which provide various ways of churning data.

#### Is it possible to do real-time processing with SparkSQL?
In SparkSQL, real-time data processing is not possible directly. We can register the existing RDD as a SQL table and trigger the SQL queries on priority.

#### What is the use of Akka in Apache Spark?
Akka is used for scheduling in Apache Spark. Spark also uses Akka for messaging between the workers and masters.

#### What do you understand by Spark map() Transformation?
Spark map() is a transformation operation used to apply the Transformation on every element of RDD, DataFrame, and Dataset and finally returns a new RDD/Dataset, respectively.

#### What is the advantage of using the Parquet file?
In Apache Spark, the Parquet file is used to perform both read and write operations. Following is the list of some advantages of having a Parquet file:

Parquet file facilitates users to fetch specific columns for access.
It consumes less space.
It follows the type-specific encoding.
It supports limited I/O operations.

#### What is the difference between persist() and cache() functions in Apache Spark?
In Apache Spark, the persist() function is used to allow the user to specify the storage level, whereas the cache() function uses the default storage level.

#### Which Spark libraries allow reliable file sharing at memory speed across different cluster frameworks?
Tachyon is the Apache Spark library's name, which is used for reliable file sharing at memory speed across various cluster frameworks.

#### What is shuffling in Apache Spark? When does it occur?
In Apache Spark, shuffling is the process of redistributing data across partitions that may lead to data movement across the executors. The implementation of shuffle operation is entirely different in Spark as compared to Hadoop.
Shuffling has two important compression parameters:
shuffle.compress: It is used to check whether the engine would compress shuffle outputs or not.
shuffle.spill.compress: It is used to decide whether to compress intermediate shuffle spill files or not.
Shuffling comes in the scene when we join two tables or perform byKey operations such as GroupByKey or ReduceByKey.

#### What is the lineage in Spark?
In Apache Spark, when a transformation (map or filter etc.) is called, it is not executed by Spark immediately; instead, a lineage is created for each transformation. This lineage is used to keep track of what all transformations have to be applied on that RDD. It also traces the location from where it has to read the data.

#### How can you trigger automatic clean-ups in Spark to handle accumulated metadata?
You can trigger the clean-ups by setting the parameter Spark.cleaner.ttl or dividing the long-running jobs into different batches and writing the intermediary results to the disk.

#### Is it possible to launch Spark jobs inside Hadoop MapReduce?
Yes, you can run all kinds of spark jobs inside MapReduce without the need to obtain the admin rights of that application.

#### What is the use of BlinkDB in Spark?
BlinkDB is a query engine tool used to execute SQL queries on massive volumes of data and renders query results in the meaningful error bars.



## Additional Resources

1. [Data Engineer Interview @ Amazon 2022](https://moizs.medium.com/data-engineer-interview-amazon-2022-411664bbda25)
2. [Top 62 Data Engineer Interview Questions & Answers in 2022](https://www.guru99.com/data-engineer-interview-questions.html)
3. [Top 100 Data Engineer Interview Question 2022](https://www.interviewquery.com/p/data-engineer-interview-questions)
4. [Facebook Data Engineer Interview Questions](https://www.interviewkickstart.com/interview-questions/facebook-data-engineer-interview-questions)
5. [Amazon Data Engineer Interview Questions](https://www.interviewkickstart.com/interview-questions/amazon-data-engineer-interview-questions)
6. [60+ Uber Data Engineer Interview Questions](https://www.interviewkickstart.com/interview-questions/uber-data-engineer-interview-questions)
7. [Square Data Engineer Interview Questions](https://www.interviewkickstart.com/interview-questions/square-data-engineer-interview-questions)
8. [Azure Data Engineer Interview Questions](https://www.interviewkickstart.com/interview-questions/azure-data-engineer-interview-questions)
9. [Top Snap Interview Questions and Answers for Product Managers, Data Engineers, and Software Engineers](https://www.interviewkickstart.com/interview-questions/snap-interview-questions)
10. [Top Kafka Interview Questions and Answers You Should Prepare](https://www.interviewkickstart.com/interview-questions/kafka-interview-questions)
11. [Top Docker Interview Questions and Answers for Your Interview Prep](https://www.interviewkickstart.com/interview-questions/docker-interview-questions)
12. [Top REST API Interview Questions](https://www.interviewkickstart.com/interview-questions/rest-api-interview-questions)
13. [Top Data Modeling Interview Questions and Answers](https://www.interviewkickstart.com/interview-questions/data-modeling-interview-questions)
14. [Top PySpark Interview Questions for Your Tech Interview](https://www.interviewkickstart.com/interview-questions/pyspark-interview-questions)
15. [Top ETL Interview Questions and Answers](https://www.interviewkickstart.com/interview-questions/etl-interview-questions)
16. [Top Hadoop Interview Questions to Practice for Your Tech Interview](https://www.interviewkickstart.com/interview-questions/hadoop-interview-questions)
17. [Top SQL Interview Questions for Experienced Professionals](https://www.interviewkickstart.com/interview-questions/sql-interview-questions-for-experienced)
18. [Top SQL Interview Questions for Developers](https://www.interviewkickstart.com/interview-questions/sql-interview-questions-for-developers)
19. [Top Google Database Interview Questions for Your SQL Interview](https://www.interviewkickstart.com/interview-questions/google-database-interview-questions)
20. [Top Relational Databases Interview Questions and Answers You Should Learn](https://www.interviewkickstart.com/interview-questions/relational-databases-interview-questions)
21. [Cloud Engineer Interview Questions - Basic, Intermediate, and Advanced](https://www.interviewkickstart.com/interview-questions/cloud-engineer-interview-questions)
22. [Data Engineer Interview Questions](https://www.interviewbit.com/data-engineer-interview-questions/)
23. [Top 40 Apache Spark Interview Questions and Answers in 2022](https://intellipaat.com/blog/interview-question/apache-spark-interview-questions/)
24. [Top Hadoop Interview Questions and Answers](https://intellipaat.com/blog/interview-question/big-data-hadoop-interview-questions/)
25. [Top Kafka Interview Questions – Most Asked](https://intellipaat.com/blog/interview-question/kafka-interview-questions/)
26. [Top HDFS Interview Questions And Answers](https://intellipaat.com/blog/interview-question/hdfs-interview-questions/)
27. [Top Cassandra Interview Questions and Answers](https://intellipaat.com/blog/interview-question/cassandra-interview-questions/)
28. [Top PIG Interview Questions - Most Asked](https://intellipaat.com/blog/interview-question/pig-interview-questions/)
29. [Top Hive Interview Questions – Most Asked](https://intellipaat.com/blog/interview-question/hive-interview-questions/)
30. [Top Sqoop Interview Questions – Most Asked](https://intellipaat.com/blog/interview-question/sqoop-interview-questions/)
31. [Top HDFS Interview Questions And Answers](https://intellipaat.com/blog/interview-question/hdfs-interview-questions/)
32. [Top Mapreduce Interview Questions And Answers](https://intellipaat.com/blog/interview-question/map-reduce-interview-questions/)
33. https://github.com/OBenner/data-engineering-interview-questions
34. https://knowledgetree.notion.site/Spark-Interview-Questions-94ff173de85d4df6849b289665e8fff3