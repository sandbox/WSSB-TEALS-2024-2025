# 6.03 Lab Instructions
#
# OVERVIEW
# Write a program that will create a week-long to-do list using a Python dictionary
# Each key in the dictionary is a day of the week.
# Each associated value is a list of items to do that day.
#
# Example output:
'''
>>>python3 daily_to_do_list.py
What would you like to do ('add' or 'get')?
add
What day?
Friday
What would you like to add to Friday's to-do list?
practice clarinet
What would you like to do ('add' or 'get')?
get
What day?
Friday
You have to do the following:
practice clarinet
What would you like to do('add' or 'get')?
'''

# INSTRUCTIONS
# The program repeatedly asks the user what action they wish to take (add or get).
#
# If the user enters get, the program asks for a day of the week, and then returns the to-do list for that day.
# If the user enters add, the program asks for a day of the week, then asks for a new item, then adds it to the specified list.
# If a user tries to add an item that already exists on the list for that day, the program rejects the request.
# At the start of the program the dictionary should be totally empty (containing no keys and no values).

## STARTER CODE
