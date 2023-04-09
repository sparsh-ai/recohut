# SQL String Functions

| Name                                                                                                    | Description                                                                              |
|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [CONCAT](https://www.mysqltutorial.org/sql-concat-in-mysql.aspx)                                        | Concatenate two or more strings into a single string                                     |
| [INSTR](https://www.mysqltutorial.org/mysql-instr/)                                                     | Return the position of the first occurrence of a substring in a string                   |
| [LENGTH](https://www.mysqltutorial.org/mysql-string-length/)                                            | Get the length of a string in bytes and in characters                                    |
| [LEFT](https://www.mysqltutorial.org/mysql-left-function/)                                              | Get a specified number of leftmost characters from a string                              |
| [LOWER](https://www.mysqltutorial.org/mysql-string-functions/mysql-lower/)                              | Convert a string to lowercase                                                            |
| [LTRIM](https://www.mysqltutorial.org/mysql-string-functions/mysql-ltrim-function/)                     | Remove all leading spaces from a string                                                  |
| [REPLACE](https://www.mysqltutorial.org/mysql-string-replace-function.aspx)                             | Search and replace a substring in a string                                               |
| [RIGHT](https://www.mysqltutorial.org/mysql-string-functions/mysql-right-function/)                     | Get a specified number of rightmost characters from a string                             |
| [RTRIM](https://www.mysqltutorial.org/mysql-string-functions/mysql-rtrim-function/)                     | Remove all trailing spaces from a string                                                 |
| [SUBSTRING](https://www.mysqltutorial.org/mysql-substring.aspx)                                         | Extract a substring starting from a position with a specific length.                     |
| [SUBSTRING_INDEX](https://www.mysqltutorial.org/mysql-string-functions/mysql-substring_index-function/) | Return a substring from a string before a specified number of occurrences of a delimiter |
| [TRIM](https://www.mysqltutorial.org/mysql-trim/)                                                       | Remove unwanted characters from a string.                                                |
| [FIND_IN_SET](https://www.mysqltutorial.org/mysql-find_in_set/)                                         | Find a string within a comma-separated list of strings                                   |
| [FORMAT](https://www.mysqltutorial.org/mysql-format-function/)                                          | Format a number with a specific locale, rounded to the number of decimals                |
| [UPPER](https://www.mysqltutorial.org/mysql-string-functions/mysql-upper/)                              | Convert a string to uppercase                                                            |

**LEFT, RIGHT, and LENGTH**

You can use LEFT to pull a certain number of characters from the left side of a string and present them as a separate string. The syntax is LEFT(string, number of characters).

When using functions within other functions, it's important to remember that the innermost functions will be evaluated first, followed by the functions that encapsulate them.

**TRIM**

The TRIM function is used to remove characters from the beginning and end of a string.

The TRIM function takes 3 arguments. First, you have to specify whether you want to remove characters from the beginning ('leading'), the end ('trailing'), or both ('both', as used above). Next you must specify all characters to be trimmed. Any characters included in the single quotes will be removed from both beginning, end, or both sides of the string. Finally, you must specify the text you want to trim using FROM.

**POSITION**

POSITION allows you to specify a substring, then returns a numerical value equal to the character number (counting from left) where that substring first appears in the target string.

Importantly, POSITION function is case-sensitive. If you want to look for a character regardless of its case, you can make your entire string a single by using the UPPER or LOWER functions.

**SUBSTR**

LEFT and RIGHT both create substrings of a specified length, but they only do so starting from the sides of an existing string. If you want to start in the middle of a string, you can use SUBSTR. The syntax is SUBSTR(*string*, *starting character position*, *# of characters*):

**CONCAT**

You can combine strings from several columns together (and with hard-coded values) using CONCAT. Simply order the values you want to concatenate and separate them with commas. If you want to hard-code values, enclose them in single quotes.

**Changing case with UPPER and LOWER**

Sometimes, you just don't want your data to look like it's screaming at you. You can use LOWER to force every character in a string to become lower-case. Similarly, you can use UPPER to make all the letters appear in upper-case:

**Turning strings into dates**

Dates are some of the most commonly screwed-up formats in SQL. This can be the result of a few things:

- The data was manipulated in Excel at some point, and the dates were changed to MM/DD/YYYY format or another format that is not compliant with SQL's strict standards.
- The data was manually entered by someone who use whatever formatting convention he/she was most familiar with.
- The date uses text (Jan, Feb, etc.) instead of numbers to record months.

In order to take advantage of all of the great date functionality, you need to have your date field formatted appropriately. This often involves some text manipulation, followed by a CAST.

**Turning dates into more useful dates**

Once you've got a well-formatted date field, you can manipulate in all sorts of interesting ways.

What if you want to include today's date or time? You can instruct your query to pull the local date and time at the time the query is run using any number of functions. Interestingly, you can run them without a FROM clause:

**COALESCE**

Occasionally, you will end up with a dataset that has some nulls that you'd prefer to contain actual values. This happens frequently in numerical data (displaying nulls as 0 is often preferable), and when performing outer joins that result in some unmatched rows. In cases like this, you can use COALESCE to replace the null values.