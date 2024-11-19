###
# The timer.py program takes a number from the user and counts down to zero. 
# Modify the program so that the last five seconds of the counter are printed 
# in words, i.e. five, four, three, two, one.
##
import time
def num_to_words(n):
    words = ['five', 'four', 'three', 'two', 'one']
    if 1 <= n <= 5:
        return words[5-n]
    return str(n)
number = int(input('Enter the number of seconds to count down: '))
while number > 0:
    if number <= 5:
        print(num_to_words(number))
    else:
        print(number)
    number -=1
    time.sleep(1) #Waits for one second

print('Time is up!')