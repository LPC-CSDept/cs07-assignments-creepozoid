import random
n = 0
i = 0 
print ('the 10 numbers are: ', end = '')
while ( i < 10):
    x = random.randint(0,100)
    print (x, end=' ')
    n = n + x
    if ( n > 500):
        print()
        print ('The total is', (n))
        break
    i = i + 1
else:
    print()
    print ('The total {0} is <= 500 '.format(n))