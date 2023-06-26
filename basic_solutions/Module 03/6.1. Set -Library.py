# In this exercise, we will work with set operations to create a program that manages a library's book borrowing system. We will use sets to store the book titles that are currently borrowed by library patrons.
#
# Your task is to write the code that allows the librarian to perform the following operations on the book borrowing system:
# •	Add a book to the system as being borrowed by a patron.
# •	Display all books currently borrowed.
# •	Check if a book is currently borrowed.
# •	Remove a book from the system once it is returned by the patron.
#
# Once you have completed the code, test it by performing the specified operations on the book borrowing system.

# Initialize an empty set for the borrowed books
borrowed_books = set()

# Add books to the borrowing system

borrowed_books.add("Book 1")
borrowed_books.add("Book 2")
borrowed_books.add("Book 3")

# Display all books currently borrowed

print("Books Currently Borrowed:")
for book in borrowed_books:
    print(book)



# Check if a book is currently borrowed

book_to_check = "Book 2"
if book_to_check in borrowed_books:
    print(f"The book '{book_to_check}' is currently borrowed.")
else:
    print(f"The book '{book_to_check}' is not currently borrowed.")


# Remove a book from the system once it is returned

book_to_return = "Book 1"
borrowed_books.remove(book_to_return)
print(f"The book '{book_to_return}' has been returned and removed from the borrowing system.")


# Display the updated borrowing system

print("Updated Borrowing System:")
for book in borrowed_books:
    print(book)
