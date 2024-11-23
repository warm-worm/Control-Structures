###
##
# Program that checks if the PIN code entered in the payment terminal 
# is correct. The user has up to three possibilities for entering a PIN 
# code. In case of three unsuccessful attempts, the card is blocked.
# The payment card is secured with a four-digit PIN code (0805) 
# Sample result:
# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.
##
###
PIN = '0805'
times = 0
while times < 3:
    PIN_input = input('Enter the PIN code: ')
    if PIN_input != PIN:
        print('Incorrect...')
        times += 1 # Increases the counter by 1
    elif PIN_input == PIN:
        print('PIN is correct.')
        break
else:
    print('Sorry, your payment card has been blocked.')
