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

#Checking if an item exits in the list or not
if "banana" in fruits:
    print("Banana is present in the fruits list.")  # Output: Banana is present in the fruits list.
else:
    print("Banana is not present in the fruits list.")