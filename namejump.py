import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

cuenta = raw_input('Enter count:')
cta = int(cuenta)

pos = raw_input('Enter position:')
posi = int(pos)

print(url)

count = 1
while (count <= cta):
    hrefs = list()
    tags = soup('a')
    for tag in tags:
        hrf = tag.get('href', None)
        hrefs.append(hrf)
    print(hrefs[posi-1])       
    html = urllib.urlopen(hrefs[posi-1]).read()
    soup = BeautifulSoup(html)
    count = count + 1
