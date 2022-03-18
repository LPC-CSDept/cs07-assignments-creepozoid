import random
list1 = []
list2 = []
n = int(input("Enter the length of list 1 you want to create: "))
for i in range(n):
    list1.append(random.randint(1, 99))
print (list1)
m = int(input("Enter the length of list 2 you want to create: "))
for i in range(m):
    list2.append(random.randint(1, 99))
print (list2)
if len(list1) < len(list2):
    (list1.extend(list2))
    print (list1)
else:
    (list2.extend(list1))
    print (list2)
 