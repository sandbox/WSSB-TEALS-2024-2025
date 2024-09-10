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

# contract goes here
def de_vowel(a_string):
  ans = ''
  for c in a_string:
    if c not in ['a','e','i','o','u']:
      ans += c
  return ans

# your code goes here
no_vowels = de_vowel("This sentence has no vowels")
print(no_vowels)
# examples go here
