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

# Now for difference we can use difference() method or "-" operator
# In difference we see all the elements which are present in first set but not in second set.
print(even.difference(prime)) # Output => {8, 10, 4, 6}
print(even - odd) # Output = > {2, 4, 6, 8, 10}
print(prime - even) # Output => {11, 3, 5, 7}

# And for symmetric difference we use symmetric_difference() method or "^" operator
# In symmetric difference we can get all the elements which are in either of the sets but not in both sets.
print(odd.symmetric_difference(prime)) # Output => {1, 2, 9, 11}
print(even ^ prime) # Output => {3, 4, 5, 6, 7, 8, 10, 11}
print(even ^ odd) # Output => {1, 2, 3, 4, 5, 6, ,7 8, 9, 10}
print("---------------------------------------------------")

# And to update a set with numerous elements we can use update() method
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.update(set2)) # Would return none as it updates set1 in place
print(set1) # Output => {1, 2, 3, 4, 5, 6}
# And interection_update(), difference_update(), symmetric_update() methods which we can aslo use to update the set with required operations:
# They work same as above methods but they just update the set in place.
#NOTE: We can use update() method with any iterable like list, tuple or even strings. 

#NOTE: The same copy logic applies here just like in list:
# Using copy() method and assigning a variable both will have different impact
# Now if we edit the copied set it will not affect the original set,
# but if we just assign the original set to a new variable it will create a reference to the original set.
copyset1 = {"a", "b", "c"}

copyset2 = copyset1
copyset2.add("d")
print(copyset1)
print(copyset2) # Both will have {"a", "b", "c", "e"}

# But when we use copy() method it won't effect the original set
copyseta = {1, 2, 3, 4} 
copysetb = copyseta.copy()

copysetb.add(5)
print(copyseta) #{1, 2, 3, 4}
print(copysetb) #{1, 2, 3, 4, 5}
print("--------------------------------------------------------")

# Now checking subset, superset and disjoint methods
# A subset is basically a collection of elements derived from a larger set or sequence, 
# where every element in the smaller collection is also present in the original one.
# Or in simple every element in the subset must exist in the larger set:
# Denoted with the subset() method or with the "<=" operator
pack1 = {"apple", "mango", "oranges", "kiwi"}
pack2 = {"guava", "strawberry", "banana", "apple"}
pack3 = {"apple", "oranges", "mango", "kiwi",}
print(pack2.issubset(pack1)) # Would give false
print(pack3.issubset(pack1)) # Would give true

# Now for superset: basically a set that contains all the elements of another set (the subset), and possibly more
# Can be denoted using superset() method or using ">=" or ">" operator
num1 = {1,2,3,4,5}
num2 = {2,4}
num3 = {2,4, 5,1}
num4 = {1,5}
print(num1.issuperset(num2)) # Would give true [as contains 2, 4 from num2]
print(num3.issuperset(num2)) # Would give true 
print(num3 >= num4) # Would give true
print(num4 > num3) # Would give false [as num4 doesn't have 2,4 from num3]

# Now for disjoint: in-short two sets are disjoint if they have no elements in common
# Basically their intersection is an empty set
# Denoted using isdisjoint() method or 
set_a = {"a", "b", "c"}
set_b = {"d", "e", "f"}
set_c = {"a", "b", "h"}

print(set_a.isdisjoint(set_b)) # Would give true (no common elements)
print(set_b.isdisjoint(set_c)) # Would give true
print(set_a.isdisjoint(set_c)) # Would give false ( "a", "b" are common here)
print(set_c.isdisjoint(set_b)) # Would give true

# Especial one: frozenset, it's also a collection data type and it's just an immutable version of a normal set
a = frozenset[1, 2, 3, 4]
#a.add(5) # this would gove error as frozensets are immutable, so no addition, removing or updation can happen
print(a)





