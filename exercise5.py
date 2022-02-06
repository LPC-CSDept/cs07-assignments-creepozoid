import random
n1 = random.randint(0,100)
n2 = random.randint(0,100)
n3 = random.randint(0,100)
print (n1, n2, n3)
#n1 = 9
#n2 = 9
#n3 = 8
if n1 == n2 == n3:
    print ("JACKPOT! all values are the same")
elif n1 == n2:
    print ("Two values are the same:", n1, "and", n2, "and non matching value is", n3)
elif n1 == n3:
    print ("Two values are the same:", n1, "and", n3, "and non matching value is", n2)
elif n3 == n2:
    print ("Two values are the same:", n3, "and", n2, "and non matching value is", n1)    
else:
        print ("All values are distinct")