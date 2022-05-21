import xlrd
import functools
file_location = 'student.xls'

def printValues(x):
  for i in x:
    print(int(i["ID"]), end=" ")
    print(i["Name"], end= " ")
    print(i["Scores"])

work_book = xlrd.open_workbook(file_location)
sheet = work_book.sheet_by_index(0)

total_rows = sheet.nrows
total_columns = sheet.ncols
header = []
id = []
name = []
scores = []
for i in range(total_rows):
  points = []
  for j in range(total_columns):
    if(sheet.cell_value(i,j)):
      if(i == 0):   
          header.append(sheet.cell_value(i,j))
      elif(j == 0):
        id.append(sheet.cell_value(i,j))
      elif(j == 1):
        name.append(sheet.cell_value(i,j))
      else:
        points.append(sheet.cell_value(i,j))
  if(points):
    scores.append(points)
print("Question #1\n")
print("header:",header)
print("id:",id)
print("name:",name)
print("scores:",scores)

finalarr = []
for i in range(len(name)):
  ziparr = [id[i], name[i], scores[i]]
  finalarr.append(dict(zip(header, ziparr)))

print("\nQuestion #2\n")
printValues(finalarr)

theLambda = lambda x : sum(x["Scores"]) > 280
greaterThan280 = list(filter(theLambda, finalarr))

print("\nQuestion #3\n")
printValues(greaterThan280)

print("\nQuestion #4\n")
theLambda = lambda x, y : x+y
for i in finalarr:
  print(int(i["ID"]), end=" ")
  print(i["Name"], end= " ")
  print((functools.reduce(theLambda, i["Scores"])))

def theLambda (x):
  x["ID"] = int(x["ID"]+10000000)
  return x

finalarr = list(map(theLambda,finalarr))

print("\nQuestion #5\n")
printValues(finalarr)