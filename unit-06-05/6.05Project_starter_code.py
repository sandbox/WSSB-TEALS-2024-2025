import random

# Dictionary of characters and character traits
CHARACTERS = {
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

HELP_TEXT = '''
- list: list out all the character's names
- gender/age/height/job: asks for a piece of information
- guess name: guess a character
- help: displays all commands
- quit: exits the game
'''

# list of traits to choose from
LIST_OF_TRAIT_LABELS = ["gender", "age", "height", "job"]

# choose a random character
random_character = ''
# setup hints
hints = 0

def action_list():
    pass
# test statement
# action_list()

def action_trait():
    pass
# test statement
# action_trait("age")

def action_guess():
    pass
# test statement
# action_guess()

# gameplay loop
playing = True
while playing:
    action = input("What would you like to do? ")
    if action == "list":
        action_list()
    elif action in LIST_OF_TRAIT_LABELS:
        action_trait(action)
    elif action == "guess":
        action_guess()
    elif action == "help":
        print(HELP_TEXT)
    elif action == "quit":
        playing = False
    else:
        print("Not a valid command, try again.")
