class Bank_Account:
    def __init__(self, balance = 0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def print_bal(self):
        print(self._balance)

account1 = Bank_Account(200)
account1.print_bal()
account1.deposit(300)
account1.print_bal()
account1.withdraw(200)
account1.print_bal()

