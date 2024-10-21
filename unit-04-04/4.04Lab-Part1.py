shopping_lists = [
  ['toothpaste', 'q-tips', 'milk'],
  ['milk', 'candy', 'apples'],
  ['planner', 'pencils', 'q-tips']
]

# Name: update_list
# Purpose: Changes a specific item in a specific list, prints the updated list
# Inputs: 
## list to update (int, not zero-indexed)
## item to update (int not zero-indexed)
## updated item (str)
# Output: None
def update_list(list_choice, item_choice, update_choice):
  shopping_lists[list_choice - 1][item_choice - 1] = update_choice
  shopping_list = shopping_lists[list_choice - 1]
  for item in shopping_list:
    print(item)

# Name: print_item
# Purpose: Prints a specific item in a specific list
# Inputs: 
## list to choose (int, not zero-indexed)
## item to update (int, not zero-indexed)
# Output: None
def print_item(list_choice, item_choice):
  shopping_item = shopping_lists[list_choice - 1][item_choice - 1]
  print(shopping_item)

# Name: print_list
# Purpose: Prints all items in specific list
# Inputs: 
## list to view (int, not zero-indexed)
# Output: None
def print_list(list_choice):
  shopping_list = shopping_lists[list_choice - 1]
  for item in shopping_list:
    print(item)

shopping = True
while shopping:
  choice = int(input("Choose 1 = update item, 2 = view item, or 3 = view list: "))

  if choice == 1:
    list_choice = int(input("Which shopping list do you want to update? "))
    item_choice = int(input("Which item on list #" + str(list_choice) + " do you want to change? "))
    update_choice = input("New value for item #" + str(item_choice) + "? ")
    update_list(list_choice, item_choice, update_choice)
  if choice == 2:
    list_choice = int(input("Which shopping list do you want to choose? "))
    item_choice = int(input("Which item on list #" + str(list_choice) + " do you want to see? "))
    print_item(list_choice, item_choice)
  if choice == 3:
    list_choice = int(input("Which shopping list would you like to see? "))
    print_list(list_choice)
