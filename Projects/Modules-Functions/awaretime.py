import datetime, pytz

print()

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Niave local time: {}".format(local_time))
print("Niave UTC: {}".format(utc_time))

print()

aware_local_time = pytz.utc.localize(local_time).astimezone() # required when using localizing if you want the time zone
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}: time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC time {}: time zone {}".format(aware_local_time, aware_utc_time.tzinfo))

print()

# Get seconds since epoch
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

print()

# Converting from timestamp -> utc date and time -> local time
s = 1445733000 # seconds since epoch on 2015-10-01 1:30:0:0
t = s + (60 * 60) # add one hour

#tz = pytz.timezone('GB')
tz = pytz.timezone('Europe/London')
#tz = pytz.timezone('America/Los_Angeles')
print(tz,":", sep='')

#dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(tz) # time zone in UK
#dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(tz)
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(tz) # time zone in tz (Europe/London here)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(tz)

print("\t{} seconds since the epoch is {}".format(s, dt1))
print("\t{} seconds since the epoch is {}".format(t, dt2))

print()
