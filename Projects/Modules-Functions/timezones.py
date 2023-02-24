import pytz
import datetime

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print()
print(f'The time in {country} is {local_time}\n')
print(f'UTC is {datetime.datetime.utcnow()}')
print()

# Print all valid timezones
# for x in pytz.all_timezones:
#     print(x)

# print()

# Print all country names (codes)
# for x in sorted(pytz.country_names):
#     print(x + ': ' + pytz.country_names[x])

# print()
for x in sorted(pytz.country_names):
    #print('{}: {}: {}'.format(x, pytz.country_names[x], pytz.country_timezones[x])) # Crashes if country does not have tz
    #print('{}: {}: {}'.format(x, pytz.country_names[x], pytz.country_timezones.get(x))) # .get() returns None if key doesn't exist
    print('{}: {}'.format(x, pytz.country_names[x]), end=':\n')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print('\t\t{}: {}'.format(zone, local_time))
    else:
        print("\t\tNo time zone(s) defined")
