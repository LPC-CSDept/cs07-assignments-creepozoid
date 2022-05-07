import random
list1 = []
list2 = []

def input():
  for i in range(random.randint(0, 10)):
    list1.append(random.randint(0, 10))
  for j in range(random.randint(0, 10)):
    list2.append(random.randint(0, 10))
  print(list1, list2)
  return list1, list2
getevens = lambda num: num % 2 == 0
def getmerged(list1, list2):
  result = []
  for num in list1:
    if getevens(num) == True:
      result.append(num)
  for num in list2:
    if getevens(num) == True:
      result.append(num)
  for num in result:
    yield num

input()
result = getmerged(list1, list2)
for v in result:
  print(v)