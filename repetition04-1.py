import random
number = 1
while number % 2 != 0:
    number = random.randint(1, 100)
    print(number)
print((number), " isn't odd, generation stopped")