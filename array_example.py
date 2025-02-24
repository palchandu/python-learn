## Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
## This is a simple example of an array in Python.

# Create an array
cars = ["Ford", "Volvo", "BMW"]

print(cars)
print(cars[1])
print(len(cars))

# Loop through an array
for x in cars:
  print(x)


# Change an item in the array
cars[1] = "Toyota"
print(cars)

# Add an item to the array
cars.append("Honda")
print(cars)

# Remove an item from the array
cars.pop(1)
print(cars)

# Remove an item from the array
cars.remove("BMW")
print(cars)
