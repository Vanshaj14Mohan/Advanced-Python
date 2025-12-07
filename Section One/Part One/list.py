# List is a built-in data type in Python that represents an ordered collection of items.
# Lists are mutable, meaning their contents can be changed after they are created.

fruits = ["apple", "banana", "mango", "orange"]
print(fruits)  # Output: ['apple', 'banana', 'mango', 'orange']

#Creating an empty list using list() function
empty_list  = list()
print(empty_list)  # Output: []

# A list can contain items of different data types and it also allows duplicate values.
mixed_list = [1, "hello", 3.14, True, "hello"]
print(mixed_list)  # Output: [1, 'hello', 3.14, True]

#Accesing list items using indexing
print(fruits[0]) # Output: apple

item = fruits[2]
print(item) # Output: mango

# Negative indexing to acces items from the end of the list
print("Last Negative Index from back:", fruits[-1]) # Output: orange
print("Last Second Negative value from the back:", fruits[-2]) # Output: mango
print("--------------------------------------")

#if you want to iterate through the list 
for fruit in fruits:
    print(fruit)

# checking the length of the list
print("Length of fruits list:", len(fruits))  # Output: 4
print("--------------------------------------")

#Checking if an item exits in the list or not
if "banana" in fruits:
    print("Banana is present in the fruits list.")  # Output: Banana is present in the fruits list.
else:
    print("Banana is not present in the fruits list.")

if "lemon" in fruits:
    print("Lemon is present in the fruits list.")
else:
    print("Lemon is not present in the fruits list.")  # Output: Lemon is not present in the fruits list.

print("--------------------------------------")

# Append items to the list using append() method
fruits.append("grape")
print("After appending grape:", fruits)  # Output: ['apple', 'banana', 'mango', 'orange', 'grape']

# Now if we want to insert an item at a specific position we can use insert() method
fruits.insert(1, "kiwi")
print("After inserting kiwi at index 1:", fruits)  # Output: ['apple', 'kiwi', 'banana', 'mango', 'orange', 'grape']

# Now if we want to remove last item from the list we can use pop() method
removed_item = fruits.pop()
print("After popping last item:", fruits)  # Output: ['apple', 'kiwi', 'banana', 'mango', 'orange']
print("Removed item:", removed_item)  # Output: grape

# We can also remove an specific item at a specific index using remove() method
fruits.remove("mango")
print("After removing mango:", fruits)  # Output: ['apple', 'kiwi', 'banana', 'orange']

# We can also reverse the list using reverse() method
fruits.reverse()
print("After reversing the list:", fruits)  # Output: ['orange', 'banana', 'kiwi', 'apple']

# And if we want to clear the entire list we can use clear() method
fruits.clear()
print("After clearing the list:", fruits)  # Output: []

# And we we are using numbers we can even sort the list using sort() method
numbers = [-1, -5, -3, 2, 4, 8, 10, 7]
print("Original numbers list:", numbers) # Output: [-1, -5, -3, 2, 4, 8, 10, 7]
numbers.sort()
print("Sorted numbers list:", numbers ) # Output: [-5, -3, -1, 2, 4, 7, 8, 10]

# If you want to get a sorted version of the list without modifying the original list you can use sorted() function
print("Original numbers list after using sorted():", numbers ) # Output: [-5, -3, -1, 2, 4, 7, 8, 10]
print("------------------------------------------------")

# Basic tricks
num = [0] * 5
print("List with 5 zeros:", num)  # Output: [0, 0, 0, 0, 0]

num_one = [1,1,1,1,1]
#now adding these two lists
result = num + num_one
print("Result after adding two lists:", result)  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
print("------------------------------------------------")

# Slicing a list
# Slicing is a technique to extract a portion of a list by specifying a range of indices.
letters = ["a", "b", "c", "d", "e"]
print("Original Letters List:", letters) # Output: ['a', 'b', 'c', 'd', 'e']

# Slicing from index 1 to 4 (4 is excluded)
slice1 = letters[1:4]
print("Sliced Letters from index 1 to 4:", slice1) # Output: ["b", "c", "d"]

# Slicing from the beginning to index 3 (3 is excluded)
slice2 = letters[:3] # :3 means from start to index 3 (3 is excluded)
print("Sliced Letters from index 0 to 3:", slice2) # Output: ["a", "b", "c"]

# Slicing from begining to end
slice3 = letters[1:] # 1: means from index 1 to end
print("Sliced Letters from index 1 to end:", slice3) # Output: ["b", "c", "d", "e"]

# Reverse slicing
slice4 = letters[::-1] # ::-1 means from end to start (reversing the list)
print("Reversed Letters List", slice4) # Output: ["e", "d", "c", "b", "a"]

# Optional stop parameter in slicing
# Slicing with step value
slice_step = letters[0:5:2] # 0 to 5 with step of 2
print("Sliced Letters from index 0 to 5 with step 2:", slice_step) # Output: ["a", "c", "e"]

#optionals step parameter in slicing
print(letters[1::1]) # Output: ['b', 'c', 'd', 'e'] means from index 1 to end with step of 1
print(letters[::2]) # Output: ['a', 'c', 'e'] means from start to end with step of 2
print("------------------------------------------------")

# Copying a list
# There are multiple ways to copy a list in Python.
original_list = [1,2,3,4,5]
copy_list = original_list.copy()  # Using copy() method
print("Original List:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Copied List using copy() method:", copy_list) # Output: [1, 2, 3, 4, 5]

#Now if we edit the copied list it will not affect the original list,
# but if we just assign the original list to a new variable it will create a reference to the original list.
reference_list = original_list # Creating a reference
reference_list.append(6)
print("Original List after modifying reference list:", original_list)  # Output: [1, 2, 3, 4, 5, 6]
print("Reference List after appending 6:", reference_list) # Output: [1, 2, 3, 4, 5, 6]
print("------------------------------------------------")

# Now using slicing to copy a list
sliced_copy = original_list[1:3] # Slicing from index 1 to 3 (3 is excluded)
print("Sliced Copy of Original List from index 1 to 3:", sliced_copy) # Output: [2, 3]
print("Original List remains unchanged:", original_list)  # Output: [1, 2, 3, 4, 5, 6]
print("------------------------------------------------")

# List comprehension
# List comprehension is a concise way to create lists using a single line of code.
squares = [x**2 for x in range(1, 6)]
print("List of squares using List Comprehesnion:", squares)  # Output: [1, 4, 9, 16, 25]


