# You are working on a data analysis project that involves processing a large dataset containing information about different books in a library. Your task is to create a class that represents an iterator for this dataset. The iterator should allow you to iterate over the books based on specific criteria, such as filtering books by genre or sorting them by publication year.
#
# To accomplish this, you need to implement a class called BookIterator with the following specifications:
#
# 1.	The class should have a constructor that takes a list of books as a parameter and initializes an instance variable to store the books.
# 2.	The class should have a method called __iter__() that returns the iterator object itself.
# 3.	The class should have a method called __next__() that retrieves the next book in each iteration based on the specified criteria. If there are no more books, it should raise the StopIteration exception.
# 4.	The class should have methods to set the criteria for filtering and sorting the books. These methods should allow the user to dynamically change the criteria during iteration.
#
# Your task is to complete the implementation of the BookIterator class according to the given specifications. Once you have implemented the class, create an instance of it with a sample list of books, set different criteria for filtering and sorting, and iterate over the books, printing their titles.

class BookIterator:
    def __init__(self, books):
        self.books = books
        self.current_index = 0
        self.filter_criteria = None
        self.sort_criteria = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.books):
            raise StopIteration

        book = self.books[self.current_index]
        self.current_index += 1

        if self.filter_criteria and not self.filter_criteria(book):
            return self.__next__()

        return book

    def filter_books(self):
        def filter_criteria(book):
            return book["genre"] == "Programming"

        self.set_filter_criteria(filter_criteria)

    def sort_books(self, books):
        def sort_criteria(book):
            return book["year"]

        self.set_sort_criteria(sort_criteria)

    def set_filter_criteria(self, criteria):
        self.filter_criteria = criteria

    def set_sort_criteria(self, criteria):
        self.sort_criteria = criteria
        self.books.sort(key=criteria)


# Sample list of books
books = [
    {"title": "Python Crash Course", "author": "Eric Matthes", "genre": "Programming", "year": 2015},
    {"title": "Clean Code", "author": "Robert C. Martin", "genre": "Programming", "year": 2008},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt, David Thomas", "genre": "Programming", "year": 1999},
    {"title": "Design Patterns", "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
     "genre": "Programming", "year": 1994},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "year": 1960},
    {"title": "1984", "author": "George Orwell", "genre": "Fiction", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Fiction", "year": 1813}
]

# Create an instance of BookIterator
book_iterator = BookIterator(books)

# Set filter criteria to only include programming books
book_iterator.filter_books()

# Iterate over the filtered books and print their titles
print("Filtered Books:")
for book in book_iterator:
    print(book["title"])

# Set sort criteria to sort books by publication year
book_iterator.sort_books(books)

# Iterate over all the books sorted by publication year and print their titles
print("\nSorted Books:")
for book in book_iterator:
    print(book["title"])

