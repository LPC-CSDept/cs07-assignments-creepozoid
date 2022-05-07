#import requests
import xlrd
#import urllib
#import os
#print (os.getcwd)

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
print ("header =", header)

for i in range(1, worksheet.nrows):
    id.append(int(worksheet.col_values(0)[i]))
print ("id =", id)

for i in range(1, worksheet.nrows):
    names.append(worksheet.col_values(1)[i])
print ("name =", names)

for i in range(1, worksheet.ncols):
    ind_score = []
    for j in range(2, worksheet.nrows):
        ind_score.append(worksheet.row_values(i)[j])
    scores.append(ind_score)
print (scores)

