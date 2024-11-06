###
# Checking whether the number
# entered from the keyboard is even or odd 
#
number = float(input('Enter number: '))

if number % 2 == False:
    print(f'{number} is even')
else:
    print(f'{number} is odd')