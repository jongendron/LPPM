import sqlite3
import pytz
import pickle

#db = sqlite3.connect("accounts.db")
db = sqlite3.connect("accounts.db", detect_types=sqlite3.PARSE_DECLTYPES) # automatically check for field types and convert when extracted with Python
# More info: https://docs.python.org./3.5/library/sqlite3.html#using-adapters-to-store-additional-python-types-in-sqlite-database
# Does not have timezone awareness

# Convert time to local using Python
# for row in db.execute("SELECT * FROM history"):
#     utc_time = pytz.utc.localize(row[0]) # convert to timezone aware object
#     local_time = utc_time.astimezone()
#     #print("{}\t{}".format(local_time, type(local_time))) # not timezone aware
#     print("{}\t{}".format(utc_time, local_time)) # not timezone aware

# Convert time to local during SQLite Query
# https://www.sqlite.org/lang_datefunc.html

#for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                      "history.account, history.amount FROM history ORDER BY history.time"): # strftime(format, time-value, modifier, modifier, ...)

# for row in db.execute("SELECT history.time AS time, strftime('%Y-%m-%d %H:%M:%S', history.time, 'localtime') AS localtime,"
#                       "unixepoch(history.time, 'localtime') / 3600 - unixepoch(history.time, 'utc') / 3600 AS timezone,"
# "history.account, history.amount FROM history"):
#    print(row)

# for row in db.execute("SELECT * FROM localhistory"):
#     print(row)

# SQLite Functions: https://www.sqlite.org/lang_corefunc.html
for row in db.execute("SELECT * FROM history"):
    utc_time = pytz.utc.localize(row[0])
    pickled_zone = row[2]
    #zone = pytz.timezone("Australia/Adelaide") # works, but "ACDC" does not work (avoid saving tz name to database)
    zone = pickle.loads(pickled_zone)
    local_time = utc_time.astimezone(zone)
    #print("{}\t{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo, zone))
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

print("*" * 60)
for row in db.execute("SELECT * FROM localhistory"):
    print(row)

db.close()