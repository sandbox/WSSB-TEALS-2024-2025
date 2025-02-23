my_dictionary = {
    'cat': 'a domestic feline',
    'dog': 'a domestic canine',
    'chair': 'furniture piece for sitting',
    'car': 'automobile'
}

print(my_dictionary)

print(my_dictionary['dog'])
print(my_dictionary.get('dog'))

print(type(my_dictionary))
# <class 'dict'>

# What are the keys?
# cat dog chair car
#
# What are the values?
# a domestic feline, etc.

# syntax
# {key : value, key : value, ...}

# print(my_dictionary['Kitten'])
# KeyError: 'kitten'

print(my_dictionary.get('Kitten'))
# None

# Note: You can pass in a second argument to get which takes the place of the None default.

print('cat' in my_dictionary)
# True
print('monkey' in my_dictionary)
# False

# my_dictionary = {'a': 1, 'b': 2, 'c': 3}
if 'a' in my_dictionary:
    print("It's there!")
else:
    print("It's missing!")
