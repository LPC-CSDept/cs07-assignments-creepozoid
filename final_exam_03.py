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
    camalenum.append(int(y[2].replace(',',"")))
    cafemalenum.append(int(y[4].replace(',',"")))
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
    flmalenum.append(int(y[2].replace(',',"")))
    flfemalenum.append(int(y[4].replace(',',"")))
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



# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++  
# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++  
# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++  
# +++++++++++++++++++++++++++++++++++++ NEW CODE BEGINS +++++++++++++++++++++++++++++++++++++ 


st_f = list(filter(lambda stt: stt['state'] == 'CA', lod)) 
#print(st_f)
gd_st_f = list(filter(lambda gndr: gndr['gender'] == 'male', st_f))
# print('list filtered by gender (male) and state (CA):')
# print(gd_st_f)


gd_f = sorted(gd_st_f, key = lambda x: x['number'])
print('list filtered by gender (male) and state (CA):')
print(gd_f)
print()
print('Sorted list (reversed):')
gd_f = sorted(gd_st_f, key = lambda x: x['number'], reverse = True)

print(gd_f)
print()
st_f = list(filter(lambda stt: stt['state'] == 'FL', lod))
#print(st_f)
gd_st_f = list(filter(lambda gndr: gndr['gender'] == 'female', st_f))
gd_st_f = list(filter(lambda lettr: lettr['name'][0] == 'E', gd_st_f)) # AAAHHHH, I SOLVED IT!!!!!!111111111 --> [0] !!!!1111

print('list filtered by gender (female), name (starts with E) and state (FL):')
print(gd_st_f)
gd_f = sorted(gd_st_f, key = lambda x: x['number'])
print()
print('Sorted list:')
print(gd_f)
# print(len(gd_f))

maxItem = max(gd_f, key=lambda x:x['number'])
minItem = min(gd_f, key=lambda x:x['number'])

tenNamesList = gd_f

for z in range(len(tenNamesList) - 10):
    minVal = (min(tenNamesList, key=lambda x:x['number'])['number']) 
    tenNamesList = list(filter(lambda i: i['number'] != minVal, tenNamesList))

print()
print('reduced to top 10:')
print(tenNamesList)