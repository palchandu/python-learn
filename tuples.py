mytuple=(1,2,3,4,5)
print(mytuple)
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
####### Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
####### Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

###### Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

thisTuple=('apple','banana','cherry','apple','cherry')
print(thisTuple)

##### Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thisTupl=('apple',)
print(thisTupl)

# Tuple Items - Data Types
# Tuple items can be of any data type:

tuple1=('apple','banana','cherry');
tuple2=(1,5,7,9,3);
tuple3=(True,False,True)

# A tuple can contain different data types:

tuple1=('apple',1,True,'banana',False)

# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple.

thisTuple=(('apple','banana','cherry'))
print(thisTuple)

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
# Negative indexing means start from the end.

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# By leaving out the end value, the range will go on to the end of the tuple:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes

# Specify negative indexes if you want to start the search from the end of the tuple

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists

# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Update Tuples

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.

# You can convert the tuple into a list, change the list, and convert the list back into a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Add tuple to a tuple.

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple)

#  Python - Unpack Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Using Asterisk*

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Join Two Tuples

# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)