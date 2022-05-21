#import sys
import re
import requests
from bs4 import BeautifulSoup as soup
page = requests.get("https://sfbay.craigslist.org/search/mca?auto_make_model=honda+valkyrie&purveyor=owner&bundleDuplicates=1&auto_title_status=1&min_price=100&condition=10&condition=20&condition=30&condition=40")
bsobj = soup(page.content,'lxml')
links = []
for link in bsobj.findAll('li',{'class':'result-row'}):
    links.append(link.a['href'])
title = {}
for link in links:
    page = requests.get(link)
    bsobj = soup(page.content,'lxml')
    print(bsobj.findAll('h1')[0].text.strip())
#    title.append(bsobj.findAll('h1')[0].text.strip()) #иуи надо переделать. перед этим разьбить строки на элементы и из них налепить кей-валбю пар. из уже и добавлять в {}
    s = (bsobj.findAll('h1')[0].text.strip())
    x = (s.split(" - "))[0]
    print(x)
    m = (s.split("-"))[1]
    y = (m.split("("))[0]
    print(m)
    title[x] = y

print(title)