def balance_list():
    balance=[0]
    return balance[-1]



if __name__ == "__main__":
    print("\nWelcome to your terminal checkbook!\n")
    print("1) view current balance\n2) record a debit (withdraw)\n3) record a credit (deposit) \n4) exit") 

    user_input=input("\nWhat would you like to do?")

    if user_input=="1":
        print("view current balance")
        print(balance_list())
        
    elif user_input=="2":
        print("record a debit (withdraw)")
        
    elif user_input=="3":
        input("How much would you like to deposite")
        print("record a credit (deposit)")
        print(balance_list(input)        
    elif user_input=="4":
        print("exit")
        
    else:
        print("Invalid choice")
