fruits=['apple','banana','cherry']
for x in fruits:
    print(x)

## Looping through string
for x in 'banana':
    print(x)

## Break statement
fruits=['apple','banana','cherry']

for x in fruits:
    print(x)
    if x=='banana':
        break

## Else in For Loop

for x in range(6):
    print(x)
else:
    print("Finally finished")