# Opgave 1
from asyncio.windows_events import NULL


def checkList(items):
    if len(items) != 8:
        return False
    item5 = items[5]
    count = 0
    for i in items:
        if i == item5:
            count+= 1
    if count >=3:
        return True
    else:
        return False



print(checkList([19, 19, 15, 5, 5, 5, 1, 2]))

# Opgave 2

def multiplyStuff(items):
    sum = 1
    for i in items:
        sum *=i
    return sum

print(multiplyStuff([8, 2, 3, -1, 7]))

# Opgave 3

sample = "1234abcd"
reverse = sample[::-1]

print(reverse)

# Opgave 4

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)

print(dic1)

# Opgave 5

for i in range(0,7):
    if i % 3 != 0 or i == 0:
        print(i)

# Opgave 6

sample = 'google.com'
count = {}

for i in sample:
    if count.get(i) == None:
        count[i] = 1
    else:
        count[i] += 1

print(count)

