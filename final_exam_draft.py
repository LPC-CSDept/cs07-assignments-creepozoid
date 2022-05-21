camale = []
cafemale = []
camalemum = []
cafemalenum = []
flmale = []
flfemale = []
flmalemum = []
flfemalenum = []

ct = list(open("ca2021.txt", "r", newline = None))
#if print(ct.readable()) != True:
#    print("Please put a file ca2021.txt into your working directory")
ft = list(open("fl2021.txt", "r"))

print(ct)
print()
print(ft)

for i in range(len(ct)):
    print(i)
    x = (ct[i])
    #x = x.strip('][').split(', ')
    #print(x)
    #print(f'{ct[i].split()}') # выполняет деление строки по пробелам и ковертацию в список (взято отсюда https://pythonim.ru/string/preobrazovanie-stroki-v-spisok-v-python) из примера однако пришлось убрать f' - конверацию в строку, непонятно нахера ее там оставили
    y = (ct[i].split())
    #print(y)
    camale.append(y[1])
    cafemale.append(y[3])
    camalemum.append(y[2])
    cafemalenum.append(y[4])
print(camale)
print(cafemale)
print(camalemum)
print(cafemalenum)
