import sqlite3 # how to add linter for Python and SQLite3

db = sqlite3.connect("contacts.db") # connect to sqlite database (creates or opens existing)

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
# Without resetting the cursor (iterator), nothing is returned

cursor = db.cursor() # create a cursor (generator)
cursor.execute("SELECT * FROM contacts")

print('-' * 20)

# .fetchall() and .fetchone()
#print(cursor.fetchall()) # returns list containing tuple of all rows in database, but prints cursor to end of Query
#print(cursor.fetchone()) # grabs current row of cursor and incriments index by one
#print(cursor.fetchone()) # same
#print(cursor.fetchone()) # Returns nothing because cursor reached end of table

for name, phone, email in cursor:
    #print(name, phone, email, sep=" | ")
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.commit() # Must commit changes to database to save your work | otherwise they are lost when connection is closed

db.close() # closes the connection
