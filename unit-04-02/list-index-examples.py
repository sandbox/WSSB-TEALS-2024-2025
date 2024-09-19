fruits = ['apple', 'berry', 'cherry', 'yuzu', 'orange']

# Practice: update the second element of our fruits list to be 'berrygood'
fruits[1] += 'good'

# Practice: grab the third element of the fruits list and use slicing
# to print it without it's last letter
word = fruits[2]
print(word[0:-1]) # first to second to last letter

# we can use negative indexing to go backwards through a list
print(word[-1]) # access the last letter
print(word[-2]) # access the second to last letter

# Example:
#
#   When we do a for loop over the elements of a list, we can't update
#   the list we can only use it
for element in fruits:
  print(element)

# if we try to update the element in this for loop, it updates the
# element variable, but it does not update the element inside the
# list. This is a tricky concept!
for element in fruits:
  # We're updating the element variable, but it doesn't change the element inside the list
  element += 's'
  print(element)
print(fruits)

# If we need to update the element of the list inside a for loop, we
# need to do a for loop over the indexes of the list. That uses the
# range and len functions, and then we can use the index to then access
# element in the list at that index, like in the following:
for index in range(0, len(fruits)):
  print(fruits[index]) # we're accessing the element of fruits at `index`
  # Next, we're updating the element of fruits at `index`
  fruits[index] += 's'
