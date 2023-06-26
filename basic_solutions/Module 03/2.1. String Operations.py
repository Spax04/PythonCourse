# In this exercise, we will create a program that performs various string operations to analyze a given text. We will use string methods and functions to manipulate the text, count occurrences of specific words, and find the most frequent word in the text.
#
# Your task is to write the code that performs the following string operations:
# 1.	Find the length of the given text.
# 2.	Convert the text to lowercase.
# 3.	Count the number of occurrences of a specific word in the text.
# 4.	Find the most frequent word in the text.
#
# Once you have completed the code, test it by analyzing the provided text.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris euismod gravida libero, in cursus mauris hendrerit sit amet. Integer sit amet volutpat tellus. Nulla facilisi. Donec tristique scelerisque est, non varius nunc ullamcorper ut. Phasellus non elit lorem. Sed suscipit elit vitae pulvinar lobortis. Curabitur quis risus non dolor luctus consectetur eu vitae tellus. Sed bibendum neque ac vestibulum elementum. Phasellus vehicula felis a sem cursus, a congue ligula consectetur. Mauris eu tincidunt magna, a consequat nibh. Nulla feugiat tellus et nisl egestas, a consectetur lacus iaculis. Maecenas nec magna quis risus laoreet mattis sed ut velit. Cras tempor id tellus a aliquet."

# Find the length of the text

length = len(text)
print("Length of the text:", length)


# Convert the text to lowercase

lowercase_text = text.lower()
print("\nLowercase text:\n", lowercase_text)


# Count the occurrences of a specific word

target_word = "consectetur"
occurrences = lowercase_text.count(target_word)
print("\nOccurrences of '", target_word, "' in the text:", occurrences)


# Find the most frequent word in the text

words = lowercase_text.split()
word_count = {}
for word in words:
if word in word_count:
word_count[word] += 1
else:
word_count[word] = 1

most_frequent_word = max(word_count, key=word_count.get)
print("Most frequent word in the text:", most_frequent_word)
