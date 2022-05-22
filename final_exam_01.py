camale = []
cafemale = []
camalenum = []
cafemalenum = []
flmale = []
flfemale = []
flmalenum = []
flfemalenum = []

ct = list(open("ca2021.txt", "r", newline = None))
ft = list(open("fl2021.txt", "r"))

for i in range(len(ct)):
    x = (ct[i])
    y = (ct[i].split())
    camale.append(y[1])
    cafemale.append(y[3])
    camalenum.append(y[2])
    cafemalenum.append(y[4])
print(camale)
print()
print(cafemale)
print()
print(camalenum)
print()
print(cafemalenum)
print()
print("=" * 64)
for i in range(len(ft)):
    x = (ft[i])
    y = (ft[i].split())
    flmale.append(y[1])
    flfemale.append(y[3])
    flmalenum.append(y[2])
    flfemalenum.append(y[4])
print(flmale)
print()
print(flfemale)
print()
print(flmalenum)
print()
print(flfemalenum)

dict_ca_male = dict(zip(camale, camalenum))
dict_ca_female = dict(zip(cafemale, cafemalenum))
dict_fl_male = dict(zip(flmale, flmalenum))
dict_fl_female = dict(zip(flfemale, flfemalenum))