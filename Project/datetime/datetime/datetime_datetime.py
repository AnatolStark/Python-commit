from datetime import datetime


# today = datetime(2019, 12, 25)
# today_now = datetime.now()
# print(today)
# print(today_now)
#
# timestamp = datetime.timestamp(today)
# print(timestamp)
# timestamp_now = datetime.timestamp(today_now)
# print(timestamp_now)

today = datetime(2019, 12, 25)
print(today)  #  2019-12-25 00:00:00
timestamp = datetime.timestamp(today)
print(timestamp)  #  1577228400.0  (v sekundah)
today_from_timestamp = datetime.fromtimestamp(timestamp)
print(today_from_timestamp)  #  2019-12-25 00:00:00
today_format = today.strftime('%d %B %Y')
print('Today is', today_format)  #  Today is 25 December 2019
print('Today is', today.strftime('%A'))  #  Today is Wednesday

# today = datetime.today()
# print(today)  #  2022-03-09 15:40:02.074988
# utc_today = today.utcnow()
# print(utc_today)  #  2022-03-09 14:40:02.078996
# print(today.date())  #  2022-03-09
# print(today.time())  #  15:40:02.074988
# print(today.isocalendar())  #  datetime.IsoCalendarDate(year=2022, week=10, weekday=3)
# print(today.isoformat())  #  2022-03-09T15:40:02.074988










