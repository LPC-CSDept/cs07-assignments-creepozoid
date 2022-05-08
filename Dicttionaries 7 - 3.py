import xlrd
import functools

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

print (dict01)
print()

a = list(filter(lambda i: sum(i['Scores']) > 380, dict01))
print(*a)

