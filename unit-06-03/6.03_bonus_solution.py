# 6.03 Lab Solution

todos = {
  k:[] for k in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
}

while True:
  command = input("What would you like to do (format: action day item)? ")
  action, extra = command.split(' ', 1)
  if action == 'add':
    day, item = extra.split(' ', 1)
    if day in todos:
      todos[day].append(item)
    else:
      print("'" + day + "' is not a valid day to add to.")
  elif action == 'get':
    day = extra
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
