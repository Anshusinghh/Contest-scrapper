from bs4 import BeautifulSoup
import requests
import re


url=f'https://codeforces.com/contests/with/anshusinghosm'
page=requests.get(url).text
doc=BeautifulSoup(page,'html.parser')
data=doc.find('table',class_='tablesorter user-contests-table').tbody

main=[]
for tag in data.find_all('tr',limit=4):
    temp=[]
    for data in tag.find_all('td'):
        link=data.find('a',href=True)
        if link != None:
            temp.append(link['href'])
        temp.append(data.text.strip())
    
    main.append(temp)


for list in main:
    for i,data in enumerate(list):
        if i in (3,4,5,6,7):continue
        print(data,end=" ")
    print("")