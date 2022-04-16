import random
list1 = []
list2 = []

def input():
    for i in range(random.randint(1, 9)):
        list1.append(random.randint(0, 9))
    for j in range(random.randint(1, 9)):
        list2.append(random.randint(0, 9))
    print(list1, list2)
    return list1, list2

def getmerged(a, b):
    result = []
    for x in a:
        if getevens(x) == True:
            result.append(x)
    for x in b:
        if getevens(x) == True:
            result.append(x)
    for x in result:
        yield x

input()
result = getmerged(list1, list2)
getevens = lambda num: num % 2 == 0
for n in result:
    print(n)