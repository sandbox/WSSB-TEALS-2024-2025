## Shopping Lists
shopping_lists = [
  ['toothpaste', 'q-tips', 'milk'],
  ['milk', 'candy', 'apples'],
  ['planner', 'pencils', 'q-tips']
]

## Part 2

# In this part of the lab you will go through your shopping list program 
# and perform a few different calculations.

# 1. Create a function, all_in_one, that will put all the shopping 
# lists into a single combined list using a for loop.

all_in_one_shopping_list = []

# Name: all_in_one
# Purpose: adds each list item to the "all in one" shopping list
# Input: None
# Output: None (modifies global list "shopping_lists")
def all_in_one():
  for shopping_list in shopping_lists:
    for item in shopping_list:
      all_in_one_shopping_list.append(item)

all_in_one()
print(all_in_one_shopping_list)

# 2. Create a function, count_q_tips, which will go through all items of 
# the list and keep a count of how many times 'q-tips' occurs.

# Name: count_q_tip
# Purpose: Adds to a counter for each occurrence of "q-tips"
# Input: None
# Output: counter (int, total number of occurrences of "q-tips")
def count_q_tips():
  counter = 0
  for shopping_list in shopping_lists:
    for item in shopping_list:
      if item == 'q-tips':
        counter += 1
  return counter

print(count_q_tips())

# 3. In order to make the shopping lists more calcium rich, write a function, 
# drink_more_milk, that adds 'milk' to each of the lists (unless it's 
# already there).

## Discussion question: What is the difference between these two methods?

### Method 1 (uses range and indexes)

# Name: drink_more_milk
# Purpose: Checks if a list includes "milk", if it doesn't, adds it to the list
# Input: None
# Output: None, modifies global list (shopping_lists)
def drink_more_milk():
  for shopping_list_index in range(0, len(shopping_lists)):
    if 'milk' not in shopping_lists[shopping_list_index]:
      print(shopping_lists[shopping_list_index])
      shopping_lists[shopping_list_index].append('milk')

# drink_more_milk()
# print(shopping_lists)

### Method 2 
### Why does this work? Would this work on a list of strings? 
### Lists are mutable
def drink_more_milk():
  for shopping_list in shopping_lists:
    if 'milk' not in shopping_list:
      shopping_list.append('milk')

drink_more_milk()
print(shopping_lists)

# 4. You can't have milk without cookies. Write a function 
# if_you_give_a_moose_a_cookie, that will go through every element of 
# shopping_cart and update 'milk' to be 'milk and cookies'.

## Discussion: Why doesn't this work?

# def if_you_give_a_moose_a_cookie():
#   for shopping_list in shopping_lists:
#     for item in shopping_list:
#       if item == 'milk':
#         item += ' and cookies'

def if_you_give_a_moose_a_cookie():
  for shopping_list in shopping_lists:
    for item_index in range(0, len(shopping_list)):
      if shopping_list[item_index] == 'milk':
        shopping_list[item_index] += ' and cookies'

if_you_give_a_moose_a_cookie()
print(shopping_lists)

## Bonus

# Write a function to reverse the order of the lists, and also reverse 
# the order of the items in each list, in the shopping_cart nested list.

# The new reversed list should look like the following when printed 
# (newlines and spacing added for clarity):

# shopping_cart = [
#   ['q-tips', 'pencils', 'planner'],
#   ['apples', 'candy', 'milk'],
#   ['milk', 'q-tips', 'tooth paste']
# ]

# Tip
# Last item can be gotten by my_list[-1]
# Second to last element: my_list[-2]
# Third to last element: my_list[-3]

reversed_shopping_lists = []
def reverse_shopping():
  for shopping_list_index in range(len(shopping_lists) - 1, -1, -1):
    reversed_shopping_list = []
    for item_index in range(len(shopping_lists[shopping_list_index]) - 1, -1, -1):
      item = shopping_lists[shopping_list_index][item_index]
      reversed_shopping_list.append(item)
    reversed_shopping_lists.append(reversed_shopping_list)

reverse_shopping()
print(reversed_shopping_lists)
