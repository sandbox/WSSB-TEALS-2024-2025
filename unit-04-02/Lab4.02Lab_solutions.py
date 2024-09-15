## Part 1

# Name: pluralize_words
# Purpose: Make a singular word plural
# Arguments: List of singular words (strings)
# Returns: None (but changes word_list)
def pluralize_words(word_list):
    for i in range(0, len(word_list)):
        word = word_list[i]
        if word[-1] == 'y':
            word_list[i] = word[0:-1] + 'ies'
        else:
            word_list[i] = word + 's'

word_list = ['apple', 'berry', 'melon']
print("Singular words: " + str(word_list))
pluralize_words(word_list)
print("No longer singular words: " + str(word_list))

## Part 2

# Name: my_reverse
# Purpose: Reverses all the letters in a word
# Arguments: String to be reversed (str)
# Returns: The reversed string (str)
def my_reverse(string_to_reverse):
  reversed_string = ''  
  for i in range(0, len(string_to_reverse)):
    reversed_string += string_to_reverse[-1 - i]
  return reversed_string

reversed = my_reverse("apples")
print(reversed)

## Part 3

def my_reverse_list(word_list_to_reverse):
  for i in range(0, len(word_list_to_reverse)):
    word_list_to_reverse[i] = my_reverse(word_list_to_reverse[i])

word_list = ['apple', 'berry', 'melon']
my_reverse_list(word_list)
print(word_list)
