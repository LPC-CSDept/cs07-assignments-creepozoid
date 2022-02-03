m = int(input("Enter males amount:"))
f = int(input("Enter females amount:"))

t = m + f
mp = ((m/t) * 100)
fp = ((f/t) * 100)
mp = ((m/t) * 100)
fp = ((f/t) * 100)


print("The total number of students:\t", t)
print("The percentage of males and females:\t", (format ((mp/100), '.2%')), "\t", (format ((fp/100), '.2%')))