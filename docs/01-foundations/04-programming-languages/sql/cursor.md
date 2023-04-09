# Cursor

To handle a result set inside a [stored procedure](https://www.mysqltutorial.org/mysql-stored-procedure-tutorial.aspx "MySQL Stored Procedure"), you use a cursor. A cursor allows you to [iterate ](https://www.mysqltutorial.org/stored-procedures-loop.aspx "How to use loop in stored procedure")a set of rows returned by a query and process each row individually.

MySQL cursor is read-only, non-scrollable and asensitive.

- Read-only: you cannot update data in the underlying table through the cursor.
- Non-scrollable: you can only fetch rows in the order determined by the [SELECT](https://www.mysqltutorial.org/mysql-select-statement-query-data.aspx) statement. You cannot fetch rows in the reversed order. In addition, you cannot skip rows or jump to a specific row in the result set.
- Asensitive: there are two kinds of cursors: asensitive cursor and insensitive cursor. An asensitive cursor points to the actual data, whereas an insensitive cursor uses a temporary copy of the data. An asensitive cursor performs faster than an insensitive cursor because it does not have to make a temporary copy of data. However, any change that made to the data from other connections will affect the data that is being used by an asensitive cursor, therefore, it is safer if you do not update the data that is being used by an asensitive cursor. MySQL cursor is asensitive.

You can use MySQL cursors in [stored procedures](https://www.mysqltutorial.org/getting-started-with-mysql-stored-procedures.aspx), [stored functions](https://www.mysqltutorial.org/mysql-stored-function/), and [triggers](https://www.mysqltutorial.org/mysql-triggers.aspx "MySQL Triggers").

First, declare a cursor by using the `DECLARE` statement:

```sql
DECLARE cursor_name CURSOR FOR SELECT_statement;
```

The cursor declaration must be after any [variable ](https://www.mysqltutorial.org/variables-in-stored-procedures.aspx "MySQL Variables in Stored Procedures")declaration. If you declare a cursor before the variable declarations, MySQL will issue an error. A cursor must always associate with a `SELECT` statement.

Next, open the cursor by using the `OPEN` statement. The `OPEN` statement initializes the result set for the cursor, therefore, you must call the `OPEN` statement before fetching rows from the result set.

```sql
OPEN cursor_name;
```

Then, use the `FETCH` statement to retrieve the next row pointed by the cursor and move the cursor to the next row in the result set.

```sql
FETCH cursor_name INTO variables list;
```

After that, check if there is any row available before fetching it.

Finally, deactivate the cursor and release the memory associated with it  using the `CLOSE` statement:

```sql
CLOSE cursor_name;
```

It is a good practice to always close a cursor when it is no longer used.

When working with MySQL cursor, you must also declare a `NOT FOUND` handler to handle the situation when the cursor could not find any row.

Because each time you call the `FETCH` statement, the cursor attempts to read the next row in the result set. When the cursor reaches the end of the result set, it will not be able to get the data, and a condition is raised. The handler is used to handle this condition.

To declare a `NOT FOUND` handler, you use the following syntax:

```sql

DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
```

The `finished` is a variable to indicate that the cursor has reached the end of the result set. Notice that the handler declaration must appear after variable and cursor declaration inside the stored procedures.

The following diagram illustrates how MySQL cursor works:

![mysql-cursor](https://user-images.githubusercontent.com/62965911/222632160-ccbd8671-684e-4176-8273-5baab4d4eed3.png)