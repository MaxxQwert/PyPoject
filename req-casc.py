import requests
with open('dataset_3378_3.txt') as fl:
    ur = fl.readline().strip()
r = requests.get(ur).text.strip()
pref = ur[:-10]
while r[:2] != 'We':
    r = requests.get(pref + r).text.strip()
    print(r, r[:2])
#r= ['a','s','ddddd','','']
print(r, len(r))