# A dictionary is a collection datatype which is unordered and mutable, It consists of a collection of key-value pairs
# So each key value pair maps the key to it's associated value.

my_dict = {"name": "John", "age": 27, "city": "New York", "gender": "Male"}
print(my_dict)

#We can also used dict function to create a dictionary
sample_dict = dict(name="Adam", city="New Jersey", age=28, gender="Male") #Putting keys as arguments
print(sample_dict)
print(type(sample_dict)) # Dict

#Accesing Values in a Dictionary
print("For accesing names:", my_dict["name"]) #John
print("For accesing names:", sample_dict["name"]) #Adam

# A dictionary is mutable, we can change it's associated values by using their keys
my_dict["age"] = 29 #new value for age key
print("Update value of age key", my_dict["age"]) # 29
#or we can also change it's keys
my_dict["email"] = "adam@1234gmail.com"
print("Updated dictionary", my_dict)
#And it will overwrite the value if the key already exists 
print("----------------------------------------------------")

#Now to delete a key value pair, we use del keyword here
del my_dict["city"]
print("After deleting city key: ", my_dict)

del my_dict["email"]
print("After deleting email key: ", my_dict)

# Can also use pop() method in order to remove specific key-value pair
my_dict.pop("gender") #removing gender key
print("Afterdeleting gender key using pop(): ", my_dict)

new_dict  = {"name": "John", "age": 27, "city": "New York", "gender": "Male", "email": "john@1234gmail.com"}
#now to verify if a key is present in the dictonary
# There are two ways to do this:
# Using "in" keyword

#Checking if age is present or not
if "age" in new_dict:
    print("Age is present")
else:
    print("Not present")

#2: Using get() method
if new_dict.get("city"):
    print("City is present")
else:
    print("City is not present")

# Or we can use try and except block to handle error if key is not present
try:
    print(new_dict["country"]) #country key is not present
except:
    print("Country key is not present")
# Will show not present message instead of giving an error

try:
    print("Name is:", new_dict["name"]) #name key is there
except:
    print("Name key is not present")
# Will give the value of name key


