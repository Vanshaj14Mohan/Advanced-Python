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