import datetime
import pytz

iso_format_string = '%Y-%m-%dT%H:%M:%S%z'

now_utc = datetime.datetime.now(pytz.timezone('UTC'))
print(now_utc.strftime(iso_format_string))  #  2022-03-10T16:28:14+0000
#
now_eu_kiev = now_utc.astimezone(pytz.timezone('Europe/Kiev'))
print(now_eu_kiev.strftime(iso_format_string))  #  2022-03-10T18:29:24+0200
#
now_eu_istanbul = now_utc.astimezone(pytz.timezone('Europe/Istanbul'))
print(now_eu_istanbul.strftime(iso_format_string))  #  2022-03-10T19:30:15+0300

naive_now = datetime.datetime.now()
print(naive_now)  #  2022-03-10 17:25:26.846210
kiev_timezone = pytz.timezone('Europe/Kiev')
local_datetime = kiev_timezone.localize(naive_now)
print(local_datetime)  #  2022-03-10 17:25:26.846210+02:00

# all_timezones = pytz.all_timezones
# for timezone in all_timezones:
#     print(timezone)


