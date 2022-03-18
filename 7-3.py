list1 = []
list2 = []
while True:
    n = int(input("Enter a number to add it to the first list. Enter 0 to stop "))
    if n == 0:
        break 
    else:
        list1.append(n)
    print (list1)

while True:
    m = int(input("Enter a number to add it to the second list. Enter 0 to stop "))
    if m == 0:
        break 
    else:
        list2.append(m)
    print (list2)

flag = 0
if(all(x in list1 for x in list2)):
    flag = 1
 
if (flag):
    print("Yes, second list is subset of first list.")
else:
    print("No, second list is not subset of first list.")
