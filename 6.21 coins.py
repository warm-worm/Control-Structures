###
##
# There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
# Write a program showing any amount (natural number) read from the 
# keyboard with as few coins as possible.
# Enter the amount in PLN: 18
# The amount of PLN 18 in coins:
# 5 PLN coins: 3
# 2 PLN coins: 1
# 1 PLN coins: 1
##
###
amount = int(input('Enter the amount in PLN: '))
if amount % 5 >= 0:
    dividant = amount // 5
    print(f'5 PLN coins: {dividant}')
    amount %= 5

if amount % 2 >= 0:
    dividant = amount // 2
    print(f'2 PLN coins: {dividant}')
    amount %= 2

if amount > 0:
    dividant = amount
    print(f'1 PLN coins: {dividant}')
