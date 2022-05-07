import xlrd

xls = 'student.xls'
work_book = xlrd.open_workbook(xls)
worksheet = work_book.sheet_by_index(0)
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

finalarr = []
for i in range(len(names)):
  ziparr = [id[i], names[i], scores[i]]
  finalarr.append(dict(zip(header, ziparr)))

print (finalarr)
