## Part 1

# Teaching Guide
# 1 Students should write the function contract
# 2 Students should try to plan what they will do to
# 3 Students should make a for loop going over the indexes of the word_list
# 4 Students can edit an item in the list in the for loop (adding the s)
# 5 Students can use a variable inside the for loop to make it easier to use the current word
# 6 Students can use negative indexing to access the last letter of the word
# 7 Students can use an if statement to check if the last letter of a word is y
# 8 Students can use slicing to copy a word, up to and excluding the last letter

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

# Example bonus: Asking for singular fruits by input, adding them to the list and then pluralizing
# Example bonus: Pluralizing ch words to 'es'
def pluralize_words(word_list):
  for i in range(0, len(word_list)):
    word = word_list[i]
    if word[-1] == 'y':
      word_list[i] = word[0:-1] + 'ies'
    elif word[-2:] == 'ch':
      word_list[i] = word + 'es'
    else:
      word_list[i] = word + 's'

number_of_fruits = int(input('How many fruits would you like to add?'))
fruits = []
for i in range(number_of_fruits):
  fruits.append(input("Add fruit #{}: ".format(i+1)))

print("Singular fruits: " + str(fruits))
pluralize_words(fruits)
print("Plural fruits: " + str(fruits))

## Part 2

# Teaching Guide
# 1 Students should write the function contract
# 2 Students should try to plan what they will do to
# 3 Students should create a result variable as an empty string that they are going to build up
# 4 Students should make a for loop going over the indexes of the string to reverse
# 5 Students can use negative indexing to grab the from the end of the string_to_reverse
# 6 Students can use math to grab the appropriate negative index in the string_to_reverse
# 7 Students can add to the reverse string
# 8 Students return the resulting reversed_string

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
