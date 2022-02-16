import random
a = random.randint(1, 100)
flag = True
while (flag):
    b = random.randint(0,100)
    print (" The previous number is {0} and the next number is {1}".format(a, b))
    if ( a < b ):
        print ("The loop will stop since the next {1} is greater than {0}".format(a, b))
        flag = False
    elif (b == a):
            print (" The previous number is {0} and the next number is {1}. They are equal".format(a, b))
    else:
        a = b 