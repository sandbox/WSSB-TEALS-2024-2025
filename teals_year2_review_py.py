# CS Year 2: Beginning of Year Review

##
## Vocabulary
##
'''
  - Python
    - A high-level general-purpose text-based programming language.
  - Programming language
  - Bugs/Debugging
  - Console
  - Output
  - Print
  - Value
    - A single piece of data in Python (e.g. 2, “Hello, World”).
  - Variable
    - A name that refers to a value.
  - Type
    - A classification for data which tells Python how it will be used.  
  - Operators 
    - Symbols that represent computations (e.g. +, -, /, *).
  - Expressions 
    - A combination of values, variables, and operators. (e.g. 2+3).
  - Statement 
    - A unit of code that Python can execute.
'''

##
## Comments
##
'''
### Discussion Questions:
  - What does it mean when Python "executes" a line of code?
  - What are some good uses for comments?
'''
# This is a comment 

##
## Data types
##
'''
### Types
  - Integer
    - A type containing a whole number  …, -2, -1, 0, 1, 2, …
  - String
    - A type containing a series of characters. Usually written using quotes (e.g. “Hello, World”).
    - Use '+' operator to concatonate strings
  - Float
    - A type containing a decimal value. (1.1, 2.0, 0.5)
  - Boolean
    - True or False
  - (List, covered later)
'''
type(3) # int
type(3.0) # float
type("three") # str
type('3') # str
type(True) # bool
print("Hello " + "World.") # "Hello World."

##
## Variables
##
animal = "dog"
print(animal) # "dog"

##
## Inputs
##
### Data given to the application by the user.
animal = input("What is your favorite animal?")

##
## Casting
##
number_integer = int('3')
number_string = str(3)
number = int(input("What is your favorite number?"))

##
## Booleans
##
5 > 3  # True
10 < 2 # False
3 == 3 # True
### example 1.0
animal = "dog"
animal == "dog"  # True
animal != "cat"  # True

## 
## AND/OR/NOT operators
##
### example 1.1
animal == "dog" or animal == "cat" # True
animal == "dog" and animal = "cat" # False


##
## Conditionals
##
### ex 1.2
if animal == "dog":
  print("Woof!")
elif animal == "cat":
  print("Meow!")
else:
  print("Please pick another animal!")
#### Result: prints "Woof!"

##
## Lists
##
### example 2.0
animals = ["dog", "cat", "fish", "parrot"]
# index
print(animals[0]) # 'dog'
animals[1] = "reptile" # assigns new value to the second list item 
print(animals) # ["dog", "reptile", "fish", "parrot"]
print(animals[-1]) # 'parrot'
# slice
print(animals[0:2]) # ["dog", "cat"]
# append
animals.append("cow")
print(animals) # ["dog", "cat", "fish", "parrot", "cow"]
# pop
last_animal = animals.pop()
print(last_animal) # 'cow'
print(animals) # ["dog", "cat", "fish", "parrot"]
# remove
animals.remove("dog")
print(animals) # ["cat", "fish", "parrot"]
# concatonate
animals = ["cat", "fish"] + ["dog"]
print(animals) # ["cat", "fish", "dog"]

##
## Loops
##
### A repeated operation while a specified condition is met.
### ex 3.0
playing = True
while playing == True: # or while playing:
  action = input("What's your next move?")
  print(action)

### ex 4.0, using loop counter
counter = 0
while counter <= 5:
  print(counter)
  counter = counter + 1 # or counter += 1
#### Result: prints 012345

##
## Functions
## 
'''
### Vocabulary
  - Function
    - A block of organized, reusable code that is used to perform a single, related action.
  - Arguments
    - A value that is passed between programs, subroutines or functions.
  - Calling functions
    - Telling the computer to run (or execute) that set of actions.
  - Return vs. print
  - Function contract
    # Name:
    # Purpose:
    # Arguments:
    # Returns:
  - Built-in vs. user-defined
    - Ex: random library's random.randint, print
'''
### ex 5.0
import random
print(random.randint(1, 5))
#### Result: prints random integer between 1 and 5 (inclusive)

### ex 6.0, custom function
# Name: my_function
# Purpose: prints "THIS IS MY FUNCTION!"
# Arguments: none
# Returns: none
def my_function():
  print("THIS IS MY FUNCTION!")
my_funtion()
### Result: prints THIS IS MY FUNCTION!

### ex 7.0
# Name: greeting
# Purpose: Prints a customized greeting for a specified name
# Arguments: name (str)
# Returns: none
def greeting(name):
  print("Hi " + name + "!")
greeting("Taylor")
### Result: prints Hi Taylor!

### ex 7.0
# Name: name_generator
# Purpose: Combines first_name and last_name and returns the resulting string
# Arguments: first_name (str), last_name (str)
# Returns: full name (str)
def name_generator(first_name, last_name):
  return (first_name + last_name)
full_name = name_generator("Taylor", "Swift")
print(full_name)
### Result: prints Taylor Swift