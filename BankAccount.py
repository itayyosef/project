## Itay Yosef 7732/4
import json
import random
class BankAccount():
    account_counter = 1
    def __init__(self,Account_name,Balance,Pin):
        self.Account_name = Account_name
        self.Account_sn = str(random.randint(200000,999999))
        self.Balance = Balance
        self.Pin = Pin
        self.account_details = {
                                "Account name":self.Account_name,
                                "Account SN":self.Account_sn,
                                "Account Balance":self.Balance,
                                "Account Pin":self.Pin
                                }                  
        BankAccount.account_counter += 1

    def deposit(self,amount:int):
        with open("accounts.json","r") as file:
            account_data = json.load(file)
            for account in account_data:
                if amount > 0:
                    if account["Account name"] == self.Account_name and account["Account Pin"] == self.Pin:
                        account["Account Balance"] += amount
                else:
                    raise ValueError("The amount must be positive number for depositing , not a negative , please try again ")
        with open("accounts.json","w") as file:
            json.dump(account_data,file,indent=4)

    def withdraw(self,amount:int):
        with open("accounts.json","r") as file:
            account_data = json.load(file)
            for account in account_data:
                if amount > 0:
                    if account["Account name"] == self.Account_name and account["Account Pin"] == self.Pin:
                        account["Account Balance"] -= amount
                else:
                    raise ValueError("The amount must be a positive number for withdrawing , not a negative , please try again")
        with open("accounts.json","w") as file:
            json.dump(account_data,file,indent=4)

    def transfer(self,amount_for_transfer:int,other_account_sn:str):
        with open("accounts.json","r") as file:
            account_data = json.load(file)
            for account in account_data:
                if account["Account SN"] == other_account_sn:
                    account["Account Balance"] += amount_for_transfer
            for account in account_data:
                if account["Account name"] == self.Account_name and account["Account Pin"] == self.Pin:
                    account["Account Balance"] -= amount_for_transfer
        #  הסכומים החדשים יצטברו ישירות לקובץ ג'ייסון
        with open("accounts.json","w") as file:
            json.dump(account_data,file,indent=4)

    def show_balance(self):
        with open("accounts.json","r") as file:
            account_data = json.load(file)
        for account in account_data:
            if account["Account name"] == self.Account_name and account["Account Pin"] == self.Pin:
                print(f"The current balance in {account['Account name']}'s account is : {account['Account Balance']} $")

    def change_pin(self,pin:str):
        try:
            new_pin = int(pin)   # אם מכניסים סטרינג  של אותיות יקבל שגיאה
        except ValueError:
            while pin.isdigit() == False or len(pin) != 4:
                print("please enter a 4 digit number to change PIN , without letters.")
                pin = input("enter a new PIN here please")
        new_pin = pin

        with open("accounts.json","r") as file:
            file_data = json.load(file)
            for account in file_data:
                if account["Account Pin"] == self.Pin:
                    account["Account Pin"] = new_pi

        with open("accounts.json","w") as file:
            json.dump(file_data,file,indent = 4)

    def save_info(self):
        try:
            with open("accounts.json","r",) as file:
                all_accounts = json.load(file) # נסיון פתיחת קובץ ריק לקריאה
        except FileNotFoundError:
            all_accounts = []   # ליצור רשימה שתכיל את כל המשתמשים אם אין כלום בקובץ
        all_accounts.append(self.account_details)
        with open("accounts.json","w") as file:  # כל פעם לדרוס את הקובץ , ולהוסיף את המשתמש החדש
            json.dump(all_accounts,file,indent=4)
