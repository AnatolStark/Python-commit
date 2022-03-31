import time

# print(time.gmtime(0))  #  time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# print(time.gmtime(time.time()))  #  time.struct_time(tm_year=2022, tm_mon=3, tm_mday=5, tm_hour=15, tm_min=40, tm_sec=58, tm_wday=5, tm_yday=64, tm_isdst=0)
# print(time.localtime(time.time())) #  time.struct_time(tm_year=2022, tm_mon=3, tm_mday=5, tm_hour=16, tm_min=42, tm_sec=38, tm_wday=5, tm_yday=64, tm_isdst=0)
# print(time.time())  #  1646495013.0562751

# epoch_start_time = time.gmtime(0)
# print(epoch_start_time)  #  time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# print("Year: ", epoch_start_time[0])  #  Year:  1970
# print("Month: ", epoch_start_time[1])  #  Month:  1
# print("Day: ", epoch_start_time[2])  #  Day:  1
#
# print("Year: ", epoch_start_time.tm_year)  #  Year:  1970
# print("Month: ", epoch_start_time.tm_mon)  #  Month:  1
# print("Day: ", epoch_start_time.tm_mday)  #  Day:  1
# print("Day of week: ", epoch_start_time.tm_wday)  #  Day of week:  3

# print(time.ctime(time.time()))  #  Sat Mar  5 16:53:54 2022
# print(time.ctime(11111111111))  #  Sun Feb  5 20:45:11 2322  #  (time.ctime(11111111111)) - v sekundah

# print("Text before delay")  #  Text before delay
# time.sleep(3.2)
# print('Text after 3.2 seconds')  #  cheres 3,2 sekundy pojavljaetsja - Text after 3.2 seconds

local_time = time.localtime(time.time())
# print(local_time)  #  time.struct_time(tm_year=2022, tm_mon=3, tm_mday=5, tm_hour=17, tm_min=2, tm_sec=51, tm_wday=5, tm_yday=64, tm_isdst=0)
# print(time.mktime(local_time))  #  1646496171.0
# print(time.asctime(local_time))  #  Sat Mar  5 17:04:56 2022
print(time.strftime('%x %X',local_time)) #  03/05/22 17:05:54
print(time.strftime('%m/%d/%Y, %H:%M:%S', local_time))  #  03/05/2022, 17:06:45
print(time.localtime(1576832090.0))  #  time.struct_time(tm_year=2019, tm_mon=12, tm_mday=20, tm_hour=9, tm_min=54, tm_sec=50, tm_wday=4, tm_yday=354, tm_isdst=0)

time_string = '21 December, 2019'

struct_time = time.strptime(time_string, '%d %B, %Y')
# print(struct_time)  #  time.struct_time(tm_year=2019, tm_mon=12, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=355, tm_isdst=-1)

