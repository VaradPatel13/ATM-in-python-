import random
import sqlite3

class Atm:
    def __init__(self):
        self.conn = sqlite3.connect('atm_database.db')
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS accounts (
                accno INTEGER PRIMARY KEY,
                name TEXT,
                mobileno TEXT,
                address TEXT,
                balance REAL,
                password TEXT
            )''')

    def insert_account(self, accno, name, mobileno, address, balance, password):
        with self.conn:
            self.conn.execute('''INSERT INTO accounts (accno, name, mobileno, address, balance, password)
                VALUES (?, ?, ?, ?, ?, ?)''', (accno, name, mobileno, address, balance, password))

    def get_account(self, accno):
        with self.conn:
            cursor = self.conn.execute('''SELECT * FROM accounts WHERE accno = ?''', (accno,))
            return cursor.fetchone()

    def update_account(self, accno, column, value):
        with self.conn:
            self.conn.execute(f'''UPDATE accounts SET {column} = ? WHERE accno = ?''', (value, accno))

    def delete_account(self, accno):
        with self.conn:
            self.conn.execute('''DELETE FROM accounts WHERE accno = ?''', (accno,))

    def createaccount(self):
        print('_' * 50)
        name = input("Enter name: ")
        mobileno = input("Enter mobile number: ")
        address = input("Enter address: ")
        balance = float(input("Enter balance: "))
        password = input("Enter password: ")
        print('_' * 50)
        accno = random.randint(100000, 999999)

        if self.get_account(accno):
            print("Account number already exists!")
        else:
            self.insert_account(accno, name, mobileno, address, balance, password)
            print("Account created successfully!")
            print("Account Number:", accno)

    def loginacc(self):
        print('_' * 50)
        accno = int(input("Enter account number: "))
        print('_' * 50)
        account = self.get_account(accno)
        if account:
            password = input("Enter password: ")
            if account[5] == password:
                print("Login successful!")
                print("Name:", account[1])
                print("Mobile Number:", account[2])
                print("Address:", account[3])
                print("Balance:", account[4])
                self.Atmmenu(accno)
            else:
                print("Invalid password!")
        else:
            print("Account not found!")

    def totalacc(self):
        print('_' * 50)
        with self.conn:
            cursor = self.conn.execute('''SELECT COUNT(*) FROM accounts''')
            return cursor.fetchone()[0]

    def totalbalance(self):
        print('_' * 50)
        with self.conn:
            cursor = self.conn.execute('''SELECT SUM(balance) FROM accounts''')
            return cursor.fetchone()[0]

    def view_accounts(self):
        with self.conn:
            cursor = self.conn.execute('''SELECT * FROM accounts''')
            rows = cursor.fetchall()
            if rows:
                print("Account Details".center(50, '-'))
                for row in rows:
                    print(f"Account Number: {row[0]}")
                    print(f"Name: {row[1]}")
                    print(f"Mobile Number: {row[2]}")
                    print(f"Address: {row[3]}")
                    print(f"Balance: {row[4]}")
                    print(f"Password: {row[5]}")
                    print("-" * 50)
            else:
                print("No accounts found!")

    def atmenu(self):
        while True:
            print('*' * 50)
            print("ATM MENU".center(50, '-'))
            print('*' * 50)
            print()
            print("1. Create Account")
            print("2. Login Account")
            print("3. Total Accounts")
            print("4. Total Balance")
            print("5. View Accounts")
            print("6. Exit")
            print('*' * 50)
            choice = input("Enter your choice: ")

            if choice == "1":
                self.createaccount()
            elif choice == "2":
                self.loginacc()
            elif choice == "3":
                total = self.totalacc()
                print("Total accounts:", total)
            elif choice == "4":
                balance = self.totalbalance()
                print("Total balance:", balance)
            elif choice == "5":
                self.view_accounts()
            elif choice == "6":
                print("Exiting ATM...")
                break
            else:
                print("Invalid choice! Please try again.")

    def Atmmenu(self, accno):
        while True:
            print('*' * 50)
            print("Account Menu:".center(50, '-'))
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Info")
            print("5. Send Money")
            print("6. Logout")
            print('*' * 50)
            choice = input("Enter your choice: ")

            if choice == "1":
                self.withdraw(accno)
            elif choice == "2":
                self.deposit(accno)
            elif choice == "3":
                self.checkbalance(accno)
            elif choice == "4":
                self.infomenu(accno)
            elif choice == "5":
                self.SendMoney(accno)
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice! Please try again.")

    def infomenu(self, accno):
        while True:
            print('*' * 50)
            print("Info Menu:")
            print("1. Change PIN")
            print("2. Change Mobile Number")
            print("3. Change Name")
            print("4. Change Address")
            print("5. Exit")
            print('*' * 50)
            choice = input("Enter your choice: ")

            if choice == "1":
                self.changepin(accno)
            elif choice == "2":
                self.changemobileno(accno)
            elif choice == "3":
                self.chgname(accno)
            elif choice == "4":
                self.changeaddress(accno)
            elif choice == "5":
                print("Exiting Info Menu...")
                break
            else:
                print("Invalid choice! Please try again.")

    def SendMoney(self, accno):
        with self.conn:
            cursor = self.conn.execute('''SELECT * FROM accounts''')
            rows = cursor.fetchall()
            if rows:
                mobileno = input("Enter Mobile Number: ")
                for account in rows:
                    if account[2] == mobileno:
                        print("Account Found!")
                        print("Name:", account[1])
                        print("Mobile Number:", account[2])
                        print("Address:", account[3])
                        amount = float(input("Enter amount to Send: "))
                        if amount <= 0:
                            print("Invalid amount entered. Please enter a positive number.")
                            return
                        if account[4] < amount:
                            print("Insufficient balance in the account.")
                            return
                        new_balance = account[4] + amount
                        self.update_account(account[0], 'balance', new_balance)
                        print("Money Send successful!")
                        account = self.get_account(accno)
                        new_balance1 = account[4] - amount
                        self.update_account(accno, 'balance', new_balance1)
                        break
                else:
                    print("Invalid Mobile Number!")
            else:
                print("Account not found!")

    def receipt(self, account):
        choice = input("Do you want a transaction receipt? (y/n): ")
        if choice.lower() == "y":
            print("Transaction Receipt".center(50, '-'))
            print("-" * 30)
            print("Name:", account[1])
            print("Current Balance:", account[4])
            print("Mobile Number:", account[2])
            print("Address:", account[3])
            print("-" * 30)
            print("Thanks for using our services!")
        else:
            print("No receipt issued.")

    def withdraw(self, accno):
        amount = float(input("Enter amount to withdraw: "))
        account = self.get_account(accno)
        if account[4] >= amount:
            new_balance = account[4] - amount
            self.update_account(accno, 'balance', new_balance)
            print("Withdrawal successful!")
            print("Updated Balance:", new_balance)
        else:
            print("Insufficient funds!")

    def deposit(self, accno):
        amount = float(input("Enter amount to deposit: "))
        account = self.get_account(accno)
        new_balance = account[4] + amount
        self.update_account(accno, 'balance', new_balance)
        print("Deposit successful!")
        print("Updated Balance:", new_balance)

    def checkbalance(self, accno):
        account = self.get_account(accno)
        print("Current Balance:", account[4])

    def changepin(self, accno):
        new_pin = input("Enter new PIN: ")
        self.update_account(accno, 'password', new_pin)
        print("PIN changed successfully!")

    def changemobileno(self, accno):
        new_mobileno = input("Enter new mobile number: ")
        self.update_account(accno, 'mobileno', new_mobileno)
        print("Mobile number changed successfully!")

    def chgname(self, accno):
        new_name = input("Enter new name: ")
        self.update_account(accno, 'name', new_name)
        print("Name changed successfully!")

    def changeaddress(self, accno):
        new_address = input("Enter new address: ")
        self.update_account(accno, 'address', new_address)
        print("Address changed successfully!")

    def __del__(self):
        self.conn.close()

# Create and run the ATM system
atm = Atm()
atm.atmenu()
