import sqlite3 # how to add linter for Python and SQLite3

db = sqlite3.connect("contacts.db") # the connection contains a cursor when created

# Command to count rows updated by SQLite command
# In this case we are executing to the cursor not the connection directly
# Using variable substituion now (Python method and SQLite method)

new_email = "newest-update@update.com"
#phone = 1234
phone = input("Please enter the phone number: ")

update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?" # SQLite substitution (don't enclose ? in single or double quote)
# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone) # Python substitution
#update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.phone = 1234" # saved command
#update_sql = "UPDATE contacts SET email = 'update@update.com'" # saved command
print(update_sql)

update_cursor = db.cursor() # creates new cursor with same position as db connection (essentially resets it)
#update_cursor.execute(update_sql) # designed to execute single sql statement.
#update_cursor.executescript(update_sql) # designed to run more than 1 sql statement in single call, separated by ";"s. Doesn't set the line counter correctly though b/c of this.
update_cursor.execute(update_sql, (new_email, phone)) # SQLite variable substitution (placeholders). This is safer against INJECTION ATTACKS. Avoid external parameter substitution.

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