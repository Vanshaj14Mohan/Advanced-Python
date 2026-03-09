# In this part we will lean about lambda function and it's usage
# A lambda function is a small one line anonymous function that is derived that is defined without a name
# Syntax for writing a lambda expression:
# lambda arguments: expression
add_no = lambda x: x+ 20
print(add_no(10)) # 30, pretty much same as a normal function

def addno(x):
    return x + 10

print(addno(10)) # 20

# Lambda functions can have multiple arguments as well
mult = lambda x,y: x*y
print(mult(5, 7)) # 35