a=33
b=200
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

## Short hand if...else

if a<b: print("a is less than b")
print("A") if a>b else print("B")
##  Ternary Operators, or Conditional Expressions.

print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500

## And :- The and keyword is a logical operator, and is used to combine conditional statements
if a>b and c>a:
    print("Both condition are equal")

## Or:- The or keyword is a logical operator, and is used to combine conditional statements

if a>b or a>c:
    print("At least one of the conditions is true")

## Not :- The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

if not a>b:
    print("a is NOT greater than b")

## Nested If :- You can have if statements inside if statements, this is called nested if statements.

x=41
if x>10:
    print("Above ten, ")
    if x>20:
        print("and also above 20!")
    else:
        print("bot not above 20.")

## The pass Statement :- if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
a=33
b=200

if b>a:
    pass