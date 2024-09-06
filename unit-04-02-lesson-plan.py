# Unit 4 Lesson 2 Plan
#
# Day 1
#
# After this lesson, you will be able to...
#   Define and identify for loop, item, iteration, scope
#   Loop through (traverse) the items in a list
#   Be aware of the scope of variables during iteration 
#
# Type the following (copy the following)
# Then run the code and talk about what happened
for i in range(0, 10): 
  print(i)

# What does the range function do? Write it down
#   Range goes from the first number to the last number, but doesn't include the last number
# What happens if the range is 5, 100?
# What is the last number that gets printed?

  
# Next example, Part 2
a_list = ['apple', 'orange', 'pear', 'strawberry', 'grape']
print(len(a_list))
print(list(range(0, len(a_list)))

# What does the `len` function do?
# How might you use `len`?

# Part 3: Lets try using the range() and len() functions to make a for loop that prints the elements of a_list, one at a time.
# Answer:
for i in range(0, len(a_list)):
  print(a_list[i])  
