###
##
# Program that finds N leading prime numbers
# Read the value of N from the keyboard
# Using loop statements check that the number N is divisible only by 1 
# and by N
# A natural number greater than 1 is called a prime if it has exactly 2 
# natural factors with the values 1 and this number
# Prime numbers: 2 3 5 7 11 ...
##
###
N = int(input('Enter a number of leading prime numbers to find: '))
count = 0
checking_from = 2
while count < N:
    is_prime = True
    for i in range(2 , checking_from): # is num divisible by any number from 2 to num-1
        if checking_from % i == 0: # if its divisible by i its not prime
            is_prime = False
            break
    if is_prime: # then print and increase the count
        print(checking_from , end=" ")
        count +=1
    checking_from += 1 # moving onto the next number