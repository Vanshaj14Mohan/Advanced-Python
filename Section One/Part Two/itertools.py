# Itertools module is a collection of tools for handling iterators:
# They are used to create iterators for efficetive looping.
# In short iteators are data types that can be used in a for loop, but they don't store their content in memory:
# Example are list, sets, tuple, strings, dictionaries etc.
# The itertools offers some advanced tools for handling iterators such as product, permutations, combinations, accumulate, groupby and infinite 
# Iterators like count, cycle and repeat:

from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat # Importing all together
# 1: product:
# Used to compute the cartesian product of input iterables:
print("For Product")
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
print("-----------------------------------------------------")

# 2: permutations:
# Mainly used to generate all possible permutations of a given iterable:
print("For Permutations")
toss = ["Head", "Tail"]
per = permutations(toss) # Shows all possible outcome of tossing a coin:
print(list(per)) # [('Head', 'Tail'), ('Tail', 'Head')]
# Can also specify length of permutation we want to generate:
data = [1, 2, 3]
data_per = permutations(data, 2) # 2 represents length of permutation we want to generate:
print(list(data_per)) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("-----------------------------------------------------")

# 3: Combinations
# The combination function basically makes all the possible combinations with a specified length
print("For Combinations")
combo = [1, 2, 3, 4, 5]
comb = combinations(combo, 2) # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
# Here 2 represents length of combinations we want to generate:
print(list(comb))
# Some more operations 
from itertools import combinations_with_replacement
comb_wr = [1, 2, 3, 4]
comb_wr = combinations_with_replacement(comb_wr, 2)
print(list(comb_wr)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print("-----------------------------------------------------")

# 4: Accumulate
# The accumulate function makes an iterator that returns the accumulated sum 
print("For Accumulate")
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a) # 1 2 3 4
print(list(acc)) # 1 3 6 10, accumulated sum of a
# we can also multiply the elements:
import operator
b = [1, 3, 4, 7]
b_acc = accumulate(b, func=operator.mul)
print(b) # 1 3 4 7
print(list(b_acc)) # 1 3 12 84
# Comparing max value with other sets
c = [1, 4, 7, 6, 9, 10]
max_c = accumulate(c, func=max)
print(c)
print(list(max_c))
print("--------------------------------------------------------")

# 5: Groupby
# It makes an iterator that returns keys and groups from an iterable
print("For Groupby")
test = [1, 2, 3, 4, 5]
def check_no(x):
    return x < 4

group_test = groupby(test, key=check_no)
for key, value in group_test:
    print(key, list(value))

#Using Lambda Functions
case = [1, 2, 3, 4, 5, 6]
checkTest = groupby(case, key =lambda x: x < 5)
for key, value in checkTest:
    print(key, list(value))
#Lambdas are small one line function that has an input and does something and returns it:

# another example
person = [{"name": "Tim", "age": 25}, {"name": "Adam", "age": 25}, {"name": "Jack", "age": 27}, {"name": "David", "age": 29}]

group_per = groupby(person, key=lambda x: x["age"])
for key, val in group_per:
    print(key, list(val))

print("--------------------------------------------------------")


