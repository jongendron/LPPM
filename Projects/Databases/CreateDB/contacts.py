import sqlite3

db = sqlite3.connect("contacts.sqlite") # connect to sqlite database (creates or opens existing)

db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)") # executes a sqlite3 command
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')") # insert single row
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

db.close() # closes the connection