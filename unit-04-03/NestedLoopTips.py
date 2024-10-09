# Part 3
# Write a function, increasing_triangle that will print out the following:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7

# strategies:
## Determine the largest repeating unit (row_number)
### This is the outer loop
## Determine the smallest repeating unit (number)
### This is the inner loop
## Look at the pattern for repeating numbers compared to the row number
### Key observation: The number of numbers in each row is equal to the row number.
### The inner loop generates the numbers for each row. For the first row, 
### you print one number, for the second row two numbers, and so on.
## For each row row_number, print numbers from 1 to row_number.
## Determine when to print (after each row)
## Determine when to reset the string (at the beginning of each row)
## Wiggle the numbers on range to start from "row_number" = 1

def increasing_triangle():
  for row_number in range(1, 8): # number of rows
    my_string = ''
    for number in range(1, row_number + 1): # numbers
      my_string += str(number) + ' '
    print(my_string)

increasing_triangle()

# Part 4:
# Write a function, vertical_stars_and_stripes that will print out the following:
#     - * - * - * -
#     - * - * - * -
#     - * - * - * -
#     - * - * - * -
#     - * - * - * -
#     - * - * - * -
#     - * - * - * -

# Strategies
## Determine the largest repeating unit (row_number), repeats 7 times
### for row_number in range(0, 7)
## Determine the smallest repeating unit (symbol), repeats 7 times
### for symbol_number in range(0, 7)
## Look at the pattern for repeating numbers compared to the 
## row number or symbol_number
### Key observation: The dashes appear on symbol_numbers 1, 3, 5, and 7 (odd symbol_numbers)
### The stars appear on symbol_numbers 2, 4, and 6 (even symbol_numbers)
## Determine when the string needs to be reset (beginning of each row)
## Determine when the string needs to be printed (after each row)
def vertical_stars_and_stripes():
  for row_number in range(0, 7):
    string = ''
    for symbol_number in range(0, 7):
      if symbol_number == 1 or symbol_number == 3 or symbol_number == 5 or symbol_number == 7:
        string += '* '
      else:
        string += '- '
    print(string)

vertical_stars_and_stripes()