camale = []
cafemale = []
camalemum = []
cafemalenum = []
flmale = []
flfemale = []
flmalemum = []
flfemalenum = []

ct = list(open("ca2021.txt", "r", newline = None))
ft = list(open("fl2021.txt", "r"))

for i in range(len(ct)):
    x = (ct[i])
    y = (ct[i].split())
    camale.append(y[1])
    cafemale.append(y[3])
    camalemum.append(y[2])
    cafemalenum.append(y[4])
print(camale)
print()
print(cafemale)
print()
print(camalemum)
print()
print(cafemalenum)
