import csv
from datetime import datetime, date, time

cr = []
dcr =dict()
with open('Crimes.csv') as f:
    crime = csv.reader(f)
    for row in crime:
        if '2015' in row[2]:
            name = row[5]
            cr.append(name)
            c = cr.count(name)
            dcr.update({name:c})
maxcr = 0
for c, n in dcr.items():
    if n > maxcr:
        maxcr = n
        crimen = c
print(crimen, maxcr)