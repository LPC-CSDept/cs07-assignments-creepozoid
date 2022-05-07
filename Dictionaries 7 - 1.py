#import requests
import xlrd
#import urllib
#import os
#print (os.getcwd)

xls = 'student.xls'
work_book = xlrd.open_workbook(xls)
print (xls)