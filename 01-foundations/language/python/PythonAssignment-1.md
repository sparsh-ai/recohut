## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
> Python is called as general purpose language because it is not limited to a specific application or use case. In fact it is used in variety of applications like Web Development, Data Analytics, Data Science, Big Data, Application development, etc. Python is called high level language because it is easy to understand & closely resembles to English language.

Q2. Why is Python called a dynamically typed language?
> Unlike other languages in Python we do not require to declare datatype of a variable. Python dynamically identifies the datatype based on the data stored in the variable.

Q3. List some pros and cons of Python programming language?
> **Pros:**
> 1. Easy to learn
> 2. Esay to develop code/application
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

Q12. What is indentation? What's the use of indentaion in Python?
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
> Boolean opeartors are used to check if given condition is True or False.

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
> Conditional statements extecute the block of code contained inside it only if the specified condition is satisfied. They are used to control the flow of code.

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
