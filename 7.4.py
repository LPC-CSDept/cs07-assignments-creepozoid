list1 = []
while True:
    n = int(input("Enter a number to add it to the first list. Enter 0 to stop "))
    if n == 0:
        break 
    else:
        list1.append(n)
        list1.sort()
    print (list1)