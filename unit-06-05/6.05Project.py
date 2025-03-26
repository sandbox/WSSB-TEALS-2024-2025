import random

# Dictionary of characters and character traits
characters = {
    "taylor": {
        "pronouns": "she/her",
        "age": "35",
        "height": "5'10",
        "job": "music"
    },
    "demi": {
        "pronouns": "they/them",
        "age": "35",
        "height": "5'0",
        "job": "music"
    },
    "simone": {
        "pronouns": "she/her",
        "age": "28",
        "height": "5'0",
        "job": "sports"
    },
    "lebron": {
        "pronouns": "he/him",
        "age": "40",
        "height": "6'9",
        "job": "sports"
    },
    "pedro": {
        "pronouns": "he/him",
        "age": "49",
        "height": "5'10",
        "job": "TV/Movies"
    },
    "zendaya": {
        "pronouns": "she/her",
        "age": "28",
        "height": "5'10",
        "job": "TV/Movies"
    },
}

help_text = '''
- list: list out all the character's names
- pronouns/age/height/job: asks for a piece of information
- guess name: guess a character
- help: displays all commands
- quit: exits the game
'''

# list of traits to choose from
list_of_trait_labels = ["pronouns", "age", "height", "job"]

# choose a random character
random_character = random.choice(list(characters))
# setup hints
hints = 0

# gameplay loop
playing = True
while playing:
    action = input("What would you like to do? ")
    if action == "list":
        print("\n")
        for name in characters:
            traits = []
            for trait in characters[name]:
                traits.append(characters[name][trait])
            print(name + ": " + str(traits) + "\n")
    elif action in list_of_trait_labels:
        if hints < 2:
            trait = characters[random_character][action]
            print(trait)
            hints += 1
        else:
            print("You've used all your hints!")
    elif action == "guess":
        user_guess = input("What character would you like to guess? ")
        if user_guess == random_character:
            print("You guessed right!")
        else:
            print("You guessed wrong.")
        print("The correct answer was " + random_character + ".")
        print("Try a new character or type 'quit'")
        random_character = random.choice(list(characters))
        hints = 0
    elif action == "help":
        print(help_text)
    elif action == "quit":
        playing = False
    else:
        print("Not a valid command, try again.")
