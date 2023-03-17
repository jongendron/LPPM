# Make sure to install Pylint
# Simple demonstration on how to create a bank account
# class attributes name with '__' prefix are "mangeled"
# meaning a new local variable is created in an instance
import datetime
import pytz


class Account:
    """ Simple account class with balance """

    # Static methods are shared by all instances of class
    # these do not call on instance (self)
    # '_' prefix shows it is nonpublic
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    # class creation involves two steps
    # 1st: __new__ takes care of creation (actual constructor, but not always required)
    # 2nd: __init__ customizes
    def __init__(self, name="Account1", balance=0):
        """ Initialize instance """
        self._name = name
        self._balance = balance
        #self._transaction_list = []
        self._transaction_list = \
            [(Account._current_time(), balance)]
        print("Account created for " + self._name + \
              f".\nBalance is {self._balance}")

    def deposit(self, amount):
        """ Deposit cash """
        if amount > 0:
            self._balance += amount
            self.show_balance() # call method from within another
            #self._transaction_list \
            #    .append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list \
                .append((Account._current_time(), amount))
            
    def withdraw(self, amount):
        """ Withdraw money """
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list \
                .append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than current balance")
        #show_balance() # must callon self.method()
        self.show_balance()

    def show_balance(self):
        """ Show balance in account """
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})" \
                  .format(amount, tran_type, date, date.astimezone()))
            
if __name__ == '__main__':
    jon = Account("Jon", 0)
    jon.show_balance()
    jon.deposit(1000)
    #jon.show_balance()
    jon.withdraw(500)
    #jon.show_balance()
    jon.withdraw(2000)
    print()
    jon.show_transactions()

    chris = Account("Christine", 800)
    chris.deposit(100)
    chris.withdraw(200)
    chris.show_transactions()
    bob = Account("Bob", 100)

    #print('\n', f'{bob.__name} | {bob._balance}') # __name fails because local is created in bob instance called '_Account__name' from mangeling
    # print('\n', f'{bob._name} | {bob._balance}') # __name fails because local is created in bob instance called '_Account__name' from mangeling
    # print()
    # print(Account.__dict__)
    # print()
    # print(bob.__dict__)