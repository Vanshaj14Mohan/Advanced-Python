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