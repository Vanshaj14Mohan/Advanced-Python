# Itertools module is a collection of tools for handling iterators:
# They are used to create iterators for efficetive looping.
# In short iteators are data types that can be used in a for loop, but they don't store their content in memory:
# Example are list, sets, tuple, strings, dictionaries etc.
# The itertools offers some advanced tools for handling iterators such as product, permutations, combinations, accumulate, groupby and infinite 
# Iterators like count, cycle and repeat:
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat
# 1: product:
# Used to compute the cartesian product of input iterables:
a = [1, 2, 3]
b = [4, 5, 6]
c = ["a"]
d = ["b"]
pro = product(a, b) # we can add repeat argument to tell the number of time we want to repeat the input iterables:
print(pro) # <itertools.product object at 0x0000016CAA380640>
prod = product(c, d, repeat=2)
print(prod) # <itertools.product object at 0x000002792C126C80>
# Convert it to list to see the output:
print(list(pro)) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
print(list(prod)) # [('a', 'b', 'a', 'b')]