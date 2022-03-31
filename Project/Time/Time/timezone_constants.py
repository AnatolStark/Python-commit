
import time

print('UTC time: ' + time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime()))  #  UTC time: 2022/03/08 15:00:20
print('Local time: ' + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))  #  Local time: 2022/03/08 16:00:20
print(time.altzone/60/60)  #  -2.0  -  ne korrektno
print(time.daylight)  #  1  -  ne korrektno
print(time.localtime())  #  time.struct_time(tm_year=2022, tm_mon=3, tm_mday=8, tm_hour=16, tm_min=6, tm_sec=4, tm_wday=1, tm_yday=67, tm_isdst=0)
print(time.timezone/60/60)  #  -1 - korrektno
print(time.tzname)  #  ('Западная Европа (зима)', 'Западная Европа (лето)')
print(time.tzname[0])  #  Западная Европа (зима)
if time.daylight != 0:
    print(time.tzname[1])  #  Западная Европа (лето)
print(time.localtime().tm_zone)  #  ???
print(time.localtime().tm_gmtoff)  #  3600 sekund
