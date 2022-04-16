
def getInput(name, score):
    IDlist = []
    nameList = []
    scoreList = []
    for i in range(name):
        IDlist.append(1001 + i)
        nameList.append(input("Please enter a student name: "))
        scores = []
        for j in range(score):
            scores.append(int(input("Enter the student's score: ")))
        scoreList.append(scores)
    return (IDlist, nameList, scoreList)

def findHighTotalScore(n, h, s):
    flatList = []
    for i in range(len(s)):
        flatList.append(sum(s[i]))
    a = sorted(flatList, reverse=True)
    b = flatList.index(a[0])
    highstud = (h[b])
    highnum = (n[b])
    print ("The highest total score of", a[0], "for all subjects combined has student", highnum, highstud)
    return (highstud, highnum, a[0])

def findLowTotalScore(n, h, s):
    flatList = []
    for i in range(len(s)):
        flatList.append(sum(s[i]))
    a = sorted(flatList)
    b = flatList.index(a[0])
    lowstud = (h[b])
    lownum = (n[b])
    print ("The lowest total score of", a[0], "for all subjects combined has student", lownum, lowstud)
    return (lowstud, lownum, a[0])

def findHighScore(n, h, s):
    max = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]>max):
                max=s[i][j]
                hstud = h[i]
                hnum = n[i]
    print("Student with highest score of", max, "is", hnum, hstud)


def findLowScore(n, h, s):
    min = s[0][0]
    lstud = h[0]
    lnum = n[0]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]<min):
                min=s[i][j]
                lstud = h[i]
                lnum = n[i]
    print ("Student with lowest score of", min, "is", lnum, lstud)

# def printAll (IDlist, nameList, scoreList):
#     print (IDlist)
#     print (nameList) 
#     print (scoreList)

def printAll (IDlist, nameList, scoreList):
    for i in range(len(IDlist)):
        print (IDlist[i], nameList[i], scoreList[i], "Total", sum(scoreList[i]), "Avg", round(sum(scoreList[i]) / len(scoreList[i]), 2))

sds = int(input('Please enter number of students ')) 
sjs = int(input('Please enter number of subjects ')) 

z = getInput(sds, sjs)
# print (z)

printAll(*z)
findHighScore(*z)
findLowScore(*z)
findHighTotalScore(*z)
findLowTotalScore(*z)
