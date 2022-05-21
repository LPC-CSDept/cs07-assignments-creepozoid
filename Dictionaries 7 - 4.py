import xlrd
import functools
from functools import reduce

xls = 'student.xls'
work_book = xlrd.open_workbook(xls)
worksheet = work_book.sheet_by_index(0)
#print (xls)
header = []
id = []
names = []
scores = []

for i in range(worksheet.ncols):
    if worksheet.row_values(0)[i] != '':
        header.append(worksheet.row_values(0)[i])
    else:
        continue

for i in range(1, worksheet.nrows):
    id.append(int(worksheet.col_values(0)[i]))

for i in range(1, worksheet.nrows):
    names.append(worksheet.col_values(1)[i])

for i in range(1, worksheet.ncols):
    ind_score = []
    for j in range(2, worksheet.nrows):
        ind_score.append(worksheet.row_values(i)[j])
    scores.append(ind_score)

dict01 = []
for i in range(len(id)):
    ind_string = (id[i], names[i], scores[i])
    dict01.append(dict(zip(header, ind_string)))

for i in range(len(id)):
    print(dict01[i]['ID'], dict01[i]['Name'], reduce(lambda x, y: x + y, dict01[i]['Scores']))

#reduce function takes two arguments - lambda function and sequence of values associated with scores keys and summarize them
