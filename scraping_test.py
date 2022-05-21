import requests
from bs4 import BeautifulSoup
URL = "https://www.indeed.com/jobs?q=python&l=Livermore%2C%20CA&rbl=Livermore%2C%20CA&jlid=3547119f36ab3650&fromage=14&vjk=3c198f30a5ca4ba2"
r = requests.get(URL)
#print(r.content)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())