x=5
y="John"
print(x)
print(y)

## variable exhange

x=4
print(type(x))
x="Sammy"
print(type(x))

## Casting

x=str(3)
x=int(3)
z=float(3)
print(type(x))
print(type(y))
print(type(z))

## Multi value multi variables

x,y,z="Hello","How","Are"
print(x)
print(y)
print(z)

#One Value multi variables
x=y=z=15
print(x)
print(y)
print(z)

## Unpacking collection(i'e list,tuples etc..)
fruits=["Apple","Banana","Cherry"]
x,y,z=fruits;
print(x)
print(y)
print(z)

## Global Variables
def myFunc():
    global x
    x="fantastic"
    return x
print(myFunc())
print("Access Global Variable",x)

## Change global variable value inside function
globValue="awesome1"
def newMyFunc():
    global globValue
    globValue="fantastic1"
    return globValue
print(newMyFunc())
print("Access Global Variable Again",globValue)