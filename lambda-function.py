## Lambda Function
'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''

x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(5,6))

x=lambda a,b,c:a+b+c
print(x(5,6,2))

## Why Use Lambda Functions?
'''
The power of lambda is better shown when you use them as an anonymous function inside another function.
'''
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))