# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import pytz
import datetime

print()
# print(sorted(pytz.all_timezones)) # all time zones
# print()
# print(sorted(pytz.country_names)) # all country names (abbreviated)
# print()
# print(sorted(pytz.country_timezones)) # all country timezones (abbreviated)
# print()
#for x in pytz.country_names:
#    print(pytz.country_names[x], end=', ')
#print(pytz.country_names.__class__)
#for x in pytz.country_timezones:
#    print(pytz.country_timezones[x])
#print()
# for x in tz_list:
#     tz = pytz.timezone(x)
#     print(f'x: {x}, {x.__class__} | tz: {tz}, {tz.__class__}')

# Step 1: create a directory of valid time zones
# -> make a dictionary where the casefold() version of the timezones are the keys
# -> and the actual value required to be input to the pytz.timezone() program is the value
all_tz = sorted(pytz.all_timezones)
tz_directory = dict(zip([x.casefold() for x in all_tz], all_tz))

# Step 2: code section that receives input data from user
# -> Option 1 - take a list of up to 9 valid timezones
# -> Option 2 - take each timezone 1 by 1 and then terminate
# -> each entry should be stored in a list that will be used by later part of program

prompt1 = """Select up to 9 valid timezones to see the local time and UTC time associated.
    Press Enter to start or Enter 0 to Exit:
"""

prompt2 = """Either: 
    (1) Enter a Valid Timezone.
    (2) Enter 1 to see the directory of valid choices.
    (3) Enter 0 to end your list.

(Your choice): """

prompt3 = """Time entered is invalid or was already entered."""

while True:
    c1 = input(prompt1).casefold()
    if c1 == '0':
        break
    i = 0 # valid timezones counter
    tz_list = []

    while True:
        c2 = input("(Your choice): ").casefold()
        if i == 9 or c2 == '0':
            break
        if c2 == '1':
            for x in tz_directory:
                print(x)
            print()
        elif c2 in tz_directory and c2 not in tz_list:
            tz_list.append(c2)
            i += 1
        else:
            print('\n' + prompt3 + '\n')

    print()
    print("Timezone List: ", end='')
    string1 = '['
    for item in tz_list:
        string1 += "'" + tz_directory[item] + "'" + ', '
    string1 = string1.rstrip(' ,') + ']'
    print(string1)
    print()

# Step 3: For each timezone in the list, print the name of the timezone, as well as date/time in local time zone and utc
    for item in tz_list:
        tz_choice = pytz.timezone(tz_directory[item])
        print(tz_choice)
        local_time = datetime.datetime.now(tz=tz_choice).strftime('%A %x %X %z')
        #local_time = pytz.utc.localize(local_time).astimezone() # no need to convert with .astimezone() because its not niave previous tz set
        utc_time = datetime.datetime.utcnow()
        utc_time = pytz.utc.localize(utc_time).strftime('%A %x %X %z')
        #print(f'\tLocal Time: {datetime.datetime.now(tz=tz_choice)}')
        #print(f'\tUTC Time: {datetime.datetime.utcnow()}')
        print(f'\tLocal Time: {local_time}') # required when using localizing if you want the time zone
        print(f'\tUTC Time: {utc_time}')
        print()

# Step 4: Allow user to exit program
    break