# 4.05 Quiz Review

##
## For loops using range
## 

for number in range(0, 10):
  print(number)

# notes: first parameter of range is inclusive, second is exclusive
# ex: for loop is initializing a local variable `index`
# `index` changes each iteration of the loop, incrementing across the range

##
## Accessing list items via index
##

fruits = ['apple', 'orange', 'grape', 'banana']
print(fruits[2]) # prints `grape`

# notes: index is "address" of the list item
# Lists are zero-indexed
# Use brackets to refer to a list item at certain index

##
## Setting list items via index
##

fruits = ['apple', 'orange', 'grape', 'banana']
fruits[2] = 'strawberry'
print(fruits) # prints `['apple', 'orange', 'strawberry', 'banana']

# notes: use list and index (with brackets) on the left side of a 
# variable assignment to update a list item to a new value

## 
## For loops using range and index
##

fruits = ['apple', 'orange', 'grape', 'banana']
for index in range(0, len(fruits)):
  print(fruits[index])

# notes: if iterating through a list, range starts at the first list index (0)
# Range ends at the last list index
# Can be calculated by using the length of the list (len)
# No need to zero-index the len because second parameter of range is exclusive
# Has the effect of iterating across each list item when using list and index

# ex2: Updating list items using range and index
fruits = ['apple', 'orange', 'grape', 'banana']
for index in range(0, len(fruits)):
  fruits[index] += ' (limited edition!)'
print(fruits)

# notes: Can use list and index on the left side to update each item in a list

##
## Comparing list items
##

# Assume fruits_1 and fruits_2 are the same length
fruits_1 = ['apple', 'orange', 'grape', 'banana']
fruits_2 = ['peach', 'orange', 'strawberry', 'banana']
for index in range(0, len(fruits_1)):
  if fruits_1[index] == fruits_2[index]:
    print(str(index) + ' is a match!')

# notes: use == for comparison, = for variables
# When on the first iteration of the loop, index is 0
# When index is 0, fruits_1[index] and fruits_2[index] are the first
# items in each list
# When index is 1, fruits_1[index] and fruits_1[index] is the second 
# item, etc.

##
## Function arguments
##
### Relationship between arguments and parameters

##
## Using variables to build strings, patterns
##
my_numbers = ''
for number in range(0, 10):
  my_numbers += number
print(my_numbers) # prints `0 1 2 3 4 5 6 7 8 9`

## Nested for loops using range
for row in range(0, 4):
    string = ''
    for column in range(0, 8):
      string += '* '
    print(string)

## Modulo operator to determine odd/even
for row in range(0, 4):
    string = ''
    for column in range(0, 8):
        if column%2 == 0:
            string += '# '
        else:
            string += '= '
    print(string)

## Nested lists and nested for loops
### Finding items with two indexes in a list of lists


## Example 4:
## @TODO function that searches a list for a string and prints the index
