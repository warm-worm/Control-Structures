#
## Program that prints the name entered from the keyboard, 
## provided it is a female name
#
name = input('Enter the name: ')
last_letter = name[-1]
if last_letter == 'a':
    print(f'{name} -- Polish female name')
else:
    print('Enter a different name.')
