# A string is an ordered and immutable collection data type used for text representation
# Created with either '' or "" quotes
case1 = "Hello Guys"
print(case1)
print(type(case1)) # Output => <class 'str'>

#Try not to use quotes inside a quote it will give error but can be fixed using escape sequence
case = "This\'s is a strings part"
# or 
demo_case = "This's a strings part"
print(demo_case) # Output => This's a string part
print(case) # Output => This's a string part

# We can even use triple quotes generally used for multi-line strings, could also be used for documentation inside a code
# Now adding \ in multi-line means that string should continue in another line and should not jump to new line.
temp = """So this is basically the part where I'll be discussing
and in-depth part regarding strings
and how it's used in Python"""
print(temp)

# Accesing characters or substrings in a string: It's quite similar to how we acces in lists:
#ie using indexing here:
print(case1[0]) # H
print(case1[1]) # e
# Now accesing from last elements
print(case1[-1]) # s
print(case1[-2]) # y

#NOTE: We can't acces and change a character in strings
# case1[0] = "h" # Now this would give error
# print(case1[0])
print("-------------------------------------------------------------")

#Slicing in strings
demo1 = "An advanced tutorial based on python"
part1 = demo1[1:5] # Start and stop index
print(part1) # Output => n ad
part2 = demo1[:7] # ffrom start to 7th index
print(part2) # Output => An adva
part3 = demo1[:] #from start to end
print(part3) # Output => An advanced tutorial based on python
part4 = demo1[4:] # From 4th index to the end
print(part4) # Output => dvanced tutorial based on python

part5 = demo1[::1] # print the whole string
print(part5)
part6 = demo1[::2] # Every second element from the string
print(part6) # Output => A dacdttra ae npto
part7 = demo1[::3] # Every third element from the string
print(part7) # Output => Aaaetoabeoph

#Reversing a string
rev_str = demo1[::-1]
print(rev_str) # Output => nohtyp no desab lairotut decnavda nA

rev_str2 = demo1[::-2]
print(rev_str2)

# Concatenation in strings : We do this using + operator
str1 = "A good day"
str2 = "to go out"
res = str1 + " " + str2
print(res)

#Iterating over elements in strings: we can use for in loop
for i in res:
    print(i)

# Now to check whether a character or substring is inside our string we can use if in statement for it
sample = "Advanced Python"
if "A" in sample:
    print("Character exist")
else:
    print("Character does not exist")

# We can also print that particular character too
x = "d"
if x in sample:
    print(x, "Character exist")
else:
    print(x, "Character does not exist")

#can also check for substring as well
if "vanced" in sample:
    print("Substring exist")
else: 
    print("Substring does not exist")

print("-------------------------------------------------------------")

# Now some more useful methods that could be used with strings
# 1: To avoid unnecessary white spaces in a string
test = "    Python   "
# here we can use strip() method to avoid unnecessary white spaces
print(test) #     Python
print(test.strip()) # Python
print(test) # Tho it won't change the original string as they are immutable

# 2: Now converting characters to Uppercase and Lowercase
data = "Python"
data2 = "PROGRAMMING LANGUAGE"
print(data.upper()) # PYTHON
print(data2.lower()) # programming language

# 3: Checking if a string/ sub-string starts and endswith with a specific character
print(data.startswith("P")) # True
print(data.startswith("H")) # False

print(data.endswith("n")) # True
print(data.endswith("r")) # False

# 4: Now we can find the index of character or a substring
print(data.find("h")) # Index 3
print(data.find("y")) # Index 1
print(data.find("on")) # Index 4
print(data.find("abc")) # Would print -1 as it does'nt exist

# 5: We can also count number of characters or substrings in a string
data3 = "programming languages"
print(data3.count("a")) # 3 as a appears three times in that string
print(data3.count("m")) # 2 times
print(data3.count("g")) # 4 times

# 6: We can also replace characters or substring inside our string
print(data3.replace("programming", "Advanced programming")) # Advanced programming languages
# It does not change the original string: And if we give it a value that does not exist it would just print original string
print("-------------------------------------------------------------")

# Now about lists and strings
task = "I'm learning advanced python language" # now if we want to convert it into a list, and put each word of string as an element in list
task2 = "I'm,learning,advanced,python,language"
list_task = task.split()
list_task2 = task2.split(",") # Without spaces 
print(list_task)
print(list_task2)
# Note using split() method without any argument it splits the string wherever there is whitespace,
# and Converts the string into a list of words

# And if you have list and you want to convert it into a string
string_conv = "".join(task) #.join method can we quite useful to join the elements of a list back to string
print(string_conv)

list1 = ["a"] * 5
print(list1) # ['a', 'a', 'a', 'a', 'a']

#Tough approach 
# Now checking how much time it takes for both to operations to get the code work done
from timeit import default_timer as timer
start = timer()
my_str2 = ""
for i in list1:
    my_str2 += i
stop = timer()    
print(my_str2) # aaaaa
print("For loop one", stop-start)

# Easy aaproach
start = timer()
my_str = "".join(list1)
print(my_str) # aaaaa
stop = timer()
print("Using Join method one", stop-start)
print("---------------------------------------------")

# Now formatted strings, 3 ways to format a string
# using % operator or using .format() method, or using F-Strings
name = "John"
age = 28
print("the name is %s" % name) # %s tells the interpreter that there is a placeholder with a string here and then we will it with our variable
print("the age is %d" % age) # %d as of integer value




