# Complete the below function find_secret(). This function takes a 2D list
# (a list of lists) containing secret words, and a single string. Print the two
# indexes needed to identify where the secret word can be found. Print -1, -1
# if the word cannot be found.

def find_secret(secrets, word):
    # complete this function

secret_words = [
   ['where', 'is', 'the'],
   ['very', 'secret', 'word'],
   ['i', 'can', 'find']
   ]
find_secret(secret_words, ‘secret’) #prints 1, 1
find_secret(secret_words, ‘missing’) #prints -1, -1
