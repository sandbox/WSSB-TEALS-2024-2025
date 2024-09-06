# Unit 4 Lesson 2 Plan
#
# Day 1
#
# After this lesson, you will be able to...
#   Define and identify for loop, item, iteration, scope
#   Loop through (traverse) the items in a list
#   Be aware of the scope of variables during iteration 
#
# Type the following (copy the following)
# Then run the code and talk about what happened
for i in range(0, 10): 
  print(i)

# What does the range function do? Write it down
#   Range goes from the first number to the last number, but doesn't include the last number
# What happens if the range is 5, 100?
# What is the last number that gets printed?
# 
# Note that range can also take in a third value that is optional.
#   the third value indicates the step size to take
for i in range(0, 10, 2):
  print(i)
  
# Next example, Part 2
a_list = ['apple', 'orange', 'pear', 'strawberry', 'grape']
print(len(a_list))
print(list(range(0, len(a_list)))

# What does the `len` function do?
# How might you use `len`?
# How might the values in the second print be helpful?
# Answer: They are a list of the indices!
#   You can use these values to access the index of a list

# Part 3: Lets try using the range() and len() functions to make a for loop that prints the elements of a_list, one at a time.
# Answer:
for i in range(0, len(a_list)):
  print(a_list[i])  


# Most common way to traverse the elements of a list is with a for loop. 
# To write or update the elements, use indices. 
# A common way to do that is to combine the functions range() and len():
#
# Example
numbers = [1,2,3,4]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

# What did this code do to numbers?

# Debugging
#
# It's tricky to get the beginning and end of the traversal right. 
# On the following page is a function that is supposed to compare two words and return True if one of the words is the reverse of the other.
# The code will contain two common errors.
#
# This looks very tricky to explain
#
# In the sample “Function Contains Two Errors” code, we expect the return value True, but we get an IndexError instead.
# Suggest printing the values of the indices immediately before the line where the error appears (right after while statement).
# First error: the index of the last character is 3, so the initial value for j should be different: j = len(word2)-1.
# Second error: we need to include the character at index 0, so we need to change the while condition: while j >= 0:
def is_reverse(word1, word2):
  if len(word1) != len(word2):
    return False
  i = 0
  j = len(word2)
  while j > 0:
    if word1[i] != word2[j]:
      return False
    i = i + 1
    j = j - 1
return True
print(is_reverse('pots', 'stop'))


# Lab fruit_pluralizer
#

# Lab Reverse String 
#
'''
Create a function my_reverse, which will return a reversed string.

Create the function contract for my_reverse.
Provide a few examples to confirm that my_reverse works:
An empty string
A string of even length
A string of odd length greater than 1
A string of length 1
'''
# contract goes here
def my_reverse(string_to_reverse):
    # your code goes here

reversed = my_reverse("apples")
print(reversed)
# examples go here
