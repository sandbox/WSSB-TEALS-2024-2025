##
## Activity 1.0, Lucky Number
##

### Part 1: Casting and inputs
'''
Print the user's lucky number. Ask the user for their favorite 
number and their birth month. Their lucky number is their 
favorite number multiplied by their birth month.
'''
favorite_number = input("What is your favorite number? ")
birth_month = input("What is your birth month? ")
lucky_number = int(favorite_number) * int(birth_month)
print("Your lucky number is " + str(lucky_number))

### Part 2: if/else statements and comparator operators
'''
Check if the user's birth month is between 1 and 12.
If the birth month is outside that range, tell the user
that's not a valid month. Otherwise print their lucky number.
'''
favorite_number = input("What is your favorite number? ")
birth_month = input("What is your birth month? ")
birth_month_int = int(birth_month)
if birth_month_int > 12 or birth_month_int < 1:
  print("That's not a month!")
else:
  lucky_number = int(favorite_number) * int(birth_month)
  print("Your lucky number is " + str(lucky_number))



##
## Activity 2.0
##

### Part 1: Functions
'''
Create a function that generates an e-mail address based on 
a first and last name. The e-mail address should be the
last name plus the first initial of the first name plus "@wssb.edu".
The function should return the full email address. Generate and print
e-mail addresses for several names. Don't forget to write the 
function contract!
'''

# Name: generate_email
# Purpose: Prints a customized greeting for a specified name
# Arguments: name (str)
# Returns: email address (str)
def generate_email(first_name, last_name):
  email = last_name + first_name[0] + '@wssb.edu'
  email = email.lower() # optional
  return email

print(generate_email("James", "Taylor"))
print(generate_email("Taylor", "Swift"))

### Part 2: Functions
'''
Create a collection of e-mail addresses by adding each one to a list.
Print the final e-mail list.
'''
def generate_email(first_name, last_name):
  email = last_name + first_name[0] + '@wssb.edu'
  email = email.lower() # optional
  return email

email_list = []
email_list.append(generate_email("James", "Taylor"))
email_list.append(generate_email("Taylor", "Swift"))
print(email_list)

##
## Bonus Activity 3.0
##

### Part 1: Lists and append
'''
Create a an empty packing list. Write a while loop that keeps 
asking the user for items to add to the packing list until 
they type "q" to quit. Then print the completed packing list.
'''
packing_list = []
packing = True
while packing:
  item = input('What do you need to add to your suitcase? (Type "q" to quit) ')

  if item == 'q':
    packing = False
  else:
    packing_list.append(item)
    print(packing_list)
print("You're all packed!")
print(packing_list)