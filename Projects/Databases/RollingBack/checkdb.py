import sqlite3
import pytz

#db = sqlite3.connect("accounts.db")
db = sqlite3.connect("accounts.db", detect_types=sqlite3.PARSE_DECLTYPES) # automatically check for field types and convert when extracted with Python
# More info: https://docs.python.org./3.5/library/sqlite3.html#using-adapters-to-store-additional-python-types-in-sqlite-database
# Does not have timezone awareness

for row in db.execute("SELECT * FROM history"):
    #utc_time = row[0]
    #local_time = pytz.utc.localize(utc_time).astimezone() # convert to local time with timezone awareness
    utc_time = pytz.utc.localize(row[0]) # convert to timezone aware object
    local_time = utc_time.astimezone()
    #print("{}\t{}".format(local_time, type(local_time))) # not timezone aware
    print("{}\t{}".format(utc_time, local_time)) # not timezone aware

db.close()