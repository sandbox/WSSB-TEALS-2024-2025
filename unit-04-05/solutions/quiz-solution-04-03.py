# Write a script below that efficiently prints the following pattern.
# Note the space after each symbol.
#
# * - * - * -
# - * - * - *
# * - * - * -
# - * - * - *
# * - * - * -
# - * - * - *

for row in range(0, 6):
    string = ''
    for column in range(0, 6):
        if column%2 == row%2:
            string += '* '
        else:
            string += '- '
    print(string)