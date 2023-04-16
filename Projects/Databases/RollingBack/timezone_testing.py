import datetime
import pytz

# utc_time = pytz.utc.localize(datetime.datetime.utcnow())
# local_time = utc_time.astimezone()
# offset = local_time.utcoffset()
# print(utc_time)
# print(local_time)
# print(offset)
# print("offset as seconds: ", offset.total_seconds())
# print("offset as minutes: ", offset.total_seconds()/60)
# print("offset as hours: ", offset.total_seconds()/60/60)
# print("offset as days: ", offset.total_seconds()/60/60/24)

# Timezone unaware
# utc_time = datetime.datetime.utcnow()
# utc_offset_seconds = -28800 # UTC offset for PST (8 hours behind UTC)
# local_time = utc_time + datetime.timedelta(seconds=utc_offset_seconds) # manually add the seconds on


# Timezone aware
utc_time = pytz.utc.localize(datetime.datetime.utcnow())
utc_offset_seconds = -7*60*60 # offset from utc in seconds
local_tz = datetime.timezone(datetime.timedelta(seconds=utc_offset_seconds))
local_time = utc_time.astimezone(local_tz)

print(utc_time)
print(utc_offset_seconds)
print(local_tz)
print(local_time)
