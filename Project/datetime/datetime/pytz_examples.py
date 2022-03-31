import pytz
import datetime

kiev = 'Europe/Kiev'
thailand = 'Asia/Bangkok'

tz_kiev = pytz.timezone(kiev)
kiev_time = datetime.datetime.now(tz=tz_kiev)
print(kiev_time)

tz_thailand = pytz.timezone(thailand)
thailand_time = datetime.datetime.now(tz=tz_thailand)
print(thailand_time)

# for tz in pytz.all_timezones:
#     print(tz)

for country in pytz.country_names:
    print(country, pytz.country_names[country], pytz.country_timezones.get(country))

# print(datetime.datetime.today())
# print(datetime.datetime.now(None))
# print(datetime.datetime.utcnow())

