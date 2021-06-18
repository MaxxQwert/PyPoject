import requests
with open('dataset_3378_2.txt') as fl:
    ur = fl.readline().strip()
r = requests.get(ur).text.splitlines()
#r= ['a','s','ddddd','','']
print(r, len(r))