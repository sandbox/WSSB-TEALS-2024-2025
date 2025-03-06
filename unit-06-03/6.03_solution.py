# 6.03 Lab Solution

todos = {
  k:[] for k in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
}

while True:
  action = input("What would you like to do ('add' or 'get')? ")
  if action == 'add':
    day = input("What day would you like to add to? ")
    if day in todos:
      item = input("What would you like to add to " + day + "'s to-do list? ")
      todos[day].append(item)
    else:
      print("'" + day + "' is not a valid day to add to.")
  elif action == 'get':
    day = input("What day? ")
    if day in todos:
      if todos[day]:
        print('You have to do the following:')
        for task in todos[day]:
          print(task)
      else:
        print('You have nothing to do on ' + day)
    else:
      print("'" + day + "' is not a valid day to get from.")
  else:
    print('"' + action + '" is not a valid action, so quitting for now!')
    break
