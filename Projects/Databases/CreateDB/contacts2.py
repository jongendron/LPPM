import sqlite3 # how to add linter for Python and SQLite3

db = sqlite3.connect("contacts.db") # the connection contains a cursor when created

# Command to count rows updated by SQLite command
# In this case we are executing to the cursor not the connection directly

#update_sql = "UPDATE  contacts SET email = 'update@update.com' WHERE contacts.phone = 4567" # saved command
update_sql = "UPDATE  contacts SET email = 'update@update.com'" # saved command

update_cursor = db.cursor() # creates new cursor with same position as db connection (essentially resets it)
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))
print()
print("Cursor and DB object have same connection: {}".format(update_cursor.connection == db))
print()

# Best practice: make commits to database using cursor connection rather than main connection to DB
update_cursor.connection.commit() # commit database changes made with the cursor connection
update_cursor.close()

# Querying with the connection directly (without explicity creating a cursor)

print('-' * 20)
#for row in db.execute("SELECT * FROM contacts"):
#    print(row)
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.close()

# Did we actually update the db?
# Don't think so! we didn't save changes to db connection