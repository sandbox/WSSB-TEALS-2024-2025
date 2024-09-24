# Part 1
# Predict what will happen when you run the following code:

# def print_6_stars():
#     my_string = ''
#     for i in range(0, 6):
#         my_string += ' *'
#     print(my_string)   

# print_6_stars() 

# Run the code, and write down what the output of the 
# function print_6_stars is. 

# * * * * * *

# Part 2
# Write a function print_star_square that calls 
# print_6_stars in a loop to produce the following output.

#    * * * * * *
#    * * * * * *
#    * * * * * *
#    * * * * * *
#    * * * * * *
#    * * * * * *

# Solution:

# def print_star_square():
#     for i in range(0, 6):
#         print_6_stars()

# print_star_square()

# Part 3
# Rewrite the function print_star_square without using print_6_stars.
# Note that there are two ways (at least) to get the above output, 
# so just try doing both!

# Solution 1:

# def print_star_square():
#     for i in range(0, 6):
#         my_string = ''
#         for j in range(0, 6):
#             my_string += ' *'
#         print(my_string)

# print_star_square()

# Solution 2:

# def print_star_square():
#     my_string = ''
#     for i in range(0, 6):
#         if i > 0:
#             my_string += '\n'     
#         for j in range(0, 6):       
#             my_string += ' *'
#     print(my_string)

# print_star_square()
