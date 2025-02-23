my_dictionary = {
    'lol': "laugh out loud",
    'rofl': "rolling on the floor laughing",
    'brb': "be right back",
    'btw': "by the way",
    'idk': "I don't know",
    'tldr': "too long, didn't read",
    'lmk': "let me know",
    'dm': "direct message",
    'til': "today I learned"
}

actions = """
    l: look up a word
    u: update/add a word
    d: delete a word
    v: view dictionary
    q: quit
    h: help
"""

print(actions)

playing = True
while playing:
    action = input("What action would you like to take? ")
    if action == 'l':
        word = input("What word would you like to look up? ")
        if word in my_dictionary:
            print(my_dictionary[word])
        else:
            print("Sorry, '" + word + "' is not defined")
    if action == 'u':
        word = input("What word would you like to update? ")
        if word not in my_dictionary:
            print("Sorry, '" + word + "' is not in the dictionary")
            add_word = input("Would you like to add it? ")
            if add_word == 'n' or add_word == 'no':
                continue
        phrase = input("What is the definition of the word? ")
        my_dictionary[word] = phrase
        print(word + ": " + my_dictionary[word])
    if action == 'd':
        word = input("What word would you like to delete? ")
        if word in my_dictionary:
            my_dictionary.pop(word)
            print(word + " has been deleted.")
        else:
            print("Sorry, that word is not in the dictionary.")
    if action == 'v':
        for item in my_dictionary:
            print(item + ": " + my_dictionary[item])
    if action == 'h':
        print(actions)
    if action == 'q':
        playing = False
