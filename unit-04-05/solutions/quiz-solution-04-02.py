# Complete the below function compare_lists(). This function accepts
# two parameters that are both lists of integers. You may assume the
# lists are the same length. Print out the larger of the two values at
# each index in the lists.

# Name: compare_lists
# Purpose: Compare numbers from two lists, print the higher number in each set
# Input: n1 (list of numbers), n2 (list of numbers)
# Output: None (prints higher number in each set)
def compare_lists(n1, n2):
    for index in range(0, len(n1)):
        if n1[index] > n2[index]:
            print(n1[index])
        else:
            print(n2[index])

example1 = [0, -4, 10, 5]
example2 = [5, 3, 2, 5]
compare_lists(example1, example2)  #prints 5, 3, 10, 5
