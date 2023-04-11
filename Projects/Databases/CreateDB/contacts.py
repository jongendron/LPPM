import sqlite3 # how to add linter for Python and SQLite3

db = sqlite3.connect("contacts.sqlite") # connect to sqlite database (creates or opens existing)

# Building
# Semicolons are not necessary for SQLite3 commands when executed through Python
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)") # executes a sqlite3 command
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')") # insert single row
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

# Querying
# cursors = generators: iterable works by generating each value as its used
# In Python we can create iterable objects that return every possible integer number for example
# Here the cursor iterates through each row of the database, creating a temporary object for each
# Does not keep track of previous rows/records because it's not a list, so no way to index the previous or next row at current iteration
cursor = db.cursor() # create a cursor (generator)
cursor.execute("SELECT * FROM contacts")
print('-' * 20)
#for row in cursor:
#    print(row) # each row is printed as a tuple
for name, phone, email in cursor:
    #print(name, phone, email, sep=" | ")
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

# Without resetting the cursor (iterator), nothing is returned
for name, phone, email in cursor:
    #print(name, phone, email, sep=" | ")
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.close() # closes the connection
