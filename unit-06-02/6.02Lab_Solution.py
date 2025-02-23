example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York."

#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()

#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")

#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")

my_dictionary = {}
for example_word in example_word_list:
    if example_word in my_dictionary:
        my_dictionary[example_word] += 1
    else:
        my_dictionary[example_word] = 1

while True:
    word = input("What word would you like to know the frequency of? ")
    if word in my_dictionary:
        print("'" + word + "' appears " + str(my_dictionary[word]) + " times.")
    else:
        print("Sorry, '" + word + "' is not in the paragraph.")
