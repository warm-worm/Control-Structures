#
## Program that asks for the number of hours of parking, 
# then calculates and prints the correct fee
# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
#
hours = int(input('How many hours do you want to be parked? '))
if hours <= 0:
    print('Incorrect number, try again.')
elif hours <= 2:
    print('Your fee is 5 PLN.')
elif hours <= 6:
    print('Your fee is 15 PLN.')
elif hours > 6:
    print('Your fee is 20 PLN.')
