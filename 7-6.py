import random
x = int(input("Enter the length of set 1 you want to create: "))
randlist = []
userlist = []
for i in range(x):
    randlist.append(random.randint(1, 99))
    randlist = list(set(randlist))
print (randlist)


while True:
    s = int(input("Enter a number to populate set 2. Enter 0 to stop: "))
    if s == 0:
        print (userlist)
        break
    else:
        userlist.append(s)


l = len(userlist)
#print (l)
m = []
v = []

if userlist[0] in randlist:

    for i in range(l):
#        print (i)
        z = randlist.index(userlist[i])
        m.append(z)
        v.append(i + randlist.index(userlist[0]))

#print (m)
#print (v)

print ("Checking if the set 2 is a subset of the set 1: ")	


k = m == v
print (k)