###
##
# Program that creates the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
##
###
row = 9
for i in range(1 , 6):
    print('*' * i)

for i in range (4 , 0 , -1): #-1 so that the loop counts down
    print('*' * i)
