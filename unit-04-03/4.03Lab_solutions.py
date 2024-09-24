# 4.03 Lab Solutions

# Part 1
# Write a function, draw_7, to draw the 7×7 square (shown below)

# def draw_7():
#     for i in range(0, 7):
#         my_string = ''
#         for j in range(0, 7):
#             my_string += ' *'
#         print(my_string)

# draw_7()

# alternate

# def print_7_stars():
#     my_string = ''
#     for i in range(0, 7):
#         my_string += ' *'
#     print(my_string)   

# def print_star_square():
#     for i in range(0, 7):
#         print_7_stars()

# print_star_square()

# Part 2
# Write a function stars_and_stripes, that will draw a 3 sets of rows. 
# 1st a row of 7 stars followed by a row of 7 dashes (shown below)

# def stars_and_stripes():
#     for i in range(0, 6):
#         my_string = ''
#         for j in range(0, 7):
#             if i%2 == 0:
#                 my_string += ' *'
#             else:
#                 my_string += ' -'
#         print(my_string)

# stars_and_stripes()

# Part 3
# Write a function, increasing_triangle that will print out the following:

# def increasing_triangle():
#     my_string = ''
#     for j in range(1, 8):
#         my_string += str(j) + ' '
#         print(my_string)

# increasing_triangle()

# Part 4
# Write a function, vertical_stars_and_stripes that will print out the following:

# def stars_and_stripes():
#     for i in range(0, 7):
#         my_string = ''
#         for j in range(0, 7):
#             if j%2 == 0:
#                 my_string += ' -'
#             else:
#                 my_string += ' *'
#         print(my_string)

# stars_and_stripes()

# Part 5: Bonus
# Use a function to create your own pattern or drawing. 
# Some possible pattern ideas:

# 5.1 Write a function that will print a border around a 7×7 square (shown below)

# def draw_7_border():
#     for i in range(0, 7):
#         my_string = ''
#         for j in range(0, 7):
#             if i == 0 or i == 6:
#                 my_string += ' *'
#             else:
#                 if j == 0 or j == 6:
#                     my_string += ' *'
#                 else:
#                     my_string += ' -'
#         print(my_string)

# draw_7_border()

# 5.2 Write a function that will print the following balanced_triangle.

# def balanced_triangle():
#     my_string = ''
#     for i in range(1, 8):
#         my_string += str(i) + ' '
#         print(my_string)
#     for j in range(7, 1, -1):
#         my_string = ''
#         for k in range(1, j):
#             my_string += str(k) + ' '
#         print(my_string)

# balanced_triangle()

# 5.3 Write a function that will print the following triangle.

# def star_triangle():
#     my_string = ''
#     for j in range(1, 6, 2):
#         my_string = str('*' * j)
#         print(my_string.center(5))

# star_triangle()

# 5.4 Draw a pattern using user input

# my_number = int(input("How many stars would you like? "))
# my_shape1 = input("What first shape would you like? ")
# my_shape2 = input("What second shape would you like? ")
# my_pattern = input("What pattern would you like (stripes, alternate, border)? ")

# def stripes(number, shape1, shape2):
#     for i in range(0, number):
#         my_string = ''
#         for j in range(0, number):
#             if i%2 == 0:
#                 my_string += ' ' + shape1
#             else:
#                 my_string += ' ' + shape2
#         print(my_string)

# def alternate(number, shape1, shape2):
#     for i in range(0, number):
#         my_string = ''
#         for j in range(0, number):
#             if j%2 == 0:
#                 my_string += ' ' + shape1
#             else:
#                 my_string += ' ' + shape2
#         print(my_string)      

# def border(number, shape1, shape2):
#     for i in range(0, number):
#         my_string = ''
#         for j in range(0, number):
#             if i == 0 or i == (number - 1):
#                 my_string += ' ' + shape1
#             else:
#                 if j == 0 or j == (number - 1):
#                     my_string += ' ' + shape1
#                 else:
#                     my_string += ' ' + shape2
#         print(my_string)   

# def custom_pattern(number, shape1, shape2, pattern):
#     if pattern == "stripes":
#         stripes(number, shape1, shape2)
#     elif pattern == "alternate":
#         alternate(number, shape1, shape2)
#     elif pattern == "border":
#         border(number, shape1, shape2)

# custom_pattern(my_number, my_shape1, my_shape2, my_pattern)
