###
##
# Program code prints the computer keyboard
# 7 8 9
# 4 5 6
# 1 2 3
##
###
i = 6
while i >= 0: # continue the loop as long as i >= 0
    j = 1 # start j at 1 for each new row
    while j <= 3:
        print(f'{i+j}',end=' ')
        j += 1
    print() # new line for each loop
    i -= 3 # substracts 3 from i after each row
