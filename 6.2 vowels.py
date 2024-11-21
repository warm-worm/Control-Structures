###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
char = 0

# Count vowels in the text
while char < len(text): #ensures the loop runs for each character in the string
    if text[char] in vowels: #checks if the character at index char is a vowel
        vowel_count += 1
    char += 1 #increments char to move to the next character in the text

print(f"The number of vowels in the text is: {vowel_count}")
