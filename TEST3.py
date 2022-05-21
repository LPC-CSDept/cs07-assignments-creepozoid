import matplotlib.pyplot as plt
x = [1,2,3,4]
data1 = [ 10, 20, 30, 40]
data2 = [ 5, 10, 5, 10]
fig, ax = plt.subplots()
ax.bar(x, data1)
ax.bar(x, data2)
plt.show()