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
print()
print("=" * 64)
for i in range(len(ft)):
    x = (ft[i])
    y = (ft[i].split())
    flmale.append(y[1])
    flfemale.append(y[3])
    flmalemum.append(y[2])
    flfemalenum.append(y[4])
print(flmale)
print()
print(flfemale)
print()
print(flmalemum)
print()
print(flfemalenum)