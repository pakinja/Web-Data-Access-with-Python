import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
url = urllib.urlopen(address)
   
print 'Retrieving', address
    
data = url.read()
print 'Retrieved',len(data),'characters'
    
#print data
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')

lista = list()
print 'counts:', len(counts)
for item in counts:
    nums = item.find('./count').text
    lista.append(int(nums))
    #print 'nums:', item.find('./count').text
#print(lista)
print(sum(lista))
