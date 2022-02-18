import random
a = random.randint(1, 100)
while True:
    b = random.randint(0,100)
    print (" The previous number is {0} and the next number is {1}".format(a, b))
    if ( a < b ):
        print ("The loop will stop since the next {1} is greater than {0}".format(a, b))
        break

    else:
        a = b 