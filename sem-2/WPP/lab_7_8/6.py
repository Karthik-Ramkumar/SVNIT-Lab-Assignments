class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


# Example usage:
my_account = BankAccount("12345", 1000)
my_account.deposit(500)
my_account.withdraw(200)
my_account.display()