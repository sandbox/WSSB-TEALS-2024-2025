# Type and run the following code

# my_building is a representation of the apartments on 
# each floor of my 3 story building

my_building = [
  ['apt1a', 'apt1b', 'apt1c'],
  ['apt2a', 'apt2b', 'apt2c'],
  ['apt3a', 'apt3b', 'apt3c']
]
print("first floor: " + str(my_building[0]))
print("first floor, 3rd apartment: " + str(my_building[0][2]))

# Write down what was printed.

# first floor: ['apt1a', 'apt1b', 'apt1c']
# first floor, 3rd apartment: apt1c

# How you would access the 2nd apartment of the 3rd floor (apt3b)?

print("third floor, 2nd apartment: " + str(my_building[2][1]))

## Part 2

# Print all the apartments one at a time

all_apts = []

for floor in my_building:
  for apartment in floor:
    print(apartment)

print(all_apts)

# How would you show all apartments in a single list?

all_apts = []

for floor in my_building:
  for apartment in floor:
    all_apts.append(apartment)

print(all_apts)

# Change all "d" apartments to say "suite"

for floor in my_building:
  floor[-1] = 'suite'

print(my_building)

# Print all the apartments that don't end in 'a'?

for floor in my_building:
  for apartment in floor:
    if apartment[-1] != 'a':
      print(apartment)

print(my_building)      

# Add "(newly renovated!)" to all apartment names

for floor in my_building:
  for apartment_number in range(0, len(floor)):
    floor[apartment_number] += ' (Newly Renovated!)'

print(my_building)

# Bonus: print a "d" apartment to each list using the same naming convention

for floor_number in range(0, len(my_building)):
  floor = my_building[floor_number]
  my_building[floor_number].append('apt' + str(floor_number + 1) + 'd')

print(my_building)
