# Do Now 4.05 Quiz Practice

## Example 1: Write a function that prints numbers from 1 to 10.
## Bonus: Make the numbers all appear on a single line
def one_to_ten():
  string = ''
  for number in range(1, 11):
    string += str(number)
  print(string)

one_to_ten()

## Example 2: Given a list of numbers, write a script to find 
## and print the largest number.
nums = [3, 7, 2, 9]
largest = nums[0]
for number in nums:
  if number > largest:
    largest = number
print(largest)

## Example 3: Write a function that prints a 6x6 square of alternating rows
## of stars and dashes
def stars_and_stripes():
  for i in range(0, 6):
    my_string = ''
    for j in range(0, 6):
      if i%2 == 0:
        my_string += ' *'
      else:
        my_string += ' -'
    print(my_string)

stars_and_stripes()

## Example 4: Write a function that takes a string as an argument and 
## searches a list for that string. The function should print the index
## of the found item
words = ['banana', 'apple', 'orange', 'grapes', 'yuzu']

def find_string(word):
  for index in range(0, len(words)):
    if words[index] == word:
      print(index)

find_string('grapes')
