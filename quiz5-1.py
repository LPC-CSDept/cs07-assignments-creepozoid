import random
mylist = []
for i in range(10):
    mylist.append(random.randint(1, 99))
print (mylist)
minindex = (mylist.index(min(mylist)))
#print (minindex)
x = mylist[minindex]
#print (x)
y = mylist[0]
mylist.pop(minindex)
#minindex2 = (mylist.index(min(mylist)))
#print (mylist)
#print (minindex2)
#z = mylist[minindex2]
#print ('-------')
mylist.insert(minindex, y)
mylist.pop(0)
mylist.insert(0, x)
print (mylist)



mylist.pop(0) #х в уме


minindex = (mylist.index(min(mylist)))
z = mylist[minindex]
w = mylist[0]
mylist.pop(minindex)
mylist.insert(minindex, w)

mylist.insert(0, z)
mylist.insert(0, x)
mylist.pop(2)

print (mylist)

