#Make a while loop that runs until we met two consecutive even numbers.
#print two even numbers.
#For example
#Input : 1 3 17 9 15 2 4
#output : 2 4

import random
number1 = random.randint(1, 100)
print (number1)
while True:
    number2 = random.randint(1, 100)
    print (number2)
    if number1 % 2 == 0 and number2 == (number1 + 2):
        break
    number1 = number2
print(number1, "and", number2, "are consequtive even numbers, generation has stopped")