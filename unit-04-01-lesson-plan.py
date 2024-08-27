# Unit 4 - Lesson 1
#
# Day 1
#
# After this lesson, you will be able to...
#   Define and identify for loop, item, iteration, scope
#   Loop through (traverse) the items in a list
#   Introduce and compare "for" and "while" loops in Python
#
# Type the following (copy the following)
#
# Leading Questions
#   What do the brackets mean? What data type does the brackets create?
#   What data type is the value in single quotes?
#   What does append do?
#   What does the plus mean?
#   What do we think the code will do before running it?
#
# Run the code and talk about what happened
single_fruit = ['apple', 'banana', 'watermelon', 'grape']
multi_fruit = []
multi_fruit.append(single_fruit[0] + 's')
multi_fruit.append(single_fruit[1] + 's')
multi_fruit.append(single_fruit[2] + 's')
multi_fruit.append(single_fruit[3] + 's')
print(multi_fruit)

#
#   What would happen if you added 100 items to the list single_fruit?
#   Write down how you would update multi_fruit, following this template code.
#
# Does that feel like a lot of work to add 100 items? Do you think there is a better way?
#
# Day 2
# - Recap Day 1
#
# Now let's try the following
list_of_numbers = [3, 5, 10, 23]
for num in list_of_numbers:
  print("num is " + str(num))

# What happened here?
# How would the code change if you added 100 items to list_of_numbers?
# Can you think about how to rewrite the code with the fruits using what you learned from the list_of_numbers example.

# Let's rewrite the code with the fruits
single_fruit = ['apple', 'banana', 'watermelon', 'grape']
multi_fruit = []
for fruit in single_fruit:
  multi_fruit.append(fruit + 's')
print(multi_fruit)

# Review Discussion
#   With the fruits list originally, what would happen if the list got much larger?
#     Have to write a lot of code! how tedious
#
#   With the numbers list, what would happen if the list got much larger?
#     We used a for loop, and don't have to write anymore code if the list gets larger. So fun

# Day 3
# - Recap Day 2
#
# Formal Definition Time
#
#   A loop is a sequence of instructions that is continually repeated until a certain condition is reached.
#
#   Each repetition is called an iteration.
#
# Examples
#   Search a list of students for the ones with names beginning with ‘R’
#   Find all the prime numbers from 1 to 100
#   Repeatedly execute user commands until a game is over
#

# The for loop
#   Slide 10
list_of_numbers = [3, 5, 10, 23]
for num in list_of_numbers: # condition
   print("num is " + str(num)) # body - indented underneath the for condition

# for item in list: (what I want to do something on)
#   I want to do this (body)
#
# num is called the variable
#   it represents an individual item in the list we are looping over
#
# What happens on each iteration?
# iteration 1, variable num, value 3
# iteration 2, variable num, value 5
# iteration 3, variable num, value 10
# iteration 4, variable num, value 23

# Full Class Example
#
# Make a list of animals
# Find the animal in your list that starts with your favorite letter
# PRint the animal you found

animals = ['cat', 'dog', 'tiger', 'elephant']
for animal in animals:
  if animal[0] == 'd':
    print('This animal starts with my favorite letter: ' + animal)

# The while loop
#   Slide 11
while playing == True: # condition
  # body - indented underneath the while condition
  action = input("Choose an action, {0} -->".format(player_name))
  if action == "travel" or action == "t":
    handle_travel()
  elif action == "rest" or action == "r":
    handle_rest()
  elif action == "hunt" or action == "h":
    handle_hunt()

# Questions: When do you think you'd use a while loop instead of a for loop?
#
# While loops are useful when you don't know when the condition is
#   going to end. They can sometimes be dangerous, because it's
#   possible to loop forever (this is called an infinite loop) and
#   then the program might never end. Your computer might get stuck!
#
# For loops are useful when we know the end condition of the loop
#   Like when we know the list we are looping over (so we know the list has an end)
#   Of if we know we want to loop from 1 to 10, we know the ending point of the loop
#

# For loop works over characters in a string too. A string is like a list of characters


# Lab Activity
#
# Create a de_vowel function.
#    Input is a string
#    Output is a copy of the string
#
# The copy should have the vowels removed
# 'a', 'e', 'i', 'o', and 'u' are counted as vowels, but not 'y'.
#
# Create the function contract for de_vowel.
#
# Write de_vowel using a for loop
#
# Provide a few examples that confirm de_vowel works as expected:
#   What if the string is all vowels?
#   What if there are no vowels?
#   What if there is a mix of vowels and non-vowels and spaces?
#   What if some of the vowel characters are capitalized?
#
# Starter Code

# contract goes here
def de_vowel(a_string):
# your code goes here
no_vowels = de_vowel("This sentence has no vowels")
print(no_vowels)
# examples go here


# BONUS Activity
# Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create a function count_vowels.
# count_vowels takes in a string and returns an int representing the number of vowels in the string.

def count_vowels(a_string):
  # code for bonus goes here

7_vowels = count_vowels("This sentence has 7 vowels")
print(7_vowels)


# Reflection
# Write in your notebook how you could use a for loop in a computer program
