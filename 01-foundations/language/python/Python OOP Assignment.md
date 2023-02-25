## Python OOP Assignment
Q1. What is the purpose of Python's OOP?
> Python OOP concept helps us to solve complex problems by using objects(Similar to real world)  
> OOP has other advantages like Encapsulation, Ploymorphism, Abstraction, Inheritance, etc.  

Q2. Where does an inheritance search look for an attribute?
> In an inheritance the attribute is first serached in the class the object was created. Later it will search in the upper super classes.

Q3. How do you distinguish between a class object and an instance object?
> Instance object is always associated with self keyword & it is bound yo a particular object.  
> Class object is bound to a class & hence self keyword is not used.  

Q4. What makes the first argument in a class’s method function special?
> In a class the first argument is self keyword. It is nothing but a refernce to the object who called that method.

Q5. What is the purpose of the init method?
> \__init\__() method in a class is a constructor of that calss.  
> It gets called as soon as an object is created.  

Q6. What is the process for creating a class instance?
> Class instance can be created anywhere in the body of class.  
> We can declare & define it similar to any other variable declartion without the self keyword.  

Q7. What is the process for creating a class?
> Class is created using the *class* keyword.
```
# Creating blank class
class Data():
	pass
	
# Creating a class with a constructor
class Data()
	def __init__(self):
		print("Welcome to the Data class")
```

Q8. How would you define the superclasses of a class?
> The super classes of the class are the parent class from which the sub-class was created.  
> The charecteristics of super class are inherited in sub-class.  

Q9. What is the relationship between classes and modules?
> Classes in Python are the collection of attributes & methods. These can be used only by the objects of the class or the derived class.  
> Modules in Python are a way to organize code. It can consists of sunctions, classes, methods, etc. We can import the module and use it wherever required.  

Q10. How do you make instances and classes?
> Class is created using the *class* keyword & we can define the class attributes & methods inside it.  
> To create instances of a Class we need to create the class objects by passing the arguments if required.  
```
# Creating a class
class Employee():
	company_name = "Google"

	def __init__(self, name, country):
		self.name = name
		self.country = country

	def display(self):
		print(f"My name is {self.name} and I am from {self.country}, working at {Employee.company_name}")
		
# Creating instance/object
emp_1 = Employee('Vivek', 'India')
emp_1.display()
```

Q11. Where and how should be class attributes created?
> Class attributes should be created directly inside the body of Class.  
> We can aslo declafe a class attribute outside the class using Class name as prefix.
```
class Example():
	# Class attribute
	count = 5
	def __init__(self):
		pass
print(Example.count) # Output -> 5
# Class attribute declared outside of the class
Example.type = 'Outside'
print(Example.type)
```

Q12. Where and how are instance attributes created?
> Instance attributes are mostly created inside the constructor. It can also be created in a method.
> Note that self keyword is required to create the instance attribute.
> We can also create the instance attributes outside the class using the object name as prefix.
```
class Person():
	
    def __init__(self, name):
        # Instance attribute declared inside the class
        self.name = name

    def disp(self):
        print("Name:", self.name, "& Age:", self.age)

e1 = Person('abc')
e2 = Person('xyz')

# Instance attributes declared outside of the class
e1.age = 20
e2.age = 30

e1.disp() # Outout -> Name: abc & Age: 20
e2.disp() # Output -> Name: xyz & Age: 30
```

Q13. What does the term "self" in a Python class mean?
> self keyword in python is used to reference the object of the class which instanciated.

Q14. How does a Python class handle operator overloading?
> In Python operator overloading is handled based on the datatype of the operands/arguments passed to it.

Q15. When do you consider allowing operator overloading of your classes?
> Whenever we need to handle the data differently based on the datatype of the operands, we will go ahead with operator overloading.

Q16. What is the most popular form of operator overloading?
> '+' operator is most popular form of operator overloading. It is used to add integers or floats and at the same time it is also used to concatinate strings.

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
> Inheritance & Polymorphism are the two most important concepts in Python OOP.

Q18. Describe three applications for exception processing.
1. To handle divide by zero  
2. To handle index out of range error
3. To handle wrong key name for dictionaries  

Q19. What happens if you don't do something extra to treat an exception?
> The program will throw error & stop the further execution if we do not handle the exceptions.

Q20. What are your options for recovering from an exception in your script?
> We can use try & except to handle the exception in our script.

Q21. Describe two methods for triggering exceptions in your script.
1. Dividing a value by zero will trigger exception.  
2. Accessing a dictionary using wrong key will trigger exception.  

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of  
whether or not an exception exists.
> finally is used to execute the code regardless of whether or not an exception exists.

Q23. What is the purpose of the try statement?
> try statement is used to check the error-prone code.

Q24. What are the two most popular try statement variations?
1. try/except/else  
2. try/except/finally

Q25. What is the purpose of the raise statement?
> raise statement is used to raise user defined exceptions.

Q26. What does the assert statement do, and what other statement is it like?
> The assert statement generates AssertionError if a condition is False. It is similar to raise statement.

Q27. What is the purpose of the with/as argument, and what other statement is it like?
> with statement is used to handle file management in Python. It is similar to except statement as it handles the errors related to files access.

Q28. What are *args, **kwargs?

- *args -> It is used to accept any number of arguments to the function
- **kwrags -> It is used to accept any no. of arguments in any sequence in the form of key-value pairs.

Q29. How can I pass optional or keyword parameters from one function to another?
> We can pass optional or keyword parameters from one function to another using *args & **kwargs
```
def func1(*args, **kwrags):
	print('func1() passing optional or keyword parameters to func2()')
	func2(*args, **kwrags)

def func2(*args, **kwrags):
	pass

```

Q30. What are Lambda Functions?
> lambda functions are one line functionswhich can accept any no. of arguments but can have only on expression

Q31. Explain Inheritance in Python with an example?
> Inheritance in Python is used to inherit the properties of parent class into the child class.

```
class DataDomain():
    basic_skills = ['Python', 'SQL', 'Problem Solving']
    tools = [] # Default blank list of tools to avoid errors as it is specific only for DataAnalysis calss
    def __init__(self, name, advance_skills):
        self.name =name
        self.advance_skills = advance_skills

    def skills(self):
        print(f"{self.name} has these skills -> {self.basic_skills + self.advance_skills + self.tools}")

class DataEngineering(DataDomain):
    pass

class DataAnalysis(DataDomain):
    def __init__(self, name, advance_skills, tools):
        super().__init__(name, advance_skills)
        self.tools = tools

class DataScience(DataDomain):
    def __init__(self, name, advance_skills):
        super().__init__(name, advance_skills)

emp1 = DataDomain('Dave', ['Management', 'Leadership'])
emp1.skills()

emp2 = DataEngineering('Mike', ['Scala', 'Hadoop', 'Spark'])
emp2.skills()

emp3 = DataAnalysis('Tom', ['Stats', 'Dashboarding'], ['Tableau', 'PowerBI'])
emp3.skills()
```

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?
> The version of func() from class A will be called because while inherting the class C we have written A before B.

Q33. Which methods/functions do we use to determine the type of instance and inheritance?
> Python has two built-in functions that work with inheritance:  
> 1. Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.  
> 2. Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

Q34.Explain the use of the 'nonlocal' keyword in Python.
- nonlocal keyword is mostly used in nested functions.  
- It is used in inner function to declare its variable as nonlocal so that its value can be used by the outer function.

Q35. What is the global keyword?
- global keyword id used to declare a global variable inside function.  
- We can access this global variable outside the function as well.
