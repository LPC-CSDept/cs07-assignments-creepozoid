import random
list1 = []
list2 = []
list3 = []
n = int(input("Enter the length of list 1 you want to create: "))
for i in range(n):
    list1.append(random.randint(1, 99))
print (list1)
m = int(input("Enter the length of list 2 you want to create: "))
for i in range(m):
    list2.append(random.randint(1, 99))
print (list2)

if len(list1) <= len(list2):
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
        if i == len(list1) - 1 and len(list1) < len(list2):
            x = len(list2) - len(list1)
            for m in range(x):
                list3.append(list2[len(list1) + m])

if len(list1) > len(list2):
    for i in range(len(list2)):
        list3.append(list1[i])
        list3.append(list2[i])
        if i == len(list2) - 1 and len(list2) < len(list1):
            x = len(list1) - len(list2)
            for m in range(x):
                list3.append(list1[len(list2) + m])
print (list3)