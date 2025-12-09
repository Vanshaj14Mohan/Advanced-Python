# A Tuple is a collection which is ordered and unchangeable (immutable).
# Tuples are written with round brackets ().
# Main difference between a list and a tuple is that lists are mutable while tuples are immutable.
# Tuples can contain items of different data types and allow duplicate values.

# Creating a tuple
data = (1, "Hello", "Max", 3.14, True)
print(data)  # Output: (1, 'Hello', 'Max', 3.14, True)

print(type(data))  # Output: <class 'tuple'>

tuple = ("max")
print(type(tuple))  # Output: <class 'str'> coz this is not a tuple, it's a string as there is no comma