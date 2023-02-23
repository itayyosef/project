## Itay Yosef 7732/4
from BankAccount import BankAccount
import json
import random
def main_menu():
    print(f"""
        MAIN MENU:

        Press (1) to make an account
        Press (2) to log in
        Press (3) to skip to examples
    """)
main_menu()
choice = int(input("enter your choice please - 1 , 2 or 3 or 0 to stop : "))
while choice != 0:
    if choice == 1:
        account_name = input("enter your account name : ")
        account_pin = input("enter the desired 4 digit PIN code : ")
        while len(account_pin) != 4:
            account_pin = input("enter the desired 4 digit PIN code : ")
        balance = 0
        new_account = BankAccount(account_name,balance,account_pin)
        new_account.save_info()
        main_menu()
        choice = int(input("enter your choice please - 1 , 2 or 3 or 0 to stop : "))
        
    elif choice == 2:
        account_name = input("Please enter your name : ")
        account_sn = input("Please enter your SN : ")
        account_pin = input("enter your 4 digit PIN code :")
        with open("accounts.json","r") as file:
            account_data = json.load(file)
            current_account = BankAccount(account_name,None,account_pin)
            for account in account_data:
                if account['Account name'] == current_account.Account_name and account['Account Pin'] == current_account.Pin and account['Account SN'] == account_sn:
                    print(f"Hello {current_account.account_details['Account name']}! Welcome back")
                    print(f"""
                    This is the option menu for possible actions in your account , press 0 to exit to main menu  : 

                    0. Go to Main Menu.
                    1. Withdrawal of cash.
                    2. Cash deposit.
                    3. Credit transfer to another account.
                    4. Change PIN.
                    5. Display current balance.
                    """)
                    action = int(input("enter your action please : "))
                    while action != 0:
                        if action == 1:
                            try:
                                amount = int(input("Enter the amount to withdraw : "))
                                current_account.withdraw(amount)
                                action = int(input("please re-enter your next action : "))
                            except ValueError as error:
                                print(error)
                        elif action == 2:
                            try:
                                amount = int(input("Enter the amount to deposit : "))
                                current_account.deposit(amount)
                                action = int(input("please re-enter your next action : "))
                            except ValueError as error:
                                print(error)
                        elif action == 3:
                            amount = int(input("Enter the amount to transfer : "))
                            other_account_sn = input("Enter the serial number (SN) of the account you want to transfer to : ")
                            current_account.transfer(amount,other_account_sn)
                            action = int(input("please re-enter your next action : "))
                        elif action == 4:
                            pin = input("Enter the new 4 digit PIN : ")
                            current_account.change_pin(pin)
                            action = int(input("please re-enter your next action : "))
                            # to change a Pin multiple times , please log in again using the new pin.
                        elif action == 5:
                            current_account.show_balance()
                            action = int(input("please re-enter your next action : "))
                    else:
                        main_menu()
                        choice = int(input("enter your choice please - 1 , 2 or 3 or 0 to stop : "))
                else:
                    continue
            else:
                print("Sorry, we have no user that uses these credentials, please try again")
        main_menu()
        choice = int(input("enter your choice please - 1 , 2 or 3 or 0 to stop : "))

    elif choice == 3:
        example1 = BankAccount("davidesko",0,"1234")
        example1.deposit(1000)         # testing ground to test the methods with any names from the json file
        #example1.withdraw(600)
        #example1.transfer(500,"495355")
        #example1.show_balance()
        #example1.save_info()
        #example1.change_pin("2346")
        main_menu()
        choice = int(input("enter your choice please - 1 , 2 or 3 or 0 to stop : "))


