# strip all letters except the upper case alphabets
# return the result

s = str(input("Enter a phrase please "))

def stripspace(a):
    x = ''.join(ch for ch in a if ch.isupper())
    #return print ([char for char in x])
    return print (x)
    
stripspace(s)

