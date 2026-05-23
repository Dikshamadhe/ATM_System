#Atm System project-2

# ---------------- ATM SYSTEM ---------------- #
balance = 20000
PIN = 1234
history = []

# PIN check
user_pin = int(input("Enter Your PIN : "))
print("Your PIN Is : ", user_pin)

if  user_pin != PIN :
    print("Sorry! Your PIN Is Wrong")
else:
    while True: 
        print("\n 1. check Balance")
        print(" 2. Deposit")
        print(" 3. Withdraw")
        print(" 4. Transaction History")
        print(" 5. Change PIN")
        print(" 6. Exit")

        choice = int(input("Enter Your Choice: "))

        # -------- CHECK BALANCE -------- #
        if choice ==1 :
            print("Balance", balance)

        # -------- DEPOSIT -------- #
        elif choice ==2:
            amount = int(input("Enter Your Amount : "))
            balance += amount
            history.append(f"Deposited : {amount}")
            print("Deposit Successfully ! ")

        # -------- WITHDRAW -------- #
        elif choice ==3:
            withdraw = int(input("Enter Your Amount :"))
            if withdraw <= balance:
               balance -=withdraw
               history.append(f"Withdrawn : {withdraw}")
               print("Withdraw Successfully ")
            else:
                print("Sorry ! Insufficient Balance")

         # -------- HISTORY -------- #
        elif choice ==4:
            print("\nTransaction History: ")
            if len(history) == 0:
                print(" No Transactions ")
            else:
                for h in history:
                 print("-" ,h)

        # -------- CHANGE PIN -------- #
        elif choice ==5:
            old_pin =int (input("Enter Your Old PIN : "))
            if old_pin != PIN :
                print("Old PIN Is Wrong")
            else:
                PIN= int (input("Enter Your New PIN: "))
                print ("PIN Changed Successfully ")

        # -------- EXIT -------- #
        elif choice ==6:
            print("THANK YOU ! ")
            break
        else:
            print("Invalid Choice")
          
