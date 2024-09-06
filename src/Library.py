from typing import List, Tuple, Optional
from src.Book import Book
from src.User import User


class Library:
    def __init__(self) -> None:
        self.__books: List[Book] = []
        self.__users: List[User] = []
        self.__checked_out_books: List[Tuple[str, str, str]] = []
        self.__checked_in_books: List[str] = []

    # Getters
    def get_books(self) -> List[Book]:
        return self.__books

    def get_users(self) -> List[User]:
        return self.__users

    def get_checked_out_books(self) -> List[Tuple[str, str, str]]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> List[str]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        self.__books.append(Book(isbn, title, author))

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_author()}")

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: str, due_date: str) -> None:
        # Search for the book by ISBN
        book_to_checkout: Optional[Book] = None
        for book in self.__books:
            if book.get_isbn() == isbn:
                book_to_checkout = book
                break

        user_to_checkout: Optional[User] = None
        for user in self.__users:
            if user.get_dni() == dni:
                user_to_checkout = user
                break

        if not user_to_checkout or not book_to_checkout:
            print(f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}")
            return

        book_to_checkout.set_available(False)
        book_to_checkout.increment_checkout_num()
        user_to_checkout.increment_checkouts()
        self.__checked_out_books.append((isbn, dni, due_date))

        print(f"User {dni} checked out book {isbn}")

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: str) -> Optional[str]:

        book_to_check_in: Optional[Book] = None
        for book in self.__books:
            if book.get_isbn() == isbn:
                book_to_check_in = book
                break

        if not book_to_check_in:
            return f"Book {isbn} is not available."

        if book_to_check_in.is_available():
            return f"Book {isbn} is not checked out."

        book_to_check_in.set_available(True)

        for user in self.__users:
            if user.get_dni() == dni:
                user.increment_checkins()
                break

        return None

    # Utils
    def add_user(self, dni: str, name: str) -> None:
        self.__users.append(User(dni, name))
