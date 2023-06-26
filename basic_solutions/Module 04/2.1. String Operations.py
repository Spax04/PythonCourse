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
        break

    elif choice == 1:
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        available = int(input("Enter the number of available copies: "))

        if title in library_catalog:
            library_catalog[title]['available'] += available
        else:
            library_catalog[title] = {'author': author, 'available': available}

        print(f"{title} by {author} added to the catalog.")

    elif choice == 2:
        search_term = input("Enter the search term (title or author): ")

        found_books = []
        for title, book in library_catalog.items():
            if search_term.lower() in title.lower() or search_term.lower() in book['author'].lower():
                found_books.append((title, book['author'], book['available']))

        if found_books:
            print("Search Results:")
            for book in found_books:
                print(f"Title: {book[0]}, Author: {book[1]}, Available: {book[2]}")
        else:
            print("No matching books found.")

    elif choice == 3:
        title = input("Enter the title of the book to borrow: ")

        if title in library_catalog:
            if library_catalog[title]['available'] > 0:
                library_catalog[title]['available'] -= 1
                print(f"You have borrowed {title}. Enjoy your reading!")
            else:
                print(f"Sorry, {title} is currently unavailable.")
        else:
            print(f"{title} is not available in the catalog.")

    elif choice == 4:
        title = input("Enter the title of the book to return: ")

        if title in library_catalog:
            library_catalog[title]['available'] += 1
            print(f"You have returned {title}. Thank you!")
        else:
            print(f"{title} is not found in the catalog.")

    elif choice == 5:
        borrowed_books = []
        for title, book in library_catalog.items():
            if book['available'] < 1:
                borrowed_books.append((title, book['author'], book['available']))

        if borrowed_books:
            print("Borrowed Books:")
            for book in borrowed_books:
                print(f"Title: {book[0]}, Author: {book[1]}, Available: {book[2]}")
        else:
            print("No books are currently borrowed.")

print("Thank you for using the Library Catalog. Goodbye!")