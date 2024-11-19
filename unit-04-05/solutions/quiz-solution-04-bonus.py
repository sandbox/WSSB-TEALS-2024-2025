# Complete the below function find_secret(). This function takes a 2D list
# (a list of lists) containing secret words, and a single string. Print the two
# indexes needed to identify where the secret word can be found. Print -1, -1
# if the word cannot be found.

# Name: find_secret
# Purpose: Search a 2D list for a secret word, print the two indexes of that word
#   Prints -1, -1 if the word cannot be found
# Input: secrets (list, 2D list of secret words), word (string, secret word 
#   to search for)
# Output: None (Prints indexes of secret word)
def find_secret(secrets, word):
   for row in range(0, len(secret_words)):
      for column in range(0, len(secrets[row])):
         if secrets[row][column] == word:
            print(str(row) + ', ' +  str(column))
            return None
   print(-1, -1)

# Alternate that doesn't use return None
# def find_secret(secrets, word):
#    indexes = '-1, -1'
#    for row in range(0, len(secret_words)):
#       for column in range(0, len(secrets[row])):
#          if secrets[row][column] == word:
#             indexes = (str(row) + ', ' +  str(column))
#    print(indexes)

# Alternate 2 that is less efficient but may be easier to understand
# def find_secret(secrets, word):
#    indexes = ''
#    for row in range(0, len(secret_words)):
#       for column in range(0, len(secrets[row])):
#          if secrets[row][column] == word:
#             indexes = (str(row) + ', ' +  str(column))
#    if indexes != '':
#       print(indexes)
#    else:
#       print('-1, -1')

secret_words = [
   ['where', 'is', 'the'],
   ['very', 'secret', 'word'],
   ['i', 'can', 'find']
   ]
find_secret(secret_words, 'secret') #prints 1, 1
find_secret(secret_words, 'missing') #prints -1, -1