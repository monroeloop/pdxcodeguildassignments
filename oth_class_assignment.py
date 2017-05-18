class BankAccount:
    def __init__(self, bal, name):
        self.balance = bal
        self.name = name

    def greet_balance(self):
        print('Hello {}, your balance is ${}.'.format(self.name, self.balance))

    def withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('You have withdrawn ${}, your balance is now ${}.'.format(amount, self.balance))
        else:
            print('You do not have enough money dude.')

    def deposit(self, amount):
        self.balance += amount
        print('You deposited ${}'.format(amount))


class BankAccountRestricted(BankAccount):
    def __init__(self, bal, name):
        BankAccount.__init__(self, bal, name)

    def withdrawal(self, amount):
        if self.balance - amount -100 >= 0:
            self.balance -= amount
            print('You have withdrawn ${}, your balance is now ${}.'.format(amount, self.balance))
        else:
            print('You do not have enough money dude.')

chris = BankAccountRestricted(100, 'Chris')
katie = BankAccount(20, 'Katie')

chris.greet_balance()
# katie.greet_balance()
chris.withdrawal(201)
# chris.withdrawal(100)
chris.deposit(400)
