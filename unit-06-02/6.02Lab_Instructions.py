# 6.02 Lab Instructions
#
# OVERVIEW
# Write a program that will count how many times a given
# word appears in a paragraph.
#
# Example output:
'''
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? cats
'cats' occurs 3 times
>>> python3 word_frequency_lab.py
What word would you like to know the frequency of? dogs
'dogs' does not occur
'''

# INSTRUCTIONS
# The program will first create a dictionary with the words as keys and the number
# of times they occur as values. Then it will prompt the user which word they
# are curious about. If the word was in the paragraph it will print the number
# of times it occurred.

## STARTER CODE

example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York."

#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()

#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")

#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")
