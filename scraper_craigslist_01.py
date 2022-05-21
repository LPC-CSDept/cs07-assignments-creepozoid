import sys
import requests
from bs4 import BeautifulSoup as soup
page = requests.get("https://sfbay.craigslist.org/search/eby/mca?purveyor=owner&bundleDuplicates=1&min_price=100&auto_make_model=honda+valkyrie&condition=10&condition=20&condition=30&condition=40&auto_title_status=1")
bsobj = soup(page.content,'lxml')
links = []
for link in bsobj.findAll('li',{'class':'result-row'}):
    links.append(link.a['href'])
title = []
for link in links:
    page = requests.get(link)
    bsobj = soup(page.content,'lxml')
    print(bsobj.findAll('h1')[0].text.strip())
    title.append(bsobj.findAll('h1')[0].text.strip())
    for i in bsobj.findAll('section',{'id':'postingbody'}):
        with open("randomfile.txt", "a") as o:
            o.write(bsobj.findAll('h1')[0].text.strip())
            o.write('')
            o.write(i.text.strip())
            o.write('')