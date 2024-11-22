###
##
# Program that prints a survey consisting of three questions. 
# Save the answers to logical type variables. Then view the survey result. 
# Sample result:
# SURVEY Are you interested in computer science? (y/n): y
# Do you like playing computer games? (y/n): n
# Do you have an Instagram account? (y/n): y
#
# SURVEY RESULTS Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes
##
###
print('SURVEY:')
comp_sci = input('Are you interested in computer science? (y/n): ')
comp_games = input('Do you like playing computer games? (y/n): ')
instagram = input('Do you have an Instagram account? (y/n): ')
print('SURVEY RESULTS:')
if comp_sci == 'y':
    print('Interested in computer science: Yes')
elif comp_sci == 'n':
    print('Interested in computer science: No')
else:
    print('Incorrect input, try again.')

if comp_games == 'y':
    print('Playing computer games: Yes')
elif comp_games == 'n':
    print('Playing computer games: No')
else:
    print('Incorrect input, try again.')

if instagram == 'y':
    print('Has Instagram account: Yes')
elif instagram == 'n':
    print('Has Instagram account: No')
else:
    print('Incorrect input, try again.')
