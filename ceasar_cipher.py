###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    if char.isalpha():
        char_code = ord(char)
    # add one to the character's code
        char_code += 1 
    # replace new character code with its
    # corresponding character (use chr())
        if char.islower():
            if char_code > ord('z'):
                char_code = ord('a')
        elif char.isupper():
            if char_code > ord('Z'):
                char_code = ord('A')
    # add encrypted character to encrypted text
        encrypted_text += chr(char_code)
    else:
        encrypted_text += char
print(plain_text)
print(encrypted_text)