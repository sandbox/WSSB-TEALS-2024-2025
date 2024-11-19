# 4.05 Quiz Review

## for loops using range
### for loop syntax
### Inclusive start, exclusive end to range

## Accessing list items via index
### Comparing list items

## Function arguments
### Relationship between arguments and parameters

## Using variables to build strings, patterns

## Nested for loops using range

## Modulo operator to determine odd/even

## Nested lists and nested for loops
### Finding items with two indexes in a list of lists

# Sample activities

## Example 1: Write a for loop that prints numbers from 1 to 10.
for i in range(1, 11):
    print(i)

## Example 2: Given a list of numbers, write code to 
## find and print the largest number.
nums = [3, 7, 2, 9]

largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)

### Alternate
largest = nums[0]
for index in range(0, len(nums)):
    if nums[index] > largest:
        largest = num
print(largest)

## Example 3: 
## @TODO rework using string for pattern and function
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

## Example 4:
## @TODO function that searches a list for a string and prints the index
