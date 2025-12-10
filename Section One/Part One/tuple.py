# A Tuple is a collection which is ordered and unchangeable (immutable).
# Tuples are written with round brackets ().
# Main difference between a list and a tuple is that lists are mutable while tuples are immutable.
# Tuples can contain items of different data types and allow duplicate values.

# Creating a tuple
data = (1, "Hello", "Max", 3.14, True)
print(data)  # Output: (1, 'Hello', 'Max', 3.14, True)

print(type(data))  # Output: <class 'tuple'>

info = ("max")
print(type(info))  # Output: <class 'str'> coz this is not a tuple, it's a string as there is no comma

# We can also use the built-in tuple() function to create a tuple
my_tuple = tuple(["Max", 92, 3.14, False])
print(my_tuple)  # Output: ('Max', 92, 3.14, False)

# Accessing tuple items using indexing
print(data[0])  # Output: 1
print(data[3]) # Output: 3.14
print(data[-1]) # Output: True
print(data[-3]) # Output: Max

print("--------------------------------------")
# We can easily iterate through a tuple using a for loop
for item in data:
    print(item) # Output: 1 Hello Max 3.14 True

# Checking the length of the tuple
print("Length of data tuple:", len(data))  # Output: 5

# checking if an item exists in the tuple
if "Max" in data:
    print("Max is present in the tuple")  # Output: Max is present in the tuple
else:
    print("Max is not present in the tuple")

# Trying to change an item in the tuple will raise an error
# data[1] = "World"  This will raise a TypeError: 'tuple' object does not support item assignment
# However, we can convert the tuple to a list, modify it, and convert it back to a tuple


