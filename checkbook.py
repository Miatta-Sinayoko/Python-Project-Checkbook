
import os
import csv

def exit():
    print("Thanks, have a great day!")

def view(balance):
    print("Your current balance is $", balance)

import csv

def deposit(transactions_file ,balance, amount):
    balance = balance +  amount
    print("Deposit of $", amount, "has been recorded.")
    with open(transactions_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount])

def withraw(transactions_file ,balance, amount):
    balance = balance -  amount
    print("withdraw of $", amount, "has been recorded.")
    with open(transactions_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount])

def main():
    # Welcome the user
    print("~~~ Welcome to your terminal checkbook! ~~~")

    # Initialize the balance
    balance = 0

    # Create a file to store the transactions
    transactions_file = "checkbook.csv"

    # Start the main loop
    while True:
        # Display the menu
        print("What would you like to do?")
        print("1) View current balance")
        print("2) Record a debit (withdraw)")
        print("3) Record a credit (deposit)")
        print("4) Exit")

        # Get the user's choice
        user_choice = input("Your choice? ")

        # Validate the user's choice
        while user_choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please enter a number between 1 and 4.")
            user_choice = input("Your choice? ")

        # Perform the user's choice
        if user_choice == "1":
            # View the current balance
            view(balance)

        elif user_choice == "2":
            # Record a debit
            debit_amount = float(input("How much is the debit? "))
            balance -= debit_amount
            print("Debit of $", debit_amount, "has been recorded.")
            with open(transactions_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([debit_amount])

        elif user_choice == "3":
            # Record a credit
            credit_amount = float(input("How much is the credit? "))
            balance += credit_amount
            print("Credit of $", credit_amount, "has been recorded.")
            with open(transactions_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([credit_amount])
            # deposit(transactions_file ,balance, credit_amount)
        else:
            # Exit the program
            exit()
            break
if __name__ == "__main__":
    main()
