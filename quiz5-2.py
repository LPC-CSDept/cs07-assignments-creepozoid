arr = []
st = []
subj = ['Math', 'English', 'Physics', 'Computer']

while True:
    c = (input("Enter student name (q to stop): "))
    if c == ("q"):
        break
    st.append(c)
    x = 0
    subarr = []
    for i in range (len(subj)):
        z = float(input("Enter score for: {} ".format(subj[x])))
        x = x + 1
        subarr.append(z)
#        print (subarr)
    arr.append(subarr)
#print (st)
#print (arr)

x = 0
ttl = 0
for i in range(len(st)):
    avg = (sum(arr[x]) / len(arr[x]))
    print ()
    print ("Average score for student {}".format(st[x]), "is", round(avg, 2), "and total is", sum(arr[x]))

    
    x = x + 1
print ()
for i in range(len(subj)):
    rsum = 0
    for j in range(len(st)):
        rsum = rsum + arr[j][i]
    #print ("The total for {0}: {1}".format((subj[i]), rsum))
    print ("The average for {0}: {1}, total is {2}".format((subj[i]), round(((rsum) / (len(st))), 2), rsum))

        

        
        

    


        



