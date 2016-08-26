import json, urllib, re


address = raw_input('Enter location: ')
url = urllib.urlopen(address)
data = url.read()
info = json.loads(data)


print 'Retrieving', address
print 'Retrieved',len(data),'characters'
print 'User count:', len(info)
print(type(info))

nums = list()
i = 1
lim = len(info['comments'])
print 'Count', lim
while(i <= lim):       
#for i in range(lim):
    for value in info['comments'][i]:
        nums.append(info['comments'][i-1].get('count'))
        i = i + 1
        
print 'Sum', sum(nums)
#print(nums)
