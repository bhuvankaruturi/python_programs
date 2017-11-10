import urllib.request
import urllib.parse

wiki = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
#url = urllib.parse.urlparse(wiki)
#print(url)
req = urllib.request.Request(wiki)
page = urllib.request.urlopen(req)
page = urllib.request.urlopen(wiki)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'lxml')

table_item = soup.find('table', class_ = 'wikitable sortable plainrowheaders')

A = []
B = []
C = []
D = []
E = []
F = []
G = []

tr_items = table_item.find_all('tr')
for item in tr_items:   
    cells = item.find_all('td')
    states = item.find_all('th')
    if len(cells) == 6:
        A.append(cells[0].text)
        B.append(states[0].text)
        C.append(cells[1].text)
        D.append(cells[2].text)
        E.append(cells[3].text)
        F.append(cells[4].text)
        G.append(cells[5].text)

import pandas as pd
df = pd.DataFrame(A, columns=['Number'])
df['States'] = B
df['Admin Capital'] = C
df['Legis Capital'] = D
df['Judic Capital'] = E
df['Established Yr'] = F
df['Former Capital'] = G
f = open('states.txt','w')
f.write(df.__str__())
f.close()
writer = pd.ExcelWriter('union_territories.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
print('Completed SuccesFully. Find the output in union_territories.xlsx')
#class_ = 'wikitable sortable plainrowheaders jquery-tablesorter'
