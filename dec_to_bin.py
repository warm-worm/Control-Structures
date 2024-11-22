###
##
# Program that converts a decimal number into a binary number
# To convert a decimal number to binary, follow these steps:
# Read a decimal number from the keyboard.
# Divide the number by 2 and note the remainder.
# Divide the quotient obtained by 2 and note the remainder.
# Repeat the same process till we get 0 as the quotient.
# Write the values of all the remainders starting from the bottom 
# to the top. That will be the required binary number.
# Sample result:
# Enter decimal number: 12
# 12(10) = 1100(2)
##
###
dec = int(input('Enter a decimal number: '))
if dec == 0:
    print('0(2)')

else:
    bin = ''
    og_dec = dec
    while dec > 0:
        remainder = dec % 2
        bin = str(remainder) + bin
        dec = dec // 2 # updating the number
    print(f'{og_dec}(10) = {bin}(2)')