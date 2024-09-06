from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []

    # Getters
    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_checked_out_books(self):
        return self.__checked_out_books

    def get_checked_in_books(self):
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author):
        self.__books.append(Book(isbn, title, author))

    # 1.2 List All Books
    def list_all_books(self):
        for book in self.__books:
            print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_author()}")

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date):
        # Search for the book by ISBN
        book_to_checkout = None
        for book in self.__books:
            if book.get_isbn() == isbn:
                book_to_checkout = book
                break

        user_to_checkout = None
        for user in self.__users:
            if user.get_dni() == dni:
                user_to_checkout = user
                break

        if not user_to_checkout or not book_to_checkout:
            print(f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}")

        book_to_checkout.set_available(False)
        book_to_checkout.increment_checkout_num()
        user_to_checkout.increment_checkouts()
        self.__checked_out_books.append((isbn, dni, due_date))

        print(f"User {dni} checked out book {isbn}")

    # 2.2 Check in book
    def check_in_book(self, isbn, dni):

        book_to_check_in = None
        for book in self.__books:
            if book.get_isbn() == isbn:
                book_to_check_in = book
                break

        if not book_to_check_in:
            return f"Book {isbn} is not available."

        if book_to_check_in.is_available():
            return f"Book {isbn} is not available."

        book_to_check_in.set_available(True)

        for user in self.__users:
            if user.get_dni() == dni:
                user.increment_checkins()
                break

    # Utils
    def add_user(self, dni, name):
        self.__users.append(User(dni, name))
