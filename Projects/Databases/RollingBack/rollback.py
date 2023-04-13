# Working in Cents (100ths of dollar) to avoid decimal data loss from binary transactions

class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

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
    #jon.deposit(10.10)
    jon.deposit(1010)
    #jon.deposit(0.10)
    jon.deposit(10)
    #jon.deposit(0.10)
    jon.deposit(10)
    #jon.withdraw(0.30)
    jon.withdraw(30)
    #jon.withdraw(0.0)
    jon.withdraw(0)
    jon.show_balance()

