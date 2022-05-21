#Make a while loop to take the user string value
#it will stop when the input string is ‘stop’
#Otherwise, check the input string includes the character ‘p’
#After the loop, print the number of strings including ‘p’
#For example
#Input : program python java c++ stop
#output: 2

#b = 0
#while True:
#    a = input("Enter word:")
#    if 'p' in str(a):
#        b = b + 1
#    if str(a) == "stop":
#       print (b)
#       break

b = 0
while True:
    char_list = []
    a = input("Enter a word. Type stop for exit:")
    for c in a:
        char_list.append(c)
    #print(char_list)
    b = b + char_list.count('p')
    if str(a) == "stop":
        print ("The total number of letter p appeared in your input (includint word stop) is:", b)
        break