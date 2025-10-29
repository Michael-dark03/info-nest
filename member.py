from typing import List
from book import Book


class Member:
    def __init__(self, member_id: str, name: str, borrowed_books: List[str] | None = None) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books: List[str] = borrowed_books or []  # store book_ids

    def borrow_book(self, book: Book) -> bool:
        if book.available_copies <= 0:
            return False
        if book.book_id in self.borrowed_books:
            return False
        book.update_copies(-1)
        self.borrowed_books.append(book.book_id)
        return True

    def return_book(self, book: Book) -> bool:
        if book.book_id not in self.borrowed_books:
            return False
        book.update_copies(1)
        self.borrowed_books.remove(book.book_id)
        return True

    def display_member_info(self) -> str:
        borrowed = ", ".join(self.borrowed_books) if self.borrowed_books else "None"
        return f"Member ID: {self.member_id} | Name: {self.name} | Borrowed Book IDs: {borrowed}"
