list = []
while True:
    n = int(input("Enter the number ")) 
    if n < 0:
        if len(list) > 2:
            list.sort()
    #        print (list)
    #        print (len(list))
            list.pop()
            list.pop(0)
    #        print (list)
            print (sum(list), sum(list) / len(list))
            break
        else:
            print ("0 0.00")
            break
    list.append(n)
#    print (list)