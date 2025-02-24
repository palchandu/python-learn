## In Python a function is defined using the def keyword:

def my_function():
    print("Hello from a function")

## call a function
my_function()

## Pass an arguments

def userName(fname,lname):
    print('Fullname: '+fname+' '+lname)

userName('Chandra','Prakash')

## Arbitrary Arguments, *args
## If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition

def numberKids(*kids):
    print(kids[0])

numberKids("One","Two","Three","Four")

## Keyword Arguments
## You can also send arguments with the key = value syntax.
## This way the order of the arguments does not matter.

def argumentExample(child3,child2,child1):
    print("The youngest child is "+ child3)

argumentExample(child1="Hello",child3="World",child2="How")

## Arbitrary Keyword Arguments, **kwargs
## If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition

def arbitraryArgumentExample(**userInfo):
    print("User last name",userInfo['lastname'])

arbitraryArgumentExample(firstname="Chandra",lastname="Prakash")

## The pass Statement
'''
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error
'''

def myFunction():
    pass

