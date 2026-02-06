# In this we will learn about collections in python:
# Collections are basically built-in data structures which are used to store and manipulate data in an efficient way:
# Five main types of collections module present in python are:
# 1: Counter
# 2: namedtuple
# 3: OrderedDict
# 4: defaultdict
# 5: deque

# Starting with Counter:
# Counter is basically a subclass of dictionay used to count the number of occurences of elements in a collection:
# It displays the count of each elements in th form of dictionary where keys are the elements and values are the count of those elements:
from collections import Counter # Need to import Counter from collections module
test = "Collections"
counter = Counter(test) # Creating a counter object
print(counter) # Output: Counter({'o': 2, 'l': 2, 'C': 1, 'e': 1, 'c': 1, 't': 1, 'i': 1, 'n': 1, 's': 1})

test_two = "abcdabdddegh"
count = Counter(test_two)
print(count.items()) # Output: dict_items([('a', 2), ('b', 2), ('c', 1), ('d', 4), ('e', 1), ('g', 1), ('h', 1)])
print(count.most_common(2)) # 2 represent the number of most common elements we want to see: [('d', 4), ('a', 2)]
print(count.most_common(1)[0][0]) #[0][0] used to get most common element only in d:
print(count.keys()) # Output: dict_keys(['a', 'b', 'c', 'd', 'e', 'g', 'h'])
print(count.values()) # Output: dict_values([2, 2, 1, 4, 1, 1, 1])
print(count.elements()) # Returns an iterator showing all elements and their : <itertools.chain object at 0x000001F1D8F788E0>
# We can convert this this iterator to list to access all the elements:
print(list(count.elements())) #Output: ['a', 'a', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'e', 'g', 'h']
print("-------------------------------------------------------")

# 2: namedTuple:
# basically a subclass of tuple that allows us to create tuple with named fields:
from collections import namedtuple
# Example:
Point = namedtuple("Point", ["x", "y"]) # Here we have created a namedtuple know as Point with fields x and y:
# Can also be defined as Point = namedtuple("Point", "x, y") # the correct way to define a namedtuple is to pass the field names as list or strings separated by commas:
p1 = Point(2, -5)
print(p1)
# Now accessing the fields
print(p1.x, p1.y) # 2 -5
# We can also access the fields using index just like in normal tuple:
print(p1[0], p1[1]) # 2 -5
# Can also use _fields to get the fields names:
print(p1._fields) # ('x', 'y')
print("-------------------------------------------------------")

# 3: OrderedDict:
# It's a subclass of dictionary that basically maintains the order of keys as they were inserted:
# They are like regular dictionaries but here they remember the order that the items were inserted:
from collections import OrderedDict
# Example case:
ord_dict = OrderedDict()
ord_dict["a"] = 1
ord_dict["b"] = 2
ord_dict["c"] = 3
ord_dict["d"] = 4
ord_dict["e"] = 5
print(ord_dict) # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

#Using a normal dictionary:
sample = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(sample) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# In python 3.7 and above, the regular dictionaries also maintain the order of insertion, so the output will be same 
# as ordered dict but in older versions of python the order is not maintained in regular dictionaries:

# Can use popitem() method to remove the last item from ordereddict:
ord_dict.popitem() # ("e": 5) will be removed
print(ord_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# Can use move_to_end() method in order to move an item to the end of the ordered dict:
ord_dict.move_to_end("c") # Now c will be moved to the end of ord_dict:
print(ord_dict) # OrderedDict([('a', 1), ('b', 2), ('d', 4), ('c', 3)])

# Now we can also move an item to the beginning by passign last = False in move_to_end() method:
ord_dict.move_to_end("d", last=False) # Now d will be moved to the beginning od ord_dict:
print(ord_dict) # OrderedDict([('d', 4), ('a', 1), ('b', 2), ('c', 3)])

# Can also pop() an item by it's key:
ord_dict.pop("a") # A would be removed from ord_dict:
print(ord_dict) # OrderedDict([('d', 4), ('b', 2), ('c', 3)])
print("-------------------------------------------------------")

