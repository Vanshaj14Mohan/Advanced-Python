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

# Now some more useful methods that could be used with strings
# To avoid unnecessary white spaces in a string
test = "    Python   "
# here we can use strip() method to avoid unnecessary white spaces
print(test) #     Python
print(test.strip()) # Python
print(test) # Tho it won't change the original string as they are immutable
