###
# ATM (cash machine) simulator
#
import math
balance = 1000  # Initial balance
pin = 1111 # initial 4-digit PIN code
check_pin = input('Input the PIN: ')
if check_pin.isdigit() and len(check_pin) == 4:
    check_pin = int(check_pin)
    while check_pin == pin or check_pin == new_pin:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print('4. Change the PIN')
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        print()

        if choice == '1':
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            new_pin = int(input("Enter the new PIN: "))
            confirm_pin = int(input('Please confirm the new PIN: '))
            if new_pin == confirm_pin:
                print(f'The new PIN ({new_pin}) has been set!')
                check_pin = int(input('Enter the new PIN to continue: '))
                pin == new_pin
                if check_pin == new_pin: 
                    continue
                else:
                    print('Incorrect PIN, try again.')
            else:
                print("The PIN's don't match, try again.")
        
        elif choice == '5':
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")
    else:
        print('Incorrect PIN, try again.')
else:
    print('The PIN number consists of 4 numbers, try again.')