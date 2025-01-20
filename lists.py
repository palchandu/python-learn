mylist=["apple","banana","cherry"]
print(mylist)
print(type(mylist))

# create list using list constructor
fruits=list(('banana','apple','grapes','pomegranets'))
print(fruits)

# Access list item
print(fruits[1])
# Negative Indexing 
# -1 refers to the last item, -2 refers to the second last item etc.

print(fruits[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
# Check if Item Exists
if 'apple' in thislist:
    print('apple exist')


# Change list item value

thislist[1]='blackcurrant'
print(thislist)

# Change a Range of Item Values
thislist[1:3]=['blackcurrant','watermelon']
print(thislist)

# if you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist[1:2]=['blackcurrant','watermelon']
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist[1:3]=['blackcurrant']
print(thislist)

# Insert Items using insert() method
thislist.insert(2,'papaya')
print(thislist)

# Add List Items using append() method
# append() method to append an item to the end of the list
thislist.append('lemon')
print(thislist)

# Add List Items using extend() method
# To append elements from another list to the current list, use the extend() method.
thislist.extend(['grapes','pomegranets'])
print(thislist)

# add any iterable to the list, not just lists
thislist.extend(('grapes','pomegranets')) # tuple
print(thislist)

# Remove List Items
# remove() method removes the specified item
thislist.remove('papaya')
print(thislist)
# if  the item to remove is more than one, then the remove() method will remove the first occurrence of the value
thislist.remove('grapes')
print(thislist)
# if the item to remove does not exist, remove() will raise an error
# thislist.remove('grapes')

# pop() method removes the specified index, (or the last item if index is not specified)
thislist.pop()
print(thislist)
thislist.pop(2)
print(thislist)

# del keyword removes the specified index
del thislist[1]
print(thislist)

# del keyword can also delete the list completely
del thislist
# print(thislist) # this will raise an error because the list is deleted

# clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if 'a' in x]
print(newlist)

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort Descending
thislist.sort(reverse=True)
print(thislist)

# sort numbers
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sort numbers descending
thislist.sort(reverse=True)
print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
def myfunc(n):
    print(n)
    return n-50
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
mylist = list(thislist)
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1+list2
print(list3)

# Another way to join two lists are by appending all the items from list2 into list1, one by one
for x in list2:
    list1.append(x)
print(list1)

# Use the extend() method to add list2 at the end of list1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
