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
print(count.most_common(2)) # 2 represent the nu,ber of most common elements we want to see: [('d', 4), ('a', 2)]
print(count.keys()) # Output: dict_keys(['a', 'b', 'c', 'd', 'e', 'g', 'h'])
print(count.values()) # Output: dict_values([2, 2, 1, 4, 1, 1, 1])
print("-------------------------------------------------------")
