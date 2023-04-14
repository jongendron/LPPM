import sqlite3
from datetime import datetime

db = sqlite3.connect("accounts.sqlite")
#db = sqlite3.connect("accounts.db")

# SQLite has 5 column/field storage classes (not data types): https://www.sqlite.org/datatype3.html
# ... apart from integer primary key fields, you can actually store any kind of value in any kind of column
# Datetime values can be handled by Python sqlite3 library supports datetime values (performs conversion automatically to/from datetime values)
db.execute("CREATE TABLE IF NOT EXISTS  accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)") # more data efficient to keep balance in separate table
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL," 
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))") # composit key made up of time and account


# Working in Cents (100ths of dollar) to avoid decimal data loss from binary transactions
class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,)) # filter database to only include name
        row = cursor.fetchone() # fetch the first row (as tuple) or None if data exists 
        # TODO: should only be 1 for the unique name, but this isn't handled yet here

        #if row is not None: # same
        if row: # there was data for this person
            self.name, self._balance = row # set the name and balance based on db
            print("Retrieved record for {} from database. ".format(self.name), end='')
        else: # database does not contain data for this person
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance)) # add person to accounts table of database 
            time = datetime.utcnow()
            cursor.execute("INSERT INTO transactions VALUES(?, ?, ?)", (time, name, opening_balance)) # TODO: shouldn't we also add initial row for transactions?
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()
        #self.name = name
        #self._balance = opening_balance
        #print("Account created for {}. ".format(self.name), end='')
        #self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._balance += amount
            print("{:.2f} deposited.".format(amount / 100))
        return self._balance / 100
    
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{:2f} withdrawn.".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero, and no more than your acocount balance.")
            return 0.0
        
    def show_balance(self):
        #print("Balance on account {0.name} is {0._balance}".format(self))
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == "__main__":
    jon = Account("Jon")
    jon.deposit(1010)
    jon.deposit(10)
    jon.deposit(10)
    jon.withdraw(30)
    jon.withdraw(0)
    jon.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)

