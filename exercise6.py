import random
n1 = random.randint(0,100)
n2 = random.randint(0,100)
n3 = random.randint(0,100)
print (n1, n2, n3)
#n1 = 2
#n2 = 1
#n3 = 1
if n1 == n2 == n3:
    print ("JACKPOT! all values are the same ")
elif n1 <= n2 and n1 <= n3:
    print ("smallest value is", n1)
elif n2 <= n1 and n2 <= n3:
    print ("smallest value is", n2)
else:
    print ("smallest value is", n3)