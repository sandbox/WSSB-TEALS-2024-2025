# Complete the below function display_until(). This function accepts
# a single integer parameter and prints out the numbers from 1 to that
# number inclusively. You may assume that the parameter is 1 or
# more.

# Name: display_until
# Purpose: Prints numbers one through n (given number)
# Input: n (integer)
# Output: none (prints numbers)
def display_until(n):
    numbers = ''
    for number in range(1, n+1):
        numbers += str(number) + ' '
    print(numbers)

display_until(10) #prints ‘1 2 3 4 5 6 7 8 9 10’

# Alternate, simpler solution
# Does not print on one line
def display_until_simple(n):
    for number in range(1, n+1):
        print(number)

# display_until_simple(10) #prints ‘1 2 3 4 5 6 7 8 9 10’
