# Expert Tips

## Tips for Technical Round

**Coding**

Fortunately, online resources abound for preparing for a technical coding interview. Here’s the rough flow I would take:

1. Get familiar with data structures. Focus on how to use lists and hashmaps (dictionaries) above all else and solve problems that require you to use and switch between them. Make sure you also understand trees and linked lists. You should understand when and why to use one data structure over another and the space and time complexity of basic operations on all of them (appending, inserting, searching).
2. Understand some of the basic algorithms such as binary search and merge sort. I recommend the book Grokking Algorithms by Aditya Y. Bhargava for a good introduction if you are not familiar with implementing them.
3. Work through problems on a platform like Leetcode or Hackerrank. I really recommend Leetcode, especially for refining your work down to one topic like a specific data structure or even to company-specific questions. Here is a link to their collection of “Easy” problems to work through, categorized by data structure: Leetcode Easy Problem Set. In my opinion, making the leap to Leetcode Premium is worth it to get full access to all of the questions plus solutions. They occasionally also offer month-long challenges that will pose a new question each day — take advantage of that! For most data engineering interviews, I think you can stick to “Easy” and “Medium” level problems. Focus on the data structures and understanding the complexity of your solutions. Don’t worry too much about delving into more advanced software engineering topics or “Hard” problems unless you anticipate that the role you are applying for will require it.

In Python, you should be comfortable with standard Python and supplemental libraries like Matplotlib, Pandas, and NumPy, know what’s available, and understand when it’s appropriate to use each library. Tip: Don’t fake it. If you don’t have much experience, be honest. You can also describe a related skill or talk about your comfort level in quickly picking up new Python skills (with an example).

**SQL**

Ah, SQL. Seems so deceptively simple. Well, SQL has tripped me up a LOT in the past. I thought I knew it because I could do some INSERTS and SELECTS and knew how to do a basic JOIN or two. How naive I was… don’t underestimate SQL! That being said, it is not easy to find resources for truly tricky SQL problems to work through. Here are some I like:

1. Leetcode (again!). Go the Database category and work your way through all of the available problems. Remember how I said that for coding you could focus on Easy and Medium but not too worry too much about Hard? Well, not for SQL. You should aim to be able to solve problems across all three difficulties. As a caveat, I don’t find the Leetcode platform as good for SQL as I find it for coding problems; sometimes the questions are oddly categorized and/or poorly defined. Sort by Acceptance rate to get a better sense of the problem’s difficulty, and keep an eye on the problem’s “thumbs up/down” user rating: some of the poorly rated questions are not very clear and can lead to confusion.
2. Hackerrank. I actually think Hackerrank’s SQL problem sets are top notch (and you’ll get sick of reading about Weather Observation stations!). Work your way through them, focusing on diversifying the skills you work on (joins, window functions, CASE WHEN statements) and less on cranking out the problems that are just multiple complicated WHERE filters.

**Database Design**

Many companies will expect you to be able to design a proper data warehouse given a business use case. Luckily there are quite a few resources available out there for brushing up on these skills. While a lot of them are more textbook-like, try to push yourself to actually work through some real-life use cases by designing a data warehouse for an online store, a peer-to-peer marketplace, or a rideshare application. Sketch out the schema on paper or a whiteboard and build up a process for starting a new problem or design. Here are some books and online resources for learning about data warehouse design:

1. The Data Warehouse Toolkit: The Complete Guide to Dimensional Modelling. This is oft-cited and a great introduction to a lot of the foundational concepts
2. Star Schema:The Complete Reference by Christopher Adamson. This covers dimensional design and data warehouse architectures as well as touching on ETL principles.
3. I have seen the Udemy course Data Warehouse Concepts recommended, but have not taken it myself.

**Data Architecture and Big Data Technologies**

Some companies will expect you to have greater experience or familiarity in big data technologies (think Hadoop, Spark, and event processing technologies like Kafka) than others will. There are many books available that cover these technologies in-depth, but unfortunately due to the rate of change of the industry they tend to become out of date quite quickly. Nothing really beats experience here, but the following are some good resources for getting started and/or sharpening up your skills in preparation for an interview:

1. Designing Data-Intensive Applications by Martin Kleppmann is a great book that covers distributed systems thoroughly from both a theoretical and practical standpoint, and discusses a lot of the concepts that underpin Big Data tech like Hadoop and Kafka. (Shameless plug for the review I wrote last summer which goes into more detail on this particular book).
2. Try playing with Spark with Databricks Community Edition
3. Read some of the official documentation for things like Hadoop, Spark, Kafka, Hive. Some companies like to ask questions to test your understanding of the underlying concepts of big data frameworks and technologies, and the official documentation often gives the most succinct and correct explanation as to the why and how of each one. I think it’s useful to think about when you might want to use one technology over another and the tradeoffs that you make when you decide to, say, move to a Hadoop cluster over a single powerful machine. Be able to discuss a good use case for Spark or Kafka, for example. This is somewhat esoteric, but unfortunately there’s not as neat a template for these kinds of questions as there is for the algorithmic or SQL kind.

## Soft Skills

Don’t neglect the soft skills portion of the interview, either! Good communication and problem solving skills go a long way.

1. One of the most important things you can do to prepare is to talk your way through the problems you are solving. It is really easy to get focused on a coding or schema design problem and go silent as you think; but unfortunately, that makes you completely inscrutable to the interviewer. Talking your way through the thought process is harder than it sounds, and it doesn’t come naturally; I really recommend explicitly practicing this as you work your way through algorithmic and design problems.
2. Write your code on a whiteboard rather than in an IDE or on paper. It sounds odd, but you will likely be asked to solve a problem on a whiteboard during your on-site interview, or even type into a blank word processor during a video call. If you’ve only practiced in IDEs that provide syntax support and familiar formatting, this will seem unnatural and can throw you off. Definitely explicitly practice it so it feels comfortable when it comes time for the interview.
3. Use the platform Pramp to work through real practice interviews with real people. This tool helped me a lot; like I mentioned in point 1, I found it very difficult to talk my way through problems, and when I hit an obstacle I would often freeze and go silent or into an excruciating “uh” mode where no prompting from the interviewer could help. Pramp is ostensibly low-pressure, because you are not actually interviewing; but it feels just as high-pressure, because you are working through problems in front of a stranger. It also puts you in the position of the interviewer, too, which I found really useful for expanding my understanding of problems.