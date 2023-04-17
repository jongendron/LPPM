import sqlite3
#from datetime import datetime
import datetime
import pytz
import pickle

#db = sqlite3.connect("accounts.sqlite")
#db = sqlite3.connect("accounts.db")
db = sqlite3.connect("accounts.db", detect_types=sqlite3.PARSE_DECLTYPES)

# SQLite has 5 column/field storage classes (not data types): https://www.sqlite.org/datatype3.html
# ... apart from integer primary key fields, you can actually store any kind of value in any kind of column
# Datetime values can be handled by Python sqlite3 library supports datetime values (performs conversion automatically to/from datetime values)
db.execute("CREATE TABLE IF NOT EXISTS  accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)") # more data efficient to keep balance in separate table
#db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL," 
#           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))") # composit key made up of time and account
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, utc_offset INTEGER NOT NULL, tz INTEGER NOT NULL," 
           "account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))") # composit key made up of time and account | this does not add another column that is a tuple

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
        
        # Pickeling a class instance (byte stream) -> save to DB column
        # aware time values contains time zone info in it's tz object
        # pickel a class instance -> converts instance into bite stream -> store into a db column
        # similar to serializing a class instance in Java
        tz = local_time.tzinfo
        return (utc_time, local_time, utc_offset, tz) # tuple of both
        #return 1, local_time, utc_offset, tz # causes ununique Primary key composite (time, account)
    
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
            #deposit_time = Account._current_time() # static
            #cursor.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, name, opening_balance))
            #cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?)", (deposit_time[0], deposit_time[2].total_seconds(), name, opening_balance)) 
            utc_time, _, utc_offset, tz = Account._current_time()
            pickled_tz = pickle.dumps(tz) # byte string object for tz
            cursor.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", (utc_time, utc_offset.total_seconds(), pickled_tz, self.name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()
        #self.name = name
        #self._balance = opening_balance
        #print("Account created for {}. ".format(self.name), end='')
        #self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        utc_time, _, utc_offset, tz = Account._current_time()
        pickled_tz = pickle.dumps(tz) # byte string object for tz

        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name)) # update balance table 
            db.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?)", (utc_time, utc_offset.total_seconds(), pickled_tz, self.name, amount))
        except sqlite3.Error:
            # we roll back changes even despite not calling commit increase there are downstream changes to db
            # without rolling back here, there are changes leaked downstream in the program
            # because in the try block, db.execute() -> accounts does not fail, so those changes carry on to next db.commit()
            db.rollback() # rollback in updates that are pending (don't do what's in the try block)
            #pass
        else:
            db.commit() # only commit if no rollback
            self._balance = new_balance # only update balance if previous transactions don't fail
        #finally:
            #db.commit() # can commit nothing


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

