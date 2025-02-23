phrases = {
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

while True:
    word = input("What word would you like to look up? ")
    if word in phrases:
        print(phrases[word])
    else:
        print("Sorry, '" + word + "' is not defined")
