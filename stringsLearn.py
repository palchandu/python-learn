#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings
a1="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a1)

a2='''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(a2)

#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String

for x in "banana":
    print(x)

#String Length
a="Hello,World!"
print(len(a))

# Check existance inside string'
text="The best things in life are free!"
print("free" in text)

# Check not existance inside string'
text="The best things in life are free!"
print("expensive" not in text)


# Slicing
# You can return a range of characters by using the slice syntax.

b="Hello World!"
print(b[2:5])

# slice from start
print(b[:5])

# slice from end
print(b[3:])

#Modify Strings

# Upper case
a="Hello, World!"
print(a.upper())

# Lower case
a="Hello, World!"
print(a.lower())

# remove whitespace
a="   Hello, World!"
print(a.strip())

# Replace  string
a="Hello, World!"
print(a.replace("H","J"))

# Split  string
a="Hello, World!"
print(a.split(","))

# Concatenate  string
a="Hello"
b="World!"
print(a+b)

# Format - Strings
# Combinig number with string is called string format
age=33
#txt="My name is chandra, I am "+age
#print(txt)

# Above is throwing error

# F-Strings
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

txt=f"My name is Chaandra, I am {age}"
print(txt)

# Another example

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

# Display the price with 2 decimals:

price=59
txt=f"The price is {price:.2f} dollars"
print(txt)

# isinstance
#  the isinstance() function, which can be used to determine if an object is of a certain data type

x=200
print(isinstance(x,int))