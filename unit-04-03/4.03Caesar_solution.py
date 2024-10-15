# 4.03 Lab Caesar Cipher Instructions

# Teaching Guide:
# Understanding letter to number conversion
# Adding 13 to mimc rotation on the wheel
# Using mod arithmetic with 26 to mimic going around the wheel and starting over
# Accessing the letter from a list
# Ignoring symbols that are not in our letter list

# Name: letter_to_number
# Purpose: Convert a letter in the alphabet to its corresponding location in the alphabet.
# Parameters: The letter to convert, as a string.
# Returns: An integer representing the position, zero-indexed, of the letter in the alphabet, or None if it's not a letter.
def letter_to_number(letter):
    letter = letter.lower()
    if letter in 'abcdefghijklmnopqrstuvwxyz':
        return ord(letter) - ord('a')
    return None

# Name: cipher
# Purpose: Convert a letter in the alphabet to its corresponding rot13 ciphered letter (a -> n, etc)
# Parameters: The letter to convert, as a string.
# Returns: An converted letter, as a stringg.
def cipher(letter):
    letter_number = letter_to_number(letter)
    if letter_number is None:
      return letter
    cipher_number = letter_number + 13
    cipher_number = cipher_number % 26
    return 'abcdefghijklmnopqrstuvwxyz'[cipher_number]

# Examples
print(cipher('a'))
print(cipher(cipher('a'))) # should print a since running the cipher twice brings you back to where you started
print(cipher('x'))
print(cipher(cipher('x')))

# Name: cipher_text
# Purpose: Converts a whole string of text through the rot13 Caesar Cipher
# Parameters: The text to convert, as a string.
# Returns: Converted text, as a string.
def cipher_text(text):
    return ''.join([cipher(c) for c in text])

text = [
    'Mary had a little lamb',
    'How much wood would a woodchuck chuck if a chuck-wood could chuck wood?',
    'This is the song that never ends, it goes on and on, my friends...',
    'I want to be the very best, like no one ever was. To catch them is my real test, to train them is my cause.',
]

# Use the cipher_text function to convert and print the full list of
# text. Hint: you'll need a for loop
# code goes here
for t in text:
  print(cipher_text(t))
  print(cipher_text(cipher_text(t)))
