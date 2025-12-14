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
# eg:
# temp_list = list(data)
# print(type(temp_list))  Output: <class 'list'>

# And to count the number of occurences of an item in a tuple, we can use the count() method.
print("--------------------------------------")
numbers = (1, 2, 3, 2, 4, 2, 5)
count_of_twos = numbers.count(2)
print("Count of 2 in numbers tuple:", count_of_twos)  # Output: 3
# To find the index of the first occurrence of an item in a tuple, we can use the index() method.
index_of_2 = numbers.index(2) # Output: 1
print("Index of first occurrence of 2 in numbers tuple:", index_of_2)  # Output: 1

# Now we can easily convert a tuple to a list and vice versa
print(type(data))  # Output: <class 'tuple'>
data_list = list(data)
print(type(data_list))  # Output: <class 'list'>
data_tuple = tuple(data_list)
print(type(data_tuple))  # Output: <class 'tuple'>
print("--------------------------------------")

# Slicing a tuple
print(data) # Output: (1, 'Hello', 'Max', 3.14, True)
sliced_tuple = data[1:4]
print(sliced_tuple)  # Output: ('Hello', 'Max', 3.14)

# Negative slicing
a = ("a", "b", "c", "d", "e", "f")
neg_slic_one = a[-4:-1] # Output: ('c', 'd', 'e')
print(neg_slic_one) 

neg_slic_two = a[-3:] # Output: ('d', 'e', 'f')
neg_slic_three = a[:-3] # Output: ('a', 'b', 'c')
print(neg_slic_two)
print(neg_slic_three)




