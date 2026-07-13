#=========================================

# Project: Banking System
# Author: Muhammad Ahtsham Javed
# Language: Python
# version: 1.0

#=========================================

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(("deposit", amount, self.balance))
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            self.transactions.append(("withdraw", amount, self.balance))
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

    def display_transaction_history(self):
        if not self.transactions:
            print("No transactions yet.")
            return

        print("Transaction history:")
        for index, (transaction_type, amount, balance) in enumerate(self.transactions, start=1):
            if transaction_type == "deposit":
                print(f"{index}. Deposit: ${amount} | Balance: ${balance}")
            else:
                print(f"{index}. Withdrawal: ${amount} | Balance: ${balance}")

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print(f"Account created for {account_holder} with account number {account_number}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def display_account_info(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def get_total_accounts(self):
        return len(self.accounts)

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return

        print("Existing accounts:")
        for index, account in enumerate(self.accounts.values(), start=1):
            print(f"{index}. {account}")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_amount(prompt):
    while True:
        value = input(prompt).strip()
        try:
            amount = float(value)
        except ValueError:
            print("Please enter a valid numeric amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            return amount


def main():
    bank = Bank()
    separator = "=" * 35
    while True:
        print(separator)
        print("    Banking System Menu    ")
        print(separator)
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. View transaction history")
        print("6. Display account info")
        print("7. View all accounts")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()
        if choice not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
            print("Invalid choice. Please try again.")
            continue

        if choice == "1":
            account_number = get_non_empty_input("Enter account number: ")
            account_holder = get_non_empty_input("Enter account holder name: ")
            bank.create_account(account_number, account_holder)

        elif choice == "2":
            account_number = get_non_empty_input("Enter account number: ")
            amount = get_valid_amount("Enter deposit amount: ")
            bank.deposit_to_account(account_number, amount)

        elif choice == "3":
            account_number = get_non_empty_input("Enter account number: ")
            amount = get_valid_amount("Enter withdrawal amount: ")
            bank.withdraw_from_account(account_number, amount)

        elif choice == "4":
            account_number = get_non_empty_input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Current balance: ${account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = get_non_empty_input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.display_transaction_history()
            else:
                print("Account not found.")

        elif choice == "6":
            account_number = get_non_empty_input("Enter account number: ")
            bank.display_account_info(account_number)

        elif choice == "7":
            print(f"Total accounts: {bank.get_total_accounts()}")
            bank.display_all_accounts()

        elif choice == "8":
            print("Thank you for using the banking system.")
            break


if __name__ == "__main__":
    main()

