#=======================================

# project: Library Management System
# Author: Muhammad Ahtsham Javed
# Language: Python
# version: 1.0

#=======================================

separator = "=" * 35


class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__total_copies = total_copies
        self.__borrowed_copies = 0
        self.__available_copies = total_copies

    def borrow(self):
        if self.__available_copies > 0:
            self.__borrowed_copies += 1
            self.__available_copies -= 1
            return True
        return False

    def return_copy(self):
        if self.__borrowed_copies > 0:
            self.__borrowed_copies -= 1
            self.__available_copies += 1
            return True
        return False

    def display_info(self):
        print(f"\tID: {self.book_id}")
        print(f"\tTitle: {self.title}")
        print(f"\tAuthor: {self.author}")
        print(f"\tTotal Copies: {self.__total_copies}")
        print(f"\tBorrowed Copies: {self.__borrowed_copies}")
        print(f"\tAvailable Copies: {self.__available_copies}")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        book_id = input("Enter book ID: ").strip()
        if not book_id:
            print("Book ID cannot be empty.")
            return
        if book_id in self.books:
            print("Book ID already exists.")
            return

        title = input("Enter book title: ").strip()
        if not title:
            print("Book title cannot be empty.")
            return

        author = input("Enter book author: ").strip()
        if not author:
            print("Book author cannot be empty.")
            return

        try:
            total_copies = int(input("Enter total copies: ").strip())
        except ValueError:
            print("Total copies must be a number.")
            return
        if total_copies <= 0:
            print("Total copies must be a positive number.")
            return

        self.books[book_id] = Book(book_id, title, author, total_copies)
        print(f"Book '{self.books[book_id].title}' added successfully.")

    def borrow_book(self):
        book_id = input("Enter book ID to borrow: ").strip()
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
            return

        if book.borrow():
            print(f"Book '{book.title}' borrowed successfully.")
        else:
            print("No copies available to borrow.")

    def return_book(self):
        book_id = input("Enter book ID to return: ").strip()
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
            return

        if book.return_copy():
            print(f"Book '{book.title}' returned successfully.")
        else:
            print("No borrowed copies to return.")
            
    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for index, book in enumerate(self.books.values(), start=1):
            print(f"Book {index}:")
            book.display_info()
            print(separator)

    def display_book_info(self):
        book_id = input("Enter book ID to display: ").strip()
        book = self.books.get(book_id)
        if not book:
            print("Book not found.")
            return
        print(f"Book Information for ID {book_id}:")
        book.display_info()
        print(separator)


def display_menu():
    print(separator)
    print("     Library Management System     ")
    print(separator)
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Book Information")
    print("5. Display All Books")
    print("6. Exit")
    return input("Enter your choice (1-6): ").strip()

def main():
    library = Library()
    while True:
        choice = display_menu()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.borrow_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            library.display_book_info()
        elif choice == "5":
            library.display_all_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()