import matplotlib.pyplot as plt
fig, ax = plt.subplots()
subjects = ['Math', 'English', 'Physics', 'Computer']
x = [1,2,3,4]
Bill = [100, 90, 80, 60]
Mary = [90, 80, 70, 100]
ax.bar(subjects, Bill)
ax.bar(subjects, Mary, bottom=Bill)
ax.set_title( 'Stacked graph for scores' )

ax.legend(['Bill', 'Mary'])


plt.show()