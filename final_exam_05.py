import random
aaa = []
ddd = {}
for i in range(10):
    aaa.append(random.randint(0, 4))
print('list of randomly selected numbers:')
print(aaa)
print()
from collections import Counter
ddd = dict(Counter(aaa))
print('dictionary created from the list above:')
print(ddd)
print()
vvv = max(ddd, key = lambda k: ddd[k])
kkk = ddd[vvv]
print("Answer:", vvv, '(', kkk, 'times occured )')
