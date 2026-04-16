# In this part we'll look into the difference between and error and an exception
# And what are the most common built-in exceptions and how we raise and handle exceptions
# And also how we can define our own exceptions in Python 

# Syntax error: A syntax error makes the parser detects a syntactically incorrect statement
# There are many ways to raise a syntax error in python for eg:

# a = 10 print(a) this would raise an error as there is no new line between two statements
# And also if we forget to close a parenthesis or a quotation mark it would raise a syntax error as well
a = 5 + "10"
#print(a) # will give a type error
# Some more common build-in exceptions 
# Module not found error if we write a module that doesn't exists. eg = > import abcd
# Namer error
# x = 5
# y = z, here z is not defined
