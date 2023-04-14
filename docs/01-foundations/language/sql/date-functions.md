# SQL Date Functions

Assuming you've got some dates properly stored as a date or time data type, you can do some pretty powerful things. Maybe you'd like to calculate a field of dates a week after an existing field. Or maybe you'd like to create a field that indicates how many days apart the values in two other date fields are. These are trivially simple, but it's important to keep in mind that the data type of your results will depend on exactly what you are doing to the dates.

When you perform arithmetic on dates (such as subtracting one date from another), the results are often stored as the interval data type—a series of integers that represent a period of time.

| Function                                                            | Description                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------|
| [CURDATE](https://www.mysqltutorial.org/mysql-curdate/)             | Returns the current date.                                                 |
| [DATEDIFF](https://www.mysqltutorial.org/mysql-datediff.aspx)       | Calculates the number of days between two DATE values.                    |
| [DAY](https://www.mysqltutorial.org/mysql-day/)                     | Gets the day of the month of a specified date.                            |
| [DATE_ADD](https://www.mysqltutorial.org/mysql-date_add/)           | Adds a time value to date value.                                          |
| [DATE_SUB](https://www.mysqltutorial.org/mysql-date_sub/)           | Subtracts a time value from a date value.                                 |
| [DATE_FORMAT](https://www.mysqltutorial.org/mysql-date_format/)     | Formats a date value based on a specified date format.                    |
| [DAYNAME](https://www.mysqltutorial.org/mysql-dayname/)             | Gets the name of a weekday for a specified date.                          |
| [DAYOFWEEK](https://www.mysqltutorial.org/mysql-dayofweek/)         | Returns the weekday index for a date.                                     |
| [EXTRACT](https://www.mysqltutorial.org/mysql-extract/)             | Extracts a part of a date.                                                |
| [LAST_DAY](https://www.mysqltutorial.org/mysql-last_day/)           | Returns the last day of the month of a specified date                     |
| [NOW](https://www.mysqltutorial.org/mysql-now/)                     | Returns the current date and time at which the statement executed.        |
| [MONTH](https://www.mysqltutorial.org/mysql-month/)                 | Returns an integer that represents a month of a specified date.           |
| [STR_TO_DATE](https://www.mysqltutorial.org/mysql-str_to_date/)     | Converts a string into a date and time value based on a specified format. |
| [SYSDATE](https://www.mysqltutorial.org/mysql-sysdate/)             | Returns the current date.                                                 |
| [TIMEDIFF](https://www.mysqltutorial.org/mysql-timediff/)           | Calculates the difference between two TIME or DATETIME values.            |
| [TIMESTAMPDIFF](https://www.mysqltutorial.org/mysql-timestampdiff/) | Calculates the difference between two DATE or DATETIME values.            |
| [WEEK](https://www.mysqltutorial.org/mysql-week/)                   | Returns a week number of a date.                                          |
| [WEEKDAY](https://www.mysqltutorial.org/mysql-weekday/)             | Returns a weekday index for a date.                                       |
| [YEAR](https://www.mysqltutorial.org/mysql-year/)                   | Return the year for a specified date                                      |
