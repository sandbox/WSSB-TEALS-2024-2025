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
random_character = random.choice(list(CHARACTERS))
# setup hints
hints = 0

def action_list():
    print("\n")
    for name in CHARACTERS:
        traits = []
        for trait in CHARACTERS[name]:
            traits.append(CHARACTERS[name][trait])
        print(name + ": " + str(traits) + "\n")

def action_trait(trait):
    global hints
    global random_character
    if hints < 2:
        character_trait = CHARACTERS[random_character][action]
        print(character_trait)
        hints += 1
    else:
        print("You've used all your hints!")

def action_guess():
    global hints
    global random_character
    user_guess = input("What character would you like to guess? ")
    if user_guess == random_character:
        print("You guessed right!")
    else:
        print("You guessed wrong.")
    print("The correct answer was " + random_character + ".")
    print("Try a new character or type 'quit'")
    random_character = random.choice(list(CHARACTERS))
    hints = 0

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
