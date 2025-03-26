import random

# Dictionary of characters and character traits
characters = {
    "taylor": {
        "gender": "female",
        "age": "35",
        "height": "5'10",
        "job": "music"
    },
    "demi": {
        "gender": "non-binary",
        "age": "35",
        "height": "5'0",
        "job": "music"
    },
    "simone": {
        "gender": "female",
        "age": "28",
        "height": "5'0",
        "job": "sports"
    },
    "lebron": {
        "gender": "male",
        "age": "40",
        "height": "6'9",
        "job": "sports"
    },
    "pedro": {
        "gender": "male",
        "age": "49",
        "height": "5'10",
        "job": "TV/Movies"
    },
    "zendaya": {
        "gender": "female",
        "age": "28",
        "height": "5'10",
        "job": "TV/Movies"
    },
}

# help text
help_text = '''
- list: list out all the character's names
- gender/age/height/job: asks for a piece of information
- guess name: guess a character
- help: displays all commands
- quit: exits the game
'''

# list of traits to choose from
list_of_trait_labels = ["gender", "age", "height", "job"]

# choose a random character

# setup hints

# gameplay loop
playing = True
while playing:
    action = input("What would you like to do? ")
    if action == "help":
        print(help_text)
    elif action == "quit":
        playing = False
    else:
        print("Not a valid command, try again.")
