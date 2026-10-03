# ATM Terminal Simulator

account_balance = 10000.0
correct_pin = 1234

print("===== WELCOME TO PYTHON BANK ATM =====")

entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin == correct_pin:
    print("\nAuthentication successful!\n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Cash")
    
    choice = int(input("\nSelect an option (1-3): "))
    
    if choice == 1:
        print("Your current balance is: Rs.", account_balance)
        
    elif choice == 2:
        deposit_amount = float(input("Enter amount to deposit: Rs. "))
        if deposit_amount > 0:
            account_balance = account_balance + deposit_amount
            print("Deposit successful! Updated balance: Rs.", account_balance)
        else:
            print("Invalid deposit amount.")
            
    elif choice == 3:
        withdraw_amount = float(input("Enter amount to withdraw: Rs. "))
        if withdraw_amount > account_balance:
            print("Transaction declined: Insufficient funds.")
        elif withdraw_amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            account_balance = account_balance - withdraw_amount
            print("Withdrawal successful! Remaining balance: Rs.", account_balance)
    else:
        print("Invalid option selected.")
else:
    print("\nIncorrect PIN. Access Denied.")