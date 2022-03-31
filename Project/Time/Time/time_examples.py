import time

# print(time.gmtime(0))
# print(time.gmtime(time.time()))
# print(time.localtime(time.time()))
# print(time.time())

# epoch_start_time = time.gmtime(0)
# print(epoch_start_time)
# print("Year: ", epoch_start_time[0])
# print("Month: ", epoch_start_time[1])
# print("Day: ", epoch_start_time[2])
#
# print("Year: ", epoch_start_time.tm_year)
# print("Month: ", epoch_start_time.tm_mon)
# print("Day: ", epoch_start_time.tm_mday)
# print("Day of week: ", epoch_start_time.tm_wday)

# print(time.ctime(time.time()))
# print(time.ctime(11111111111))

# print("Text before delay")
# time.sleep(3.2)
# print('Text after 3.2 seconds')

# local_time = time.localtime(time.time())
# print(local_time)
# print(time.mktime(local_time))
# print(time.asctime(local_time))
# print(time.strftime('%x %X',local_time))
# print(time.strftime('%m/%d/%Y, %H:%M:%S', local_time))
# print(time.localtime(1576832090.0))

time_string = '21 December, 2019'

struct_time = time.strptime(time_string, '%d %B, %Y')
print(struct_time)
