'''
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

'''

# Arithmetic operators
# +, Addition
# -, Subtraction
# *, Multiplication
# /, Division
# %, Modulus
# **, Exponentiation 
# //, Floor division


a=5
b=2
print('Addition',a+b)
print('Subtraction',a-b)
print('Multiplication',a*b)
print('Division',a/b)
print('Modulus',a%b)
print('Exponentiation',a**b)
print('Floor division',a//b)

# Python Assignment Operators
# = ,x = 5 
# += ,x+= 5 same x=x+5 
# -= ,x-= 5 same x=x-5
# *= ,x *= 5 same x=x*5
# /= ,x /= 5 same x=x/5
# %= ,x %= 5 same x=x%5
# //= ,x //= 5 same x=x//5
# **= ,x **= 5 same x=x**5
# &= ,x &= 5 same x=x&5 Bitwise AND operator 
# |= ,x |= 5 same x=x|5 Bitwise OR Operator
# ^= ,x ^= 5 same x=x^5 Bitwise XOR Operation
# >>= ,x >>= 5 same x=x>>5 Bitwise Right Shift Operator
# <<= ,x <<= 5 same x=x<<5 Bitwise Left Shift Operator
# := ,x := 5 same x=x:5 walrus operator
x=5
print(x)
x+=5
print(x)
x-=5
print(x)
x*=5
print(x)
x/=5
print(x)
x=7
x%=5
print(x)
x=6
x//=5
print(x)
x=2
x**=4
print(x)
x=7
x&=3
print(x)

# Python Comparison Operators
# ==, Equal,x == y
# !=, Not equal,x != y
# >, Greater than,x > y
# <,Less than,x < y
# >=,Greater than or equal to,x >= y
# <=,Less than or equal to,x <= y
x=4
y=3
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# Python Logical Operators
# and,Returns True if both statements are true,x < 5 and  x < 10
# or,Returns True if one of the statements is true,x < 5 or x < 4
# not,Reverse the result, returns False if the result is true,not(x < 5 and x < 10)
x=9
print(x>2 and x<10)
print(x>2 or x<10)
print(not(x>2 and x<10))

# Python Identity Operators
# is ,Returns True if both variables are the same object,x is y
# is not, Returns True if both variables are not the same object,x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z=x
print(x is y)
print(x is z)
print(x is not y)

# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
# in ,Returns True if a sequence with the specified value is present in the object,x in y
# not in,Returns True if a sequence with the specified value is not present in the object,x not in y
x = ["apple", "banana"]

print("banana" in x)
print("banana" not in x)

#Python Bitwise Operators
# &, 	AND,	Sets each bit to 1 if both bits are 1,	x & y
# |,	OR,	Sets each bit to 1 if one of two bits is 1,	x | y
# ^	,XOR,	Sets each bit to 1 if only one of two bits is 1	,x ^ y
# ~,	NOT,	Inverts all the bits,	~x
# <<,	Zero fill left shift,	Shift left by pushing zeros in from the right and let the leftmost bits fall off,	x << 2
# >>,	Signed right shift,	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off,	x >> 2



# Operator Precedence

'''
Operator precedence determines the order in which operations are performed in an expression. In Python, operators with higher precedence are evaluated before operators with lower precedence. When operators have the same precedence, their associativity (left-to-right or right-to-left) determines the order of evaluation.

Here is a list of Python operators in descending order of precedence:

1.Parentheses: ()
2.Exponentiation: **
3.Unary plus, minus, bitwise NOT: +x, -x, ~x
4.Multiplication, Division, Floor Division, Modulus: *, /, //, %
5.Addition, Subtraction: +, -
6.Bitwise Shift Operators: <<, >>
7.Bitwise AND: &
8.Bitwise XOR: ^
9.Bitwise OR: |
10.Comparison Operators: ==, !=, >, >=, <, <=, is, is not, in, not in
11.Boolean NOT: not x
12.Boolean AND: and
13.Boolean OR: or
14.Lambda: lambda

Note: If two operators have the same precedence, the expression is evaluated from left to right.
'''