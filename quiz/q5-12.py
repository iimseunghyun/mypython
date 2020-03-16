import time

today = time.strftime("%Y%m%d")
todayyear = int(today[:4])
todaymonth = int(today[4:6])
todayday = int(today[6:])

print(todayyear, todaymonth, todayday)