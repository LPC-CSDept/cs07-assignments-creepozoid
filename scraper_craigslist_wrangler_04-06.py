# This scraper get from craigslist listing of all 2004 -2006 jeep wranglers 
# that are for sale in SF Bay Area and create a dictionary 
# where key is title of an ad and value is the price of the corresponding vehicle

import requests
from bs4 import BeautifulSoup as soup
page = requests.get("https://sfbay.craigslist.org/search/cta?purveyor=owner&auto_make_model=jeep+wrangler&min_auto_year=2004&max_auto_year=2006")
bsobj = soup(page.content,'lxml')
links = []
for link in bsobj.findAll('li',{'class':'result-row'}):
    links.append(link.a['href'])
dict01 = {}
for link in links:
    page = requests.get(link)
    bsobj = soup(page.content,'lxml')
    print(bsobj.findAll('h1')[0].text.strip())
    s = (bsobj.findAll('h1')[0].text.strip())
    x = (s.split(" - "))[0]
    m = (s.split("-"))[1]
    y = (m.split("("))[0]
    dict01[x] = y
print()
print(dict01)