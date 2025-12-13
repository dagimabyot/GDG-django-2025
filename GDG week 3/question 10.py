class BankAcoount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.__balance
    
account = BankAcoount("10000447687234", 1000)
account.deposit(500)
print(account.get_balance())

account.withdraw(300)  
print(account.get_balance())   