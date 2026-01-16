# A set is collection data type in Python which is unordered and mutable.
# But it can only contain unique elements, means it does not allow duplicate values.
# Created just like a dictionary but we don't use key-value pairs in sets.

myset = {1, 2, 3, 4, 5}
print(myset) # Output => {1, 2, 3, 4, 5}
print(type(myset)) # Output => <class 'set'>

myset2 = {1, 2, 2, 3, 4, 4, 1} # with duplicate values
print(myset2) # Output => {1, 2, 3, 4} 