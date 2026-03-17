import time
dt = time.localtime(1760792385.7273266)
print(dt)
day = dt.tm_mday
month = dt.tm_mon
year = dt.tm_year
print(f"{day} / {month} / {year}")
h = dt.tm_hour
m = dt.tm_min
s = dt.tm_sec
print(f"{h} : {m} : {s}")