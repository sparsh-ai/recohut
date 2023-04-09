# Triggers

*Triggers* are a type of stored procedure, configured to call whenever an event occurs. This trigger can be used, for example, to signalize the execution of some statements whenever new data is included in a table, or a record is edited in the table.

Many *trigger* use cases are about creating transaction audit tables and maintaining data consistency, by reviewing relationships before confirming any type of transaction. We can use a trigger in the data definition and for data manipulation instructions.

In the following, we will use the **DDL CREATE** statement, which we have already seen in this note to create tables, but now we will use it to create a **TRIGGER**:

```sql
CREATE TRIGGER LOG_PRICE_HISTORY before update
on PRODUCTS_SERVICES
for each row
insert into PRICE_HISTORY
values(old.PRODUCTID, old.BASEPRICE, old.DISCOUNT, old.FINALPRICE, old.DATELASTUPDATE);
```

Executing this command, the **LOG_PRICE_HISTORY** trigger will be created and linked to the **PRODUCTS_SERVICES** table, with the following condition: whenever an item is edited in this table, a new record will be created in the **PRICE_HISTORY** table with the data from this table before the change.

This makes it possible for you to keep a history of this table and know exactly the changes that were made.

Sometimes, tables become very large, with thousands and even millions of records. This size can cause performance problems in database operations, and one of the methods used to mitigate these problems was indexes, which we are going to look at now.

In MySQL, a trigger is a stored program invoked automatically in response to an event such as [insert](https://www.mysqltutorial.org/mysql-insert-statement.aspx), [update](https://www.mysqltutorial.org/mysql-update-data.aspx), or [delete](https://www.mysqltutorial.org/mysql-delete-statement.aspx) that occurs in the associated table. For example, you can define a trigger that is invoked automatically before a new row is inserted into a table.

MySQL supports triggers that are invoked in response to the [INSERT](https://www.mysqltutorial.org/mysql-insert-statement.aspx), [UPDATE](https://www.mysqltutorial.org/mysql-update-data.aspx) or [DELETE](https://www.mysqltutorial.org/mysql-delete-statement.aspx) event.

The SQL standard defines two types of triggers: row-level triggers and statement-level triggers.

- A row-level trigger is activated for each row that is inserted, updated, or deleted.  For example, if a table has 100 rows inserted, updated, or deleted, the trigger is automatically invoked 100 times for the 100 rows affected.
- A statement-level trigger is executed once for each transaction regardless of how many rows are inserted, updated, or deleted.

**Advantages of triggers**

- Triggers provide another way to check the integrity of data.
- Triggers handle errors from the database layer.
- Triggers give an alternative way to [run scheduled tasks](https://www.mysqltutorial.org/mysql-triggers/working-mysql-scheduled-event/). By using triggers, you don't have to wait for the [scheduled events](https://www.mysqltutorial.org/mysql-triggers/working-mysql-scheduled-event/) to run because the triggers are invoked automatically *before* or *after* a change is made to the data in a table.
- Triggers can be useful for auditing the data changes in tables.

**Disadvantages of triggers**

- Triggers can only provide extended validations, not all validations. For simple validations, you can use the [NOT NULL](https://www.mysqltutorial.org/mysql-not-null-constraint/), [UNIQUE](https://www.mysqltutorial.org/mysql-unique-constraint/), [CHECK](https://www.mysqltutorial.org/mysql-check-constraint/) and [FOREIGN KEY](https://www.mysqltutorial.org/mysql-foreign-key/) constraints.
- Triggers can be difficult to troubleshoot because they execute automatically in the database, which may not invisible to the client applications.
- Triggers may increase the overhead of the MySQL Server.