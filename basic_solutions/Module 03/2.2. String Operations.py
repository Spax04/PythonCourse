# You work at a social media company and have been assigned a task to analyze user comments. Your task is to create a program that takes a user's comment as input and performs the following operations:
#
# 1.	Count the total number of characters in the comment.
# 2.	Count the number of words in the comment.
# 3.	Check if a specific word is present in the comment.
# 4.	Replace a specific word in the comment with another word.
#
# Here are the steps to follow:
#
# 1.	Ask the user to enter a comment.
# 2.	Use a while loop to repeat the following operations until the user chooses to exit:
# •	Display a menu of options to the user:
#   o	Count characters
#   o	Count words
#   o	Check word presence
#   o	Replace word
#   	Exit
# •	Ask the user to select an option by entering the corresponding number.
# •	Based on the user's choice, perform the corresponding operation.
# •	Display the result to the user.

comment = input("Enter your comment: ")

print("\nMenu:")
print("1. Count characters")
print("2. Count words")
print("3. Check word presence")
print("4. Replace word")
print("5. Exit")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    character_count = len(comment)
    print("Total number of characters in the comment:", character_count)

elif choice == 2:
    word_count = len(comment.split())
    print("Total number of words in the comment:", word_count)

elif choice == 3:
    word_to_check = input("Enter the word to check: ")
    if word_to_check.lower() in comment.lower():
        print(f"The word '{word_to_check}' is present in the comment.")
    else:
        print(f"The word '{word_to_check}' is not present in the comment.")

elif choice == 4:
    word_to_replace = input("Enter the word to replace: ")
    replacement_word = input("Enter the replacement word: ")
    comment = comment.replace(word_to_replace, replacement_word)
    print("Comment after word replacement:", comment)

elif choice == 5:
    print("Exiting the program...")
    exit()

else:
    print("Invalid choice. Please try again.")

