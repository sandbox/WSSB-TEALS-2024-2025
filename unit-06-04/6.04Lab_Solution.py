example_paragraph = """
I am Sam. I am Sam. Sam-I-am.

That Sam-I-am! That Sam-I-am!
I do not like that Sam-I-am!

Would you like green eggs and ham?

I do not like them, Sam-I-am.
I do not like green eggs and ham.

Would you like them here or there?

I would not like them here or there.
I would not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.

Would you like them in a house?
Would you like them with a mouse?

I do not like them in a house.
I do not like them with a mouse.
I do not like them here or there.
I do not like them anywhere.
I do not like green eggs and ham.
I do not like them, Sam-I-am.
"""

# Name: text_to_word_list
# Purpose: Takes a paragraph of text and turns it into a list of words
# without punctuation or capitalization
# Inputs: paragraph (string)
# Outputs: list of words (list)
def text_to_word_list(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.replace("\n\n", "").replace("\n", " ")
    symbols = ['.', ',', '?', '!']
    for symbol in symbols:
        paragraph = paragraph.replace(symbol, "")
    paragraph_list = paragraph.split(" ")
    return paragraph_list

# Name: count_frequencies
# Purpose: Turns a word list into a dictionary with each unique word
# as a key, and the number of occurrences as values
# Input: A list of words (list)
# Output: A dictionary of words as keys and number of occurrences as values (dictionary)
def count_frequencies(word_list):
    my_dictionary = {}
    for word in word_list:
        if word in my_dictionary:
            my_dictionary[word] += 1
        else:
            my_dictionary[word] = 1
    return my_dictionary

# Name: find_max_value_key
# Purpose: Finds the word in a dictionary with the most occurrences
# Input: A dictionary of words as keys and number of occurrences as values (dictionary)
# Output: The word with the most occurrences (string)
def find_max_value_key(my_dictionary):
    max_count = 0
    max_word = ''
    for key in my_dictionary:
        if my_dictionary[key] > max_count:
            max_count = my_dictionary[key]
            max_word = key
    return max_word

# Name: find_top_word
# Purpose: Prints the word that occurs most in a paragraph
# Inputs: Paragrah (string), optional: dictionary of words and occurrences (dictionary)
# Outputs: The dictionary minus the top occurring word
def find_top_word(paragraph, dictionary_counts = {}):
    word_list = text_to_word_list(paragraph)
    # only create a new dictionary if the current dictionary is empty
    if dictionary_counts == {}:
        dictionary_counts = count_frequencies(word_list)
    top_word = find_max_value_key(dictionary_counts)
    print(top_word)
    # remove top word from dictionary
    dictionary_counts.pop(top_word)
    return dictionary_counts

# find_top_word(example_paragraph)

# Name: find_top_five_words
# Purpose: Prints the top five words that occur most in a paragraph
# by calling "find_top_word" five times
# Inputs: Paragrah (string)
# Outputs: None
def find_top_five_words(paragraph):
    dictionary_counts = {}
    for i in range(0, 5):
        dictionary_counts = find_top_word(paragraph, dictionary_counts)

find_top_five_words(example_paragraph)
