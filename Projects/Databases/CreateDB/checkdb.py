# TODO: Modify this program so it asks user to enter a name, then use a WHERE clause in the SQL statement to retrieve just the row for that one person.

import sqlite3

db = sqlite3.connect("contacts.db")

sqlcmd = "SELECT * FROM contacts WHERE contacts.name LIKE ?"
name = input("Specify a name: ")

print('-' * 20)
#for name, phone, email in db.execute("SELECT * FROM contacts"):
for name, phone, email in db.execute(sqlcmd, (name,)): # tuples with one element need comma, otherwise its saved as a string, and this will pass as multiple arguements, equal to length string
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.close()

