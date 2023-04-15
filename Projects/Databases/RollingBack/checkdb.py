import sqlite3

#db = sqlite3.connect("accounts.db")
db = sqlite3.connect("accounts.db", detect_types=sqlite3.PARSE_DECLTYPES) # automatically check for field types and convert when extracted with Python
# More info: https://docs.python.org./3.5/library/sqlite3.html#using-adapters-to-store-additional-python-types-in-sqlite-database
# Does not have timezone awareness

for row in db.execute("SELECT * FROM history"):
    #print(row)
    local_time = row[0] # extract time
    print("{}\t{}".format(local_time, type(local_time))) # is a string

db.close()