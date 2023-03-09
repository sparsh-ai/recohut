# SQLite Basics

The following entity-relationship- (ER) diagram for the books database shows the database’s tables and the relationships among them:

![](https://user-images.githubusercontent.com/62965911/214046007-fdd1f654-bc02-4d0f-a2f9-ca6e41ab6803.png)

The first compartment in each box contains the table’s name, and the remaining compartments contain the table’s columns. The names in italic are primary keys. A table’s primary key uniquely identifies each row in the table. Every row must have a primary-key value, and that value must be unique in the table. This is known as the Rule of Entity Integrity. Again, for the author_ISBN table, the primary key is the combination of both columns—this is known as a composite primary key.

The line between the titles and author_ISBN tables illustrates a one-to-many relationship—one book can be written by many authors. The line links the primary key isbn in table titles to the corresponding foreign key in table author_ISBN. The relationships in the entity-relationship diagram illustrate that the sole purpose of the author_ISBN table is to provide a many-to-many relationship between the authors and titles tables—an author can write many books, and a book can have many authors.