from random import randint
rw = []
cl = []
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

a = [[randint(0, 99) for j in range(r)] for i in range(c)]
print(a)
print()
for i in range(r):
	rtot = sum(a[i])
	print ("The summation of row {0}: {1}".format(i, rtot))

for i in range(r):
    rw.append(sum(a[i]))
rw.sort()
print ("The biggest sum of numbers among the rows is", rw[len(rw) - 1])

print()

for i in range(c):
	ctot = 0
	for j in range(r):
		ctot = ctot + a[j][i]
	print ("The summation of column {0}: {1}".format(i, ctot))

for i in range(c):
    ctot = 0
    for j in range(r):
        ctot = ctot + a[j][i]
    cl.append(ctot)
cl.sort()
print ("The biggest sum of numbers among the columns is", cl[len(cl) - 1])