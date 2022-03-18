list = []
while True:
    a = input("Please enter numbers one by one. Enter q to stop: ")
    if a == ("q"):
        print ("You've entered:", list)
        break
    else:
        a = float(a)
        list.append(a)
m = (sum(list) / len(list))
#print ("The average of your lsit is:", m)
for i in range (len(list)):
    z = list[i] - m
    if z < 0:
        z = z * -1
    print ((format ((z), '.2f')), end = " ")



