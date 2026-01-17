# A set is collection data type in Python which is unordered and mutable.
# But it can only contain unique elements, means it does not allow duplicate values.
# Created just like a dictionary but we don't use key-value pairs in sets.

myset = {1, 2, 3, 4, 5}
print(myset) # Output => {1, 2, 3, 4, 5}
print(type(myset)) # Output => <class 'set'>

myset2 = {1, 2, 2, 3, 4, 4, 1} # with duplicate values
print(myset2) # Output => {1, 2, 3, 4} 

# Can also create a set using set() function and can use a list or any other iterable to create a list 
sample_set = set([1, 2, 3, 1, 2, 3, 4, 4, 5])
print(sample_set) # Output => {1, 2, 3, 4, 5} 
# Passing a string now
string_set = set("Python")
print(string_set) # Output can be in any order as set are unordered:

# And if we crate an empty set it would be considered a dictionary
empty_set = {}
print(type(empty_set)) # Output => <class 'dict'>
print("---------------------------------------------------")

# Now adding and removing elements in a set
demo_set = set()
demo_set.add(1)
demo_set.add(2)
demo_set.add(3)
demo_set.add(4)
demo_set.add(5)
print(demo_set) # Output => {1, 2, 3, 4, 5}

# Now to remove, we can use remove() or even discard() method too.
demo_set.remove(1)
demo_set.remove(3)
demo_set.discard(5) # using discard here
print(demo_set) # Output => {2, 4}

#NOTE: And if we try to remove an element which is actually not present in the set, it will raise an key error.
#Can use clear() to empty the set, or use pop() this will remove and return an arbitrary value from the set.
demo_set.clear()
print(demo_set) #Output => set()
print("---------------------------------------------------")

# Now iterating through a set, we can use a for loop
for i in myset:
    print(i)

#Checking if an element is present in our set or not, using "in" keyword
if 1 in myset:
    print("1 is present in myset")
else:
    print("Not present")

if 6 in myset:
    print("6 is present")
else:
    print("6 is not present")

# Now some operations on sets that are Union, Intersection, Difference and symmetric difference
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
prime = { 2, 3, 5, 7, 11}

# Now for union, in this we can use union() method or "|" operator
print(even.union(odd)) # Output => {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(even | prime) # Output => {2, 3, 5, 6, 7, 8, 10, 11}

# Now for intersection, in this we can use intersection or "&" operator
print(odd.intersection(prime)) #Output => {3, 5, 7}
print(even & prime) # Output => {2}

# And for difference we can use difference() method or "-" operator
print(even.difference(prime)) # Output => {8, 10, 4, 6}
print(even - odd) # Output = > {2, 4, 6, 8, 10}
print(prime - even) # Output => {11, 3, 5, 7}


