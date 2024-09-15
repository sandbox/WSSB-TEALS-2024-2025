# 1. Run the following code:

for i in range(0, 10):
   print(i)

# In your notebook, write down what the range function does.

# 2. Uncomment and run the following code:

# a_list = ['apple', 'orange', 'pear', 'strawberry', 'grape']
# print(len(a_list))
# print(list(range(0, len(a_list))))

# Write down what range(0, len(a_list)) does.

# 3. Use the range and len functions to make a for loop that 
# prints the elements of a_list, one at a time.

# 4. Find the errors in the following code:

# def is_reverse(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     index1 = 0 # starts from beginning of word
#     index2 = len(word2) # starts from end of word
#     while index2 > 0:
#         if word1[index1] != word2[index2]:
#             return False
#         index1 += 1
#         index2 -= 1
#     return True
# print(is_reverse('pots', 'stop'))
