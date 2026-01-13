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

