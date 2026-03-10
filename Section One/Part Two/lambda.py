# In this part we will lean about lambda function and it's usage
# A lambda function is a small one line anonymous function that is derived that is defined without a 
# A lambda function is typically used when we need a simple function that is used only once in your code,
# or it can be used as an arguments to higher order functions, functions that take functions as arguments
# They are used along built-in functions sorted map, filter, reduce and so on.
# Syntax for writing a lambda expression:
# lambda arguments: expression

add_no = lambda x: x+ 20
print(add_no(10)) # 30, pretty much same as a normal function

def addno(x):
    return x + 10

print(addno(10)) # 20

# Lambda functions can have multiple arguments as well
mult = lambda x,y: x*y
print(mult(5, 7)) # 35

point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

sorted_point = sorted(point2D)

print(point2D)
print(sorted_point)