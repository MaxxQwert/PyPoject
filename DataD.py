import datetime
b = [int(x) for x in input().split()]
dat = datetime.date(b[0], b[1], b[2]) + datetime.timedelta(int(input()))
print(dat.strftime('%Y %-m %-d'))