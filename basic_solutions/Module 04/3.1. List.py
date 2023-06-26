# You have been hired as a data analyst at a company that specializes in analyzing social media data. Your task is to write a Python program that performs various operations on a list of tweets. The program should allow you to filter and analyze the tweets based on certain criteria. Your task is to implement the following features:
#
# 1.	Create an empty list to store the tweets.
# 2.	Use a while loop to keep the program running until the user chooses to quit.
# 3.	Display the menu options to the user: "Add tweet", "Filter tweets", "Analyze tweets", and "Quit".
# 4.	Use if-else statements to execute the corresponding operation based on the user's choice.
# 5.	For the "Add tweet" option, prompt the user to enter a tweet and add it to the list.
# 6.	For the "Filter tweets" option, prompt the user to enter a keyword and display only the tweets that contain that keyword.
# 7.	For the "Analyze tweets" option, calculate and display the average length of the tweets in the list.
# 8.	If the user enters an invalid choice, display an error message.
# Remember to use list operations and methods, while and for loops, if and else operators, and functions to implement this program.

def display_menu():
    print("Menu Options:")
    print("1. Add tweet")
    print("2. Filter tweets")
    print("3. Analyze tweets")
    print("4. Quit")

def add_tweet(tweets):
    tweet = input("Enter a tweet: ")
    tweets.append(tweet)
    print("Tweet added.")

def filter_tweets(tweets):
    keyword = input("Enter a keyword to filter tweets: ")
    filtered_tweets = [tweet for tweet in tweets if keyword.lower() in tweet.lower()]
    if filtered_tweets:
        print("Filtered tweets:")
    for tweet in filtered_tweets:
        print(tweet)
    else:
        print("No tweets found with the given keyword.")

def analyze_tweets(tweets):
    total_length = sum(len(tweet) for tweet in tweets)
    if len(tweets) > 0:
        average_length = total_length / len(tweets)
        print(f"Average tweet length: {average_length:.2f}")
    else:
        print("No tweets available for analysis.")

tweets = []
choice = 0

while choice != 4:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_tweet(tweets)
    elif choice == 2:
        filter_tweets(tweets)
    elif choice == 3:
        analyze_tweets(tweets)
    elif choice == 4:
        print("Thank you for using the tweet analysis program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
print("Program exited.")