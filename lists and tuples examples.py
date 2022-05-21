#LISTS
print ("LISTS")
print ("BASIC USAGE OF LISTS")
print ("Create a list with the values")
numbers = [5, 10, 15, 20]
print (numbers)
print ("-" * 64)

print ("Create a list with range function")
numbers = list(range(5))
print (numbers)
print ("-" * 64)

print ("Create a list with Repetition Operator")
numbers = [0] * 5
print (numbers) 
print ("-" * 32)
numbers = [0, 1, 2] * 3
print (numbers)
print ("=" * 64)

print ("LIST WITH A LOOP")

print ("List as an iterator")
numbers = [10, 20, 30, 40, 50]
for n in numbers:
       print (n, end=' ')
print()
print ("-" * 64)

print ("Indexing")
numbers = [10,20,30,40,50]
for i in range(5):
       print (numbers[i] , end='\t')
print ()
for i in range(0, 5, 2):
       print (numbers[i] , end='\t')
print ()
print ("-" * 64)

print ("CHANGE LIST VALUE")
print ("Let’s think of two cases")

num = [10, 20, 30, 40, 50]
for i in range(5):
       num[i] += 10
for v in num:
       print (v, end=' ')
print()
print ("-" * 32)

num = [10, 20, 30, 40, 50]
for v in num:
       v += 10
       print (v, end=' ')    # Values are added to 10
print()
for v in num:
       print (v, end=' ')
print()
print ("Values are not changed. Why? Хмм... границы видимости?")
print ("-" * 64)

print ("CREATE A LIST WITH THE 5 USER INPUTS")

print ("5 user inputs")

N = 5
numbers = []
for i in range(N):
       user_input = int(input('Enter your input'))
       numbers.insert(i, user_input)
for v in numbers:
       print (v, end=' ')

print ("-" * 64)

print ("5 random values")

import random
N = 5
randnums = []
for i in range(N):
       randnums.insert(i, random.randint(0,100))
for v in randnums:
       print (v, end=' ')
print ("-" * 64)

print ("PYTHON LIST/ARRAY METHODS")
print ("Finding Items in Lists")
print ("In operators")

num_list = [10, 20, 30, 40, 50]
target = int(input('Enter the target number'))
if target in num_list:
       print ("Target found in the list")
else:
       print ("Target is not in the list")

print ("-" * 32)

num_list = [10, 20, 30, 40, 50]
target = int(input('Enter the target number'))
for i in range(len(num_list)):
       if num_list[i] == target:
              print ("Target found at the index ", i)
              break
if ( i == len(num_list)-1):
       print ("Target is not in the list")

print ("-" * 64)

print ("Traditional way to find an item")

num_list = [10, 20, 30, 40, 50]
target = int(input('Enter the target number'))
for i in range(len(num_list)):
       if num_list[i] == target:
              print ("Target found at the index ", i)
              break
if ( i == len(num_list)-1):
       print ("Target is not in the list")

print ("-" * 64)

print ("Append")
print ("Append an item")
num1 = [10, 20, 30, 40, 50]
num1.append(60)
num1

print ("-" * 32)

#num1 = []
#num1[0] = 10 # ERROR

print ("-" * 32)
print ("Append a list")

num1 = [10, 20, 30]
num2 = [40, 50, 60]
num1.append(num2) # Not [10, 20, 30, 40, 50, 60]
print (num1)
#number of elements num1 : 4 why?

print ("-" * 64)

print ("Extend")
print ("Append a list")

num1 = [10, 20, 30]
num2 = [40, 50, 60]
num1.extend(num2) # Not [10, 20, 30, 40, 50. 60]
print (num1)
#number of elements num1 : 4. why? #IN Y OPINION THIS TIME NUMBER OF ELEMENTS IS 6 (SLIDE 12)

print ("-" * 64)

print ("Count()")
print ("The number of elements with the specified value")

num1 = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1]
print (num1.count(1)) # number of occurrences

print ("-" * 64)

print ("Pop()")
print ("Removes the element at the specified position")
num1 = [10, 20, 30]
num1.pop(len(num1)-1)
print (num1)
# Try this:
#num1.pop()

print ("-" * 64)

print ("Insert()")
print ("insert an item into the list (need an index and value)") 
num_list = [10, 20, 30, 40, 50]
add_val = 100500
num_list.insert(0, add_val)
for v in num_list:
       print (v, end=' ')

print ("-" * 64)

print ("insert an item with out-of-range index")

num_list = [10, 20, 30, 40, 50]
num_list.insert(10, 60) # do not try with uncertain index
print (num_list)

print ("-" * 32)

#num_list = [10, 20, 30, 40, 50]
#num_list[5] # Index Error

print ("-" * 64)

print ("Insert an item into sorted list")
print ("Find the index to be inserted")

num_list = [10, 20, 30, 40, 50]
add_val = 75
flag = 0
for i in range(len(num_list)):
       if ( num_list[i] > add_val):
              num_list.insert(i, add_val)
              flag = 1
              break
if ( flag == 0 ):
       num_list.insert(i+1, add_val)
for v in num_list:
       print (v, end=' ')







print ("-" * 64)

print ("Finding Items in Lists")
print ("Finding Items in Lists")