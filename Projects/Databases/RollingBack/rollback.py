import sqlite3
#from datetime import datetime
import datetime
import pytz

#db = sqlite3.connect("accounts.sqlite")
#db = sqlite3.connect("accounts.db")
db = sqlite3.connect("accounts.db", detect_types=sqlite3.PARSE_DECLTYPES)

# SQLite has 5 column/field storage classes (not data types): https://www.sqlite.org/datatype3.html
# ... apart from integer primary key fields, you can actually store any kind of value in any kind of column
# Datetime values can be handled by Python sqlite3 library supports datetime values (performs conversion automatically to/from datetime values)
db.execute("CREATE TABLE IF NOT EXISTS  accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)") # more data efficient to keep balance in separate table
#db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL," 
#           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))") # composit key made up of time and account
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, utc_offset INTEGER NOT NULL, account TEXT NOT NULL," 
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))") # composit key made up of time and account | this does not add another column that is a tuple

# Create View containing local time instead of UTC
# db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
#     " SELECT history.time AS time, strftime('%Y-%m-%d %H:%M:%S', history.time, 'localtime') AS localtime,"
#     " unixepoch(history.time, 'localtime') / 3600 - unixepoch(history.time, 'utc') / 3600 AS timezone,"
#     " history.account, history.amount FROM history")

db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
    " SELECT strftime('%Y-%m-%d %H:%M:%S', history.time, 'localtime') AS localtime,"
    " history.utc_offset, history.account, history.amount FROM history")

# Working in Cents (100ths of dollar) to avoid decimal data loss from binary transactions
class Account(object):

    @staticmethod
    def _current_time(): # static method for the class (rather than instance)        
        utc_time = pytz.utc.localize(datetime.datetime.utcnow()) # best to convert from utc later
        local_time = utc_time.astimezone()
        utc_offset = local_time.utcoffset()
        #print(utc_time, utc_time.utcoffset(), sep=" | ")
        #print(local_time, local_time.utcoffset(), sep=" | ")
        #return utc_time
        return (utc_time, local_time, utc_offset) # tuple of both
    
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
            #time = datetime.datetime.utcnow()
            #deposit_time = pytz.utc.localize(datetime.datetime.utcnow())
            deposit_time = Account._current_time() # static
            #cursor.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, name, opening_balance)) # TODO: shouldn't we also add initial row for transactions?
            cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?)", (deposit_time[0], deposit_time[2].total_seconds(), name, opening_balance)) # TODO: shouldn't we also add initial row for transactions?
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()
        #self.name = name
        #self._balance = opening_balance
        #print("Account created for {}. ".format(self.name), end='')
        #self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        transaction_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name)) # update balance table 
        #db.execute("INSERT INTO history VALUES(?, ?, ?)", (transaction_time, self.name, amount)) # update history table
        db.execute("INSERT INTO history VALUES(?, ?, ?, ?)", (transaction_time[0], transaction_time[2].total_seconds(), self.name, amount)) # update history table
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # #deposit_time = pytz.utc.localize(datetime.datetime.utcnow())
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name)) # update balance table 
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount)) # update history table
            # db.commit()
            # self._balance += amount 
            self._save_update(amount)
            print("{:.2f} deposited.".format(amount / 100))
        return self._balance / 100
    
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:            
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name)) # update balance table 
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount)) # update history table
            # db.commit()
            # self._balance -= amount
            self._save_update(-amount) # negate for withdrawal
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
    #jon.withdraw(0)
    jon.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)

