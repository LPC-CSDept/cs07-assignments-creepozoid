from ast import While
import random
x = int(input("Enter the length of list you want to create: "))
randlist = []
for i in range(x):
    randlist.append(random.randint(1, 99))
print (randlist)
while len(randlist) > 0:
    n = int(input("Enter the number you would like to delete from the list: "))
    randlist.remove(n)
    print (randlist)
