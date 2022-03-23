import random
list1 = []
list2 = []
list3 = []
n = int(input("Enter the length of list 1 you want to create: "))
for i in range(n):
    list1.append(random.randint(1, 99))
print (list1)
m = int(input("Enter the length of list 2 you want to create: "))
for i in range(m):
    list2.append(random.randint(1, 99))
print (list2)

if len(list1) <= len(list2):
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
        if i == len(list1) - 1 and len(list1) < len(list2):
            x = len(list2) - len(list1)
            for m in range(x):
                list3.append(list2[len(list1) + m])

if len(list1) > len(list2):
    for i in range(len(list2)):
        list3.append(list1[i])
        list3.append(list2[i])
        if i == len(list2) - 1 and len(list2) < len(list1):
            x = len(list1) - len(list2)
            for m in range(x):
                list3.append(list1[len(list2) + m])
print (list3)

# Hope you check out the below code.
# N = int(input())

# num1 = [0] * N
# for i in range(N):
# 	num1[i] = int(input())
# print (num1)

# M = int(input())
# num2 = [0] * M
# for i in range(M):
# 	num2[i] = int(input())
# print (num2)

# minlen = N if N < M else M
# num3 = [0] * (minlen * 2)
# for i in range(minlen):
# 	num3[2*i] = num1[i]
# 	num3[2*i+1] = num2[i] 

# if N == minlen:
# 	num3 = num3 + num2[minlen:]
# else:
# 	num3 = num3 + num1[minlen:]

# print (num3)
