#Nima Gyeltshen
#1 Electrical Engg.
#02230067
#Reference
#https://www.youtube.com/watch?v=BRssQPHZMrc
#https://www.youtube.com/watch?v=pTB0EiLXUC8
#https://www.youtube.com/watch?v=qiSCMNBIP2g

import os   # module for interacting operating system
import random   # module for generating random numbers
import string   # module for generating random strings

# base account class
class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    # depositing money 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Nu{amount}. New Balance: Nu{self.balance}")
        else:
            print("error")

    # withdrawing money 
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: Nu{amount}. New Balance: Nu{self.balance}")
        else:
            print("Error")

    #saving the data of the banking in a file
    def save_to_file(self, file_name='accounts.txt'):
        with open(file_name, 'a') as f:
            f.write(f"{self.account_number},{self.password},{self.account_type},{self.balance}\n")


# Personal Account class
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0):
        #using inheritance
        super().__init__(account_number, password, 'personal', balance)

# bussiness Account class
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0):
        #using inheritance
        super().__init__(account_number, password, 'business', balance)

# enerating account number
def generate_account_number():
    return ''.join(random.choices(string.digits, k=6))

#generating passwords for the account
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=3))

# data file for storing  banking data
def load_accounts(file_name='accounts.txt'):
    accounts = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                account_number, password, account_type, balance = line.strip().split(',')
                balance = float(balance)
                if account_type == 'personal':
                    account = PersonalAccount(account_number, password, balance)
                elif account_type == 'business':
                    account = BusinessAccount(account_number, password, balance)
                accounts[account_number] = account
    return accounts

# logging in an account
def login(accounts):
    #prompt user to enter acc. no and password
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    
    account = accounts.get(account_number)
    if account and account.password == password:
        print("Login successful")
        return account
    else:
        print("Error")
        return None


# transfer of money
def fund_transfer(accounts, from_account):
    #prompt user to enter the recipient acc. and amount to be transfered
    to_account_number = input("Enter the recipient's account number: ")
    amount = float(input("Enter the amount to send: "))
    if to_account_number in accounts:
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            accounts[to_account_number].deposit(amount)
            print(f"Transferred Nu{amount} to {to_account_number}")
        else:
            print("Error")
    else:
        print("error")

# main function
def main():
    accounts = load_accounts()

    while True:
        # Options
        print("\n Welcome to Gyeltshen Bank")
        print("1. Open an Account")
        print("2. Login to Account")
        print("3. Exit")
        #promnpt user to choose
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Select Account Type:")
            print("1. Personal Account")
            print("2. Business Account")
            account_type = input("Enter your choice: ")
            if account_type in ['1', '2']:
                account_number = generate_account_number()
                password = generate_password()
                if account_type == '1':
                    account = PersonalAccount(account_number, password)
                else:
                    account = BusinessAccount(account_number, password)
                account.save_to_file()
                accounts[account_number] = account
                print(f"Account created successfully! Account Number: {account_number}, Password: {password}")
            else:
                print("Error")

        elif choice == '2':
            account = login(accounts)
            if account:
                while True:
                    print("\n option")
                    print("1. Balance")
                    print("2. Deposit ")
                    print("3. Withdraw ")
                    print("4. Transfer funds")
                    print("5. Delete Account")
                    print("6. Logout")
                    #prompt user to choose
                    account_choice = input("Enter your choice: ")

                    if account_choice == '1':
                        print(f"Your Balance: Nu{account.balance}")
                    elif account_choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif account_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif account_choice == '4':
                        fund_transfer(accounts, account)
                    elif account_choice == '5':
                        del accounts[account.account_number]
                        print("Account deleted ")
                        break
                    elif account_choice == '6':
                        print("Successful")
                        break
                    else:
                        print("Error")
        
        elif choice == '3':
            print("Thank you for using Gyeltshen Bank")
            break

        else:
            print("error")

# Function call
if __name__ == "__main__":
    main()