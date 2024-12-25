import random

class Atm:
    def __init__(self):
        self.accounts = {}  

    def createaccount (self):
        print('_'*50)
        name = input("Enter name: ")
        mobileno = input("Enter mobile number: ")
        address = input("Enter address: ")
        balance = float(input("Enter balance: "))
        password = input("Enter password: ")
        print('_'*50)
        

        accno = random.randint(100000, 999999)  

        if accno in self.accounts:
            print("Account number already exists!")
        else:
            self.accounts[accno] = {'name': name, 'mobileno': mobileno, 'address': address,
                                             'balance': balance, 'password': password}
            print("Account created successfully!")
            print("Account Number:", accno)

    def loginacc(self):
        print('_'*50)
        accno = int(input("Enter account number: "))
        print('_'*50)          
        if accno in self.accounts:
            password = input("Enter password: ")
            account = self.accounts[accno]
            if account['password'] == password:
                print("Login successful!")
                print("Name:", account['name'])
                print("Mobile Number:", account['mobileno'])
                print("Address:", account['address'])
                print("Balance:", account['balance'])
                self.Atmmenu(accno)
                return
            else:
              print("Invalid password!")
        else:
           print("Account not found!")


    def totalacc(self):
        print('_'*50)
        return len(self.accounts)
        print('_'*50)

    def totalbalance (self):
        print('_'*50)
        total = sum(account['balance'] for account in self.accounts.values())
        print('_'*50)
        return total

    def atmenu(self):
        while True:
            print('*'*50)
            print("ATM MENU".center(50,'-'))
            print('*'*50)
            print()
            print("1. Create Account")
            print("2. Login Account")
            print("3. Total Accounts")
            print("4. Total Balance")
            print("5. Exit")
            print('*'*50)
            print('*'*50)
            choice = input("Enter your choice : ")

            if choice == "1":
                self.createaccount ()
            elif choice == "2":
                self.loginacc()
            elif choice == "3":
                total = self.totalacc()
                print("Total accounts:", total)
            elif choice == "4":
                balance = self.totalbalance ()
                print("Total balance:", balance)
            elif choice == "5":
                print("Exiting ATM...")
                break
            else:
                print("Invalid choice! Please try again.")

    def Atmmenu(self, accno):
        while True:
            print('*'*50)
            print("Account Menu:".center(50,'-'))
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Info")
            print("5. Logout")
            print('*'*50)
            choice = input("Enter your choice (1 to 5): ")

            if choice == "1":
                self.withdraw(accno)
            elif choice == "2":
                self.deposit(accno)
            elif choice == "3":
                self.checkbalance(accno)
            elif choice == "4":
                self.infomenu(accno)
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice! Please try again.")

    def infomenu(self, accno):
         while True:
            print('*'*50)
            print("Info Menu:")
            print("1. Change PIN")
            print("2. Change Mobile Number")
            print("3. Change Name")
            print("4. Change Address")
            print("5. Exit")
            print('*'*50)
            choice = input("Enter your choice (1-5): ")

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

    def withdraw(self, accno):
        amount = float(input("Enter amount to withdraw: "))
        account = self.accounts[accno]
        if amount <= account['balance']:
            account['balance'] -= amount
            print("Withdrawal successful!")
            print("Updated Balance:", account['balance'])
            self.receipt(account)
        else:
            print("Insufficient funds!")

    def deposit(self, accno):
        amount = float(input("Enter amount to deposit: "))
        account = self.accounts[accno]
        account['balance'] += amount
        print("Deposit successful!")
        print("Updated Balance:", account['balance'])
        self.receipt(account)

    def receipt(self, account):
        choice = input("Do you want a transaction receipt? (y/n): ")
        if choice.lower() == "y":
            print("Transaction Receipt".center(50,'-'))
            print("-" * 30)
            print("Name:", account['name'])
            print("-" * 30)
            print("Current Balance:", account['balance'])
            print("-" * 30)
            print("Mobile Number:", account['mobileno'])
            print("-" * 30)
            print("Address:", account['address'])
            print("-" * 30)
            print("-" * 30)
 
            print("Thanks for using our services!")
            print("-" * 30)
        else:
            print("Wrong choice")

    def checkbalance(self, accno):
        account = self.accounts[accno]
        print("Current Balance:", account['balance'])

    def changepin(self, accno):
        new_pin = input("Enter new PIN: ")
        account = self.accounts[accno]
        account['password'] = new_pin
        print("PIN changed successfully!")

    def changemobileno(self, accno):
        new_mobileno = input("Enter new mobile number: ")
        account = self.accounts[accno]
        account['mobileno'] = new_mobileno
        print("Mobile number changed successfully!")

    def chgname(self, accno):
        new_name = input("Enter new name: ")
        account = self.accounts[accno]
        account['name'] = new_name
        print("Name changed successfully!")

    def changeaddress(self, accno):
        new_address = input("Enter new address: ")
        account = self.accounts[accno]
        account['address'] = new_address
        print("Address changed successfully!")



atm = Atm()
atm.atmenu()