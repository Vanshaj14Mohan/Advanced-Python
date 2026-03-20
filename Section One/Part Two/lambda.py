# In this part we will lean about lambda function and it's usage
# A lambda function is a small one line anonymous function that is derived that is defined without a 
# It's typically used when we need a simple function that is used only once in your code,
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
sorted_point = sorted(point2D) # Would sort the point2D from x paramter 
sorted_ypoint = sorted(point2D, key=lambda x: x[1])

print(point2D)
print(sorted_point) # [(1, 2), (5, -1), (10, 4), (15, 1)] sorted the x parameter while keeping y paramater unsorted
print(sorted_ypoint) # [(5, -1), (15, 1), (1, 2), (10, 4)] sorted the y parameter while keeping x paramater unsorted

# And here we could also create a normal function to sort the values based on the y parameter as well 
def sort_by_y(x):
    return x[1]

func_sorted_ypoint = sorted(point2D, key=sort_by_y) # passing the function as key here
print(func_sorted_ypoint) # [(5, -1), (15, 1), (1, 2), (10, 4)] same result as above

# Another example
points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sorted = sorted(points, key=lambda x: x[0] + x[1]) 
print(points_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]
print("---------------------------------------------")

# Now about map functions:
# Map functions transforms each element with a function
# It has a function as an argument and then a sequence eg a list 
#Syntax map(function, sequence)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b)) # [2, 4, 6, 8, 10]

# We can achieve the same output using list comprehension
c = [x*2 for x in a]
print(c) # [2, 4, 6, 8, 10], same output as above
print("-----------------------------------------------")

# For Filter function
#Same paramter as map function but filter function must return true or false, 
#and it returns all the elements for which the function returns to true
demo = [1, 2, 3, 4, 5]
fil = filter(lambda x: x%2 == 0, demo)
print(list(fil)) # [2, 4], only even number

#using list omprehension
d = [ x for x in demo if x%2 == 0]
print(list(d)) # [2, 4] same output as above

demo_two = [1, 2, 3, 4, 5, 6, 7]
fil_two = filter(lambda x: x%2!=0, demo_two)
print(list(fil_two)) # [1, 3, 5, 7], only odd numbers

e = [ x for x in demo_two if x%2!= 0]
print(list(e)) #  [1, 3, 5, 7] same output as above

# Reduce function, It also takes a function and sequence and repeatedly applies the function to the element and returns a single value
from functools import reduce
red = [1, 2, 3, 4, 5, 6, 7]
prod_red = reduce(lambda x,y: x*y, red)
print(prod_red) #5040


