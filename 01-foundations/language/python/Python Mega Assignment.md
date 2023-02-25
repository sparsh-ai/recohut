## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
> Python is called as general purpose language because it is not limited to a specific application or use case. In fact it is used in variety of applications like Web Development, Data Analytics, Data Science, Big Data, Application development, etc. Python is called high level language because it is easy to understand & closely resembles to English language.

Q2. Why is Python called a dynamically typed language?
> Unlike other languages in Python we do not require to declare datatype of a variable. Python dynamically identifies the datatype based on the data stored in the variable.

Q3. List some pros and cons of Python programming language?
> **Pros:**
> 1. Easy to learn
> 2. Easy to develop code/application
> 3. Wide variety of libraries.
> **Cons:**
> 1. Low performance
> 2. High memory requirement
> 3. Difficult to optimize

Q4. In what all domains can we use Python?
> Python can be used in Data Science, Data Engineering, Data Analytics, Web Development, Application development, etc.

Q5. What are variable and how can we declare them?
> Variable is a named entity which references to a memory location. We can store value in variables.
> e.g. a = 10

Q6. How can we take an input from the user in Python?
> We can use input function in Python to take user input.
> e.g name = input("Enter your name: ")

Q7. What is the default datatype of the value that has been taken as an input using input() function?
> The default datatype of the value from input function is string.

Q8. What is type casting?
> With the help of type casting we can change the dataype of a variable.

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
> We can use split() function to take multiple inputs from user.
> We can also use input function inside a loop to take input in each iteration of loop.

Q10. What are keywords?
> Keywords are predefined words in Python. We cannot use these words to name any variable, function, class, etc in our code.

Q11. Can we use keywords as a variable? Support your answer with reason.
> We cannot use keyword as a variable name. This may override the predefined purpose of the keyword & end up as an error.

Q12. What is indentation? What's the use of indentation in Python?
> Indentation is nothing but 4 consecutive spaces in Python. It is used to identify the section/block of code. It is used in functions, classes, loops, decision statements, etc

Q13. How can we throw some output in Python?
> We can throw output in python using print() function.
> e.g. print("Hello World!!")

Q14. What are operators in Python?
> Operators in Python are used to perform Arithmetic, Logical, Relational, etc operations on the variables.

Q15. What is difference between / and // operators?
> / -> The output of this operator is of float datatype.  
> // -> The output of this operator is of integer datatype.

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
	print('iNeuron' * 4)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

	num = int(input("Enter a number: "))
	if num % 2:
		print("Odd")
	else:
	print("Even")

Q18. What are boolean operator?
> Boolean operators are used to check if given condition is True or False.

Q19. What will the output of the following?
```
1 or 0
0 and 0
True and False and True
1 or 0 or 0
```

	1 or 0 -> 1
	0 and 0 -> 0
	True and False and True -> False
	1 or 0 or 0 -> 1

Q20. What are conditional statements in Python?
> Conditional statements execute the block of code contained inside it only if the specified condition is satisfied. They are used to control the flow of code.

Q21. What is use of 'if', 'elif' and 'else' keywords?
> if: Used to check the first condition.  
> elif: Used to check the nth condition in a nested if-else statement.  
> else: It is executed when all conditions in if & elif are not satisfied.

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

	age = int(input("Enter age: "))
	if age >= 18:
		print("I can vote")
	else:
		print("I can't vote")

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

	sum = 0
	for num in numbers:
		if num %2 == 0:
			sum = sum + num
	print(sum)

Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

	n1 = int(input("Enter 1st number: "))
	n2 = int(input("Enter 2nd number: "))
	n3 = int(input("Enter 3rd number: "))
	if n1 > n2 and n1 > n3:
		print(n1)
	elif n2 > n1 and n2 > n3:
		print(n2)
	else:
		print(n3)

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

	for num in numbers:
		if num > 500:
			break
		elif num < 151 and num % 5 == 0:
			print(num)

Q26. What is a string? How can we declare string in Python?
> String datatype in Python is used to store character or text data. We can declare string in Python using:
- Single quotes: 'Big Data'
- Double quotes: "Big Data"
- Triple quotes: ''' Big Data'''

Q27. How can we access the string using its index?
> We can access string or its part by providing the index no. or range of index nos.

    sample_str = 'Big Data Engineer'
    sample_str[0:3] -> 'Big'
    sample_str[ : : -1] -> 'reenignE ataD giB'

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```

    print(string[9:])

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```

    print(string[-1:-8:-1])

Q30. Reverse the string given in the above question.

    print(string[::-1])

Q31. How can you delete entire string at once?

    del string

Q32. What is escape sequence?
> Escape sequence ( \ ) is used to treat the special character as a part of string to avoid the errors. 
> e.g. string = "I opted for \"Big Data Engineering\" course"

Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```

    print("'iNeuron's Big Data Course'")
    # or
    print('\'iNeuron\'s Big Data Course\'')

Q34. What is a list in Python?
> List in python is a sequential datatype. It is used to store different types of data in a sequential manner.

Q35. How can you create a list in Python?

    sample_list = [1, 'Hi', True, 4.5]

Q36. How can we access the elements in a list?
> We can access the elements of list using index.

    sample_list = [1, 'Hi', True, 4.5]
    smaple_list[0] -> 1
    smaple_list[1] -> 'Hi'
    smaple_list[-1] -> 4.5

Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 

    print(lst[4][2])

Q38. Take a list as an input from the user and find the length of the list.

	# Method 1
    input_list = input('Enter , separated list items:').split(',')
    print(input_list)
    
    # Method 2
	input_list = eval(input('Enter the list with []: '))
	print(input_list)

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
```

    lst.insert(3, 'Big')
    # Output -> ["Welcome", "to", "Data", "Big", "course"]
    lst.insert(2, 'Big')
    # Output -> ["Welcome", "to", "Big", "Data", "course"]

Q40. What is a tuple? How is it different from list?
> Tuple is another type of sequential datatype. We can store different types of data inside it.
> The difference between Tuple & List is, List is mutable & Tuple is immutable.

Q41. How can you create a tuple in Python

	# Using () brackets
	tup1 = (1, 2, 'Big', 'Data', 2.0)

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
> We cannot add data after creating the Tuple as tuples are immutable.
> The only way to update the tuple is to overwrite the entire tuple with required changes.

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
> We can combine two tuples using + operator.

	tup1 = (1,2,3,4)
	tup2 = (5,6,7,8)
	combined_tuple = tup1 + tup2
	print(combined_tuple)

Q44. Take a tuple as an input and print the count of elements in it.

	tup1 = eval(input('Enter the tuple elements:'))
	print('Length of the tuple is:', len(tup1))

Q45. What are sets in Python?
> Set is a data type in pyton which is collection of unique elements. It is not indexed.

Q46. How can you create a set?

	# Method 1
	s1 = {1, 2, 3}
	
	# Method 2
	s2 = set([1,2,3])
	
Q47. Create a set and add "iNeuron" in your set.

	s1 = {'Big', 'Data', 'Engineer'}
	s1.add('iNeuron')

Q48. Try to add multiple values using add() function.
> We cannot add multiple values using add() function.

Q49. How is update() different from add()?
> update() function can add multiple elements in a set if iterable items like list, tuple, string or another set is providied to it as an argument.

Q50. What is clear() in sets?
> clear() function is used to delete all elements in set & make it empty.

Q51. What is frozen set?
> Frozen set is datatype in Pyton. It is similar to set except it is immutable.

Q52. How is frozen set different from set?
> Set is mutable while frozen set is immutable.

Q53. What is union() in sets? Explain via code.
> union() in set is used to combine the elements of two different sets.

	s1 = {'Big', 'Data', 'Engineer'}
	s2 = {1, 2, 3}
	print(s1.union(s2))
	# Output -> {1, 2, 3, 'Data', 'Engineer', 'Big'}

Q54. What is intersection() in sets? Explain via code.
> intersection() in sets is used to get only those elements which are present in both the sets.

	s1 = {'Data', 'Engineer', 'Software', 'Developer'}
	s2 = {'Software', 'Engineer', 'Data', 'Science'}
	print(s1.intersection(s2))
	# Output -> {'Data', 'Software', 'Engineer'}

Q55. What is dictionary in Python?
> dictionary data type in Python is used to store data in the form of key-value pairs.

Q56. How is dictionary different from all other data structures.
> dictionary stores data in key-value pair. While most of the sequential data types use indexes to access data dictionary uses keys.

Q57. How can we declare a dictionary in Python?

	# Empty dictionary
	dict1 = dict()
	dict2 = {}
	
	# Dictionary with elements
	dict3 = {'name':'Vivek', 'age':23, 'city':'Pune'}

Q58. What will the output of the following?
```
var = {}
print(type(var))
```
> <class 'dict'>

Q59. How can we add an element in a dictionary?
	
	dict1 = dict()
	
	# Method 1
	dict1.update({'name':'Vivek'})
	
	# Method 2
	dict1['age'] = 23
	
	print(dict1)
	# Output -> {'name': 'Vivek', 'age': 23}

Q60. Create a dictionary and access all the values in that dictionary.
	
	dict1 = {'name':'Vivek', 'age':23, 'city':'Pune'}
	print(dict1.values())
	# Output -> dict_values(['Vivek', 23, 'Pune'])

Q61. Create a nested dictionary and access all the element in the inner dictionary.

	dict1 = {'name':'Vivek', 'age':23, 'city':'Pune', 'skills': {'language':'Python', 'database':'MySQL'}}
	print(dict1.get('skills'))
	# Output -> {'language':'Python', 'database':'MySQL'}

Q62. What is the use of get() function?
> get() function is used to get value corresponding to the key given as an argument.

Q63. What is the use of items() function?
> items() function is used to get a list of key-value tuples of a dictionary

Q64. What is the use of pop() function?
> pop() function is used to get value corresponding to the key given as an argument. It also deletes that key-value pair from dictionary.

Q65. What is the use of popitems() function?
> It removes the last item inserted from a dictionary.

Q66. What is the use of keys() function?
> keys() function is used to get all the keys from a dictionary.

Q67. What is the use of values() function?
> values() function is used to get all the values from a dictionary.

Q68. What are loops in Python?
> Loops in Python are used to execute a block of code repeatedly until the condition is True.

Q69. How many type of loop are there in Python?
> In Python there are two types of loops
- for loop
- while loop

Q70. What is the difference between for and while loops?
> Mostly we use 'for loop' for a particular range and we use 'while loop' until a particular condition is True.

Q71. What is the use of continue statement?
> continue statement is used to skip the current execution of the loop & move to the next iteration.

Q72. What is the use of break statement?
> break statement is used to exit from the loop.

Q73. What is the use of pass statement?
> pass statement is used to temporarily execute the program without the block of code which we have planned to develop in future.

Q74. What is the use of range() function?
> range() function generates range of numbers which have been passed to it as an argument. 

Q75. How can you loop over a dictionary?
> We can use items() function to loop through a dictionary.

	dict1 = {'name':'Vivek', 'age':23, 'city':'Pune', 'skills': {'language':'Python', 'database':'MySQL'}}
	for k,v in dict1.items():
	    print('Key:', k, 'Value:', v)

### Coding problems
Q76. Write a Python program to find the factorial of a given number.

	def fact(num):
	    result = 1
	    for n in range(2, num+1):
		result = result * n
	    return result

	input_number = int(input('Enter a number: '))
	factorial = fact(input_number)
	print('Factorial of', input_number, 'is', factorial)

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

	p = int(input('Enter principal amount: '))
	r = int(input('Enter annual interest rate: '))
	t = int(input('Enter time (in years): '))

	simple_interest = (p * r * t) / 100
	print('Simple interest:', simple_interest)

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

	p = int(input('Enter principal amount: '))
	r = int(input('Enter annual interest rate: '))
	t = int(input('Enter time (in years): '))

	compound_interest = p * (1 + r / 100) ** t
	print('Compound interest:', compound_interest)

Q79. Write a Python program to check if a number is prime or not.

	num = int(input('Enter a number: '))

	if num == 0 or num ==1:
		   print('The input number', num, 'is not a prime number')
	else:
		for n in range(2, num):
			if num % n == 0:
				print('The input number', num, 'is not a prime number')
				break
		else:
			print('The input number', num, 'is a prime number')

Q80. Write a Python program to check Armstrong Number.

	num = input('Enter a number: ')
	result = 0

	for n in num:
		result += int(n) ** 3

	if int(num) == result:
		print(num, 'is a Armstrong number')
	else:
		print(num, 'is not a Armstrong number')

Q81. Write a Python program to find the n-th Fibonacci Number.

	num = int(input('Enter a number: '))
	fibonacci = [0, 1]

	if num == 0:
	    print('The nth Fibonacci numbre is 0')
	elif num == 1:
	    print('The nth Fibonacci numbre is 1')
	else:
	    for n in range(2, num + 1):
		result = fibonacci[-1] + fibonacci[-2]
		fibonacci.append(result)
	    print('The nth Fibonacci numbre is', fibonacci[-1])

Q82. Write a Python program to interchange the first and last element in a list.

	lst = [1, 2, 3, 4, 5]
	lst[0], lst[-1] = lst[-1], lst[0]
	print(lst)
	# Output -> [5, 2, 3, 4, 1]

Q83. Write a Python program to swap two elements in a list.

	lst = [1, 2, 3, 4, 5]
	i1 = int(input('Enter 1st index to swap: '))
	i2 = int(input('Enter 2nd index to swap: '))
	lst[i1], lst[i2] = lst[i2], lst[i1]
	print(lst)

Q84. Write a Python program to find N largest element from a list.

	lst = [3, 5, 1, 2, 4]
	n = int(input('Enter the no. of largest numbers required: '))
	lst.sort(reverse=True)
	print(lst[0:n])

Q85. Write a Python program to find cumulative sum of a list.

	lst = [3, 5, 1, 2, 4]
	cumulative_sum = 0
	for i in range(len(lst)):
	    cumulative_sum += lst[i]
	    lst[i] = cumulative_sum

	print(lst)
	# Output -> [3, 8, 9, 11, 15]

Q86. Write a Python program to check if a string is palindrome or not.

	s = input('Enter a string: ')
	reverse_s = s[ : : -1]

	if s.upper() == reverse_s.upper():
	    print('The string is palindrome ')
	else:
	    print('The string is not palindrome ')

Q87. Write a Python program to remove i'th element from a string.

	s = input('Enter a string: ')
	i = int(input('Enter index of element to be removed: '))
	s = s[:i] + s[i+1:]
	print(s)

Q88. Write a Python program to check if a substring is present in a given string.

	s = input('Enter a string: ')
	substr = input('Enter sub string: ')
	if s.find(substr) == -1:
	    print('Substring not present')
	else:
	    print('Substring is present')

Q89. Write a Python program to find words which are greater than given length k.

	s = input('Enter a string: ')
	k = int(input('Enter desired length: '))

	lst = s.split()
	for word in lst:
	    if len(word) > k:
		print(word)

Q90. Write a Python program to extract unquire dictionary values.

	test_dict = {'my': [1, 8, 9, 6], 'big': [10, 11, 9, 1], 'data': [6, 12, 10, 6], 'dict': [5, 2, 1]}
	result = []
	for v in test_dict.values():
	    result += v
	print(list(set(result)))

Q91. Write a Python program to merge two dictionary.

	dict1 = {'a':1, 'b':2, 'c':3}
	dict2 = {'d':4, 'e':5, 'f':6}

	dict1.update(dict2)
	print(dict1)
	# Output -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```

	lst = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
	my_dict = dict(lst)
	print(my_dict)
	# Output -> {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```

	lst = [9, 5, 6]
	result = []
	for num in lst:
		result.append((num, num**3))

	print(result)
	# Output -> [(9, 729), (5, 125), (6, 216)]

Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```

	test_tuple1 = (7, 2)
	test_tuple2 = (7, 8)

	result = []
	for i in test_tuple1:
		for j in test_tuple2:
			result.append((i, j))        
			result.append((j, i))        

	print(result)
	# Output -> [(7, 7), (7, 7), (7, 8), (8, 7), (2, 7), (7, 2), (2, 8), (8, 2)]

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```

	lst = [('for', 24), ('Geeks', 8), ('Geeks', 30)]

	def second_item(tup):
		return tup[1]

	lst.sort(key=second_item)
	print(lst)
	# Output -> [('Geeks', 8), ('for', 24), ('Geeks', 30)]

Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
	n = 5
	for i in range(1, n+1):
		print('* ' * i)
	
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```

	n = 5
	for i in range(1, n+1):
		print(' ' * (n-i), '*' * i)

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

	n = 5
	for i in range(1, n+1):
		print(' ' * (n-i), '* ' * i)

Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```

	n = 5
	for i in range(1, n+1):
		for j in range(1, i+1):
			print(j, end=' ')
		print()

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 
```

	import string
	alpha = list(string.ascii_uppercase)
	n = 5
	for i in range(1, n+1):
		print((alpha[i-1] + ' ') * i)
		
