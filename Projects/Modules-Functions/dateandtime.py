import time

print()
print('The epoch on this system starts at ' +\
      time.strftime('%c', time.gmtime(0)) +\
        '\n')

print('The current timezone is {0} with an \
offset of {1} hours.\n'.format(time.tzname[0],\
    time.timezone/3600)) # time.timezone() returns seconds offset of time zone

if time.daylight != 0:
    print('\tDaylight Saving Time is in effect \
for this location.\n')
    print('\tThe DST timezone is ' + time.tzname[1] + '\n')

print('\tLocal time is ' +\
      time.strftime('%Y-%M-%d %H:%M:%S',\
                    time.localtime()) + '\n')

print('\tUTC time is ' +\
      time.strftime('%Y-%M-%d %H:%M:%S',\
                    time.gmtime()) + '\n')