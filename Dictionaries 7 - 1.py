
import requests
import xlrd
import urllib

link = 'https://github.com/Kwooley/CS07/blob/main/Chap09/student.xls'
file_name, headers = urllib.request.urlretrieve(link)
print (file_name)
workbook = xlrd.open_workbook(file_name)
print (workbook)