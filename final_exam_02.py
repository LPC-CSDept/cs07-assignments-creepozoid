from msilib import CAB


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
# print(camale)
# print()
# print(cafemale)
# print()
# print(camalemum)
# print()
# print(cafemalenum)
# print()
# print("=" * 64)
for i in range(len(ft)):
    x = (ft[i])
    y = (ft[i].split())
    flmale.append(y[1])
    flfemale.append(y[3])
    flmalenum.append(y[2])
    flfemalenum.append(y[4])
# print(flmale)
# print()
# print(flfemale)
# print()
# print(flmalemum)
# print()
# print(flfemalenum)

dict_ca_male = dict(zip(camale, camalenum))
dict_ca_female = dict(zip(cafemale, cafemalenum))
dict_fl_male = dict(zip(flmale, flmalenum))
dict_fl_female = dict(zip(flfemale, flfemalenum))

# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++  
# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++  
# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++  
# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++  

cam = []
caf = []
flm = []
flf = []
lod = []
for i in range(100):
    #print(i)
    dict01 = {}
    dict02 = {}
    dict03 = {}
    dict04 = {}
    dict01['state'] = 'CA'
    dict02['state'] = 'CA'  
    dict03['state'] = 'FL'      
    dict04['state'] = 'FL'  
    dict01['name'] = camale[i]
    dict02['name'] = cafemale[i]
    dict03['name'] = flmale[i]
    dict04['name'] = flfemale[i]
    dict01['gender'] = 'male'
    dict02['gender'] = 'female'
    dict03['gender'] = 'male'
    dict04['gender'] = 'female'
    dict01['number'] = camalenum[i]
    dict02['number'] = cafemalenum[i]
    dict03['number'] = flmalenum[i]
    dict04['number'] = flfemalenum[i]
    cam.append(dict01)
    caf.append(dict02)
    flm.append(dict03)
    flf.append(dict04)
    lod.append(dict01)
    lod.append(dict02)
    lod.append(dict03)
    lod.append(dict04)

print("The list of dictionaries:")
print(lod)
print()
print("CA male dictionary:")
print(cam)
print()
print("CA female dictionary:")
print(caf)
print()
print("FL male dictionary:")
print(flm)
print()
print("FL female dictionary:")
print(flf)
print()

