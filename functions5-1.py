# reads two lists of integers and returns the sum of multiplying the corresponding list items. 
# assumption: two lists must be the same

x = 0
y = 0
l1 = []
l2 = []
l3 = []
n = int(input("Please enter the length of the list 1 (equal in size to list 2) "))
while x < n:
    a = int(input("Enter a number to populate list A: "))
    l1.append(a)
    x = x + 1
print (l1)
while y < n:
    a = int(input("Enter a number to populate list B: "))
    l2.append(a)
    y = y + 1
print (l2)

def sumProduct(a, b):
    for i in range(n):
        v = a[i] * b[i]
        l3.append(v)
    return print (sum(l3))

sumProduct(l1, l2)




    

