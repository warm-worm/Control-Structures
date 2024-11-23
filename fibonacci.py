###
##
# Program that prints the first twenty words of the Fibonacci sequence
# The first term is equal to 0, the second is equal to 1, each 
# subsequent term is the sum of the previous two
# Sample: 0 1 1 2 3 5 8 13 21 34 ...
##
###
x = 0
y = 1
while True:
    print(x , end=' ') # prints current fibonacci number
    if x > 1000:
        break
    x , y = y , x + y # updates x and y for the next number