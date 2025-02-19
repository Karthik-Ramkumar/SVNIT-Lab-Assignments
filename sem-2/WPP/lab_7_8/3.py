class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}  # Dictionary to store accounts (account_number: Account object)

    def create_account(self, account_number, customer_name, initial_deposit):
        if account_number in self.accounts:
            print("Account number already exists.")
            return None
        account = Account(account_number, customer_name, initial_deposit)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None

    def display_accounts(self):
        print(f"\n--- {self.bank_name} Accounts ---")
        for account_number, account in self.accounts.items():
            account.display()


class Account:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
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
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")


my_bank = Bank("My Bank")
account1 = my_bank.create_account("12345", "Alice", 1000)
account2 = my_bank.create_account("67890", "Bob", 500)

if account1:
    account1.deposit(500)
    account1.withdraw(200)

my_bank.display_accounts()

account_bob = my_bank.get_account("67890")
if account_bob:
  account_bob.display()