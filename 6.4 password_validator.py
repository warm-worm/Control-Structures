###
# Password validator
# New password is at least 12 characters long
#
new_password = input('Enter new password: ')
if len(new_password) < 12:
   print('Password too short (min. 12 chars)') 
else:
   repeat = input('Please repeat the password: ')
if repeat == new_password:
    print('The password has been set!')
else:
    print('Incorrect password, try again.')