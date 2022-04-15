import sys # to remove "Traceback (most recent call last): ..." message
sys.tracebacklimit = 0 # to remove "Traceback (most recent call last): ..." message

str = input("Enter a phrase please ")

def getalnum(str):
    for char in str:
        if char.isalnum():
            yield char
            
x = getalnum(str)
for i in str:
    print (next(getalnum(x)))




