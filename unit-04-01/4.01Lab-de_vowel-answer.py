# Lab Activity
#
# Create a de_vowel function.
#    Input is a string
#    Output is a copy of the string
#
# The copy should have the vowels removed
# 'a', 'e', 'i', 'o', and 'u' are counted as vowels, but not 'y'.
#
# Create the function contract for de_vowel.
#
# Write de_vowel using a for loop
#
# Provide a few examples that confirm de_vowel works as expected:
#   What if the string is all vowels?
#   What if there are no vowels?
#   What if there is a mix of vowels and non-vowels and spaces?
#   What if some of the vowel characters are capitalized?
#
# Starter Code

# Name de_vowel
# Purpose remove all occurences of vowels aeiou from a string
# Input a string
# Output a string with all vowels removed
def de_vowel(a_string):
  ans = ''
  for c in a_string:
    if c.lower() not in 'aeiou':
      ans += c
  return ans

# longer example
def de_vowel(a_string):
  ans = ''
  for x in a_string:
    c = x.lower()
    if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u':
      ans += x
  return ans

# your code goes here
no_vowels = de_vowel("This sentence has no vowels")
print(no_vowels)
# examples go here
print(de_vowel('aeuio'))
print(de_vowel('CCCCCCC'))
print(de_vowel(''))
print(de_vowel('no vowels'))
print(de_vowel('Capitalized VOWeLS'))
