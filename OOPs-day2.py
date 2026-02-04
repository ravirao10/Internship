# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Book Title :", self.title)
        print("Author     :", self.author)


# Child class (Single Inheritance)
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        # Call parent class constructor
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        # Call parent method
        self.display_book_details()
        print("Issued To  :", self.issued_to)
        print("Issued Date:", self.issued_date)


# Creating object of IssuedBook
issued_book = IssuedBook(
    title="Python Programming",
    author="Alice",
    issued_to="Thamson",
    issued_date="01-Feb-2026"
)

# Display all details
issued_book.display_issued_book_details()
