# 4.03 Lab Caesar Cipher Instructions

# In this lab we will be implementing a Caesar Cipher

# The Caesar cipher is one if the simplest and most straightforward
# ways to obfuscate text. The way it works is that the alphabet is
# printed on a wheel, in order, and you step through the text letter
# by letter by first rotating the wheel to the original letter and
# then rotating right a certain number of letters. To decipher the
# text, you rotate the wheel to the ciphered letter and then rotate
# left that same number of letters. Because of the rotation of the
# wheel, Caesar ciphers are commonly abbreviated 'rot' and then the
# number of spaces to rotate, e.g. 'rot13'. An example of rot13 in
# action is below:

# Input: Hello world
# Output: Uryyb jbeyq
#
# The rot13 mapping looks like this:
#
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# NOPQRSTUVWXYZABCDEFGHIJKLM

# Meaning, A becomes N, B becomes O, ..., Y becomes L, Z becomes M.

# For this assignment, you will write a single function, cipher. This
# function will take a single letter and return the letter 13 steps to
# the right. A letter_to_number() function is provided which converts
# letters to their numerical position in the alphabet.

# Name: letter_to_number
# Purpose: Convert a letter in the alphabet to its corresponding location in the alphabet.
# Parameters: The letter to convert, as a string.
# Returns: An integer representing the position, zero-indexed, of the letter in the alphabet, or None if it's not a letter.
def letter_to_number(letter):
    letter = letter.lower()
    if letter in 'abcdefghijklmnopqrstuvwxyz':
        return ord(letter) - ord('a')
    return None

# function contract goes here
def cipher(letter):
    # function body goes here

# Examples
print(cipher('a'))
print(cipher(cipher('a')))
print(cipher('x'))
print(cipher(cipher('x')))
# add more examples here


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
