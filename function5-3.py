isspace = lambda a : a.isspace()

s = str(input("Enter a phrase please "))

def strip(s):
    char = ""
    for x in s:
        if isspace (x) != True:
            char = char + x
    return char


print (strip(s))

