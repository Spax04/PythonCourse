# You have been assigned a task to create a program for managing a library catalog. Your program should allow users to perform various operations such as adding books, searching for books, borrowing books, and returning books. Additionally, the program should keep track of the availability of each book and display the borrowed books.
#
# Here are the steps to follow:
#
# 1.	Create an empty dictionary called library_catalog to store the books. The keys of the dictionary will be the book titles, and the values will be dictionaries representing each book with keys 'author' and 'available'.
# 2.	Use a while loop to repeat the following operations until the user chooses to exit:
# •	Display a menu of options to the user:
# o	Add book
# o	Search book
# o	Borrow book
# o	Return book
# o	Display borrowed books
# o	Exit
# •	Ask the user to select an option by entering the corresponding number.
# •	Based on the user's choice, perform the corresponding operation.
# •	Display the result to the user.
#
# For each option:
#
# 1.	Add Book:
#
# •	Ask the user to enter the book title, author, and the number of available copies.
# •	Create a dictionary representing the book with keys 'author' and 'available'.
# •	Add the book to the library_catalog dictionary with the book title as the key and the book dictionary as the value.
# •	If the book already exists in the catalog, update the number of available copies.
#
# 2.	Search Book:
#
# •	Ask the user to enter a search term (either title or author).
# •	Iterate over the keys and values of the library_catalog dictionary and check if the search term matches the title or author of any book.
# •	If a match is found, display the book details including the author and the number of available copies.
# •	If no match is found, display a message indicating that the book is not available.
#
# 3.	Borrow Book:
#
# •	Ask the user to enter the title of the book to borrow.
# •	If the book exists in the library_catalog dictionary and is available, decrease the number of available copies by 1.
# •	If the book is not available or doesn't exist, display a message indicating that the book cannot be borrowed.
# 4.	Return Book:
#
# •	Ask the user to enter the title of the book to return.
# •	If the book exists in the library_catalog dictionary, increase the number of available copies by 1.
# •	If the book doesn't exist, display a message indicating that the book cannot be returned.
# •	Display Borrowed Books:
# •	Iterate over the keys and values of the library_catalog dictionary and display the details of the borrowed books, including the title, author, and the number of available copies (which should be less than the total copies).


library_catalog = {}

while True:
    print("\nMenu:")
    print("1. Add book")
    print("2. Search book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Display borrowed books")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 6:

    # Your code here

    if choice == 1:

    # Your code here

    elif choice == 2:

    # Your code here

    elif choice == 3:

    # Your code here

    elif choice == 4:

    # Your code here

    elif choice == 5:

# Your code here

