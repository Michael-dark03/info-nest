from __future__ import annotations
from typing import List, Optional
from datetime import datetime
import os

from book import Book
from member import Member


BOOKS_FILE = "books.txt"
MEMBERS_FILE = "members.txt"
TRANSACTIONS_FILE = "transactions.txt"


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []
        self.members: List[Member] = []
        self._ensure_data_files()
        self.load_data()

    def _ensure_data_files(self) -> None:
        for filename in (BOOKS_FILE, MEMBERS_FILE, TRANSACTIONS_FILE):
            if not os.path.exists(filename):
                with open(filename, "w", encoding="utf-8"):
                    pass

    def save_data(self) -> None:
        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
            for b in self.books:
                line = f"{b.book_id},{b.title},{b.author},{b.available_copies},{b.borrow_count}\n"
                f.write(line)

        with open(MEMBERS_FILE, "w", encoding="utf-8") as f:
            for m in self.members:
                borrowed = ";".join(m.borrowed_books)
                line = f"{m.member_id},{m.name},{borrowed}\n"
                f.write(line)

    def load_data(self) -> None:
        self.books.clear()
        self.members.clear()
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) < 5:
                        continue
                    book_id, title, author, copies_str, borrow_count_str = parts[0], parts[1], parts[2], parts[3], parts[4]
                    try:
                        copies = int(copies_str)
                        borrow_count = int(borrow_count_str)
                    except ValueError:
                        continue
                    self.books.append(Book(book_id, title, author, copies, borrow_count))

        if os.path.exists(MEMBERS_FILE):
            with open(MEMBERS_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) < 2:
                        continue
                    member_id, name = parts[0], parts[1]
                    borrowed_books = []
                    if len(parts) >= 3 and parts[2]:
                        borrowed_books = parts[2].split(";")
                    self.members.append(Member(member_id, name, borrowed_books))

    def add_book(self, book: Book) -> None:
        existing = self.find_book_by_id(book.book_id)
        if existing is not None:
            existing.update_copies(book.available_copies)
            return
        self.books.append(book)

    def add_member(self, member: Member) -> None:
        if self.find_member_by_id(member.member_id) is not None:
            return
        self.members.append(member)

    def display_all_books(self) -> List[str]:
        return [b.display_info() for b in self.books]

    def display_all_members(self) -> List[str]:
        return [m.display_member_info() for m in self.members]

    def find_member_by_id(self, member_id: str) -> Optional[Member]:
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    def find_book_by_title(self, title: str) -> Optional[Book]:
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

    def find_book_by_id(self, book_id: str) -> Optional[Book]:
        for b in self.books:
            if b.book_id == book_id:
                return b
        return None

    def borrow_transaction(self, member_id: str, book_title: str) -> str:
        member = self.find_member_by_id(member_id)
        if member is None:
            return "Member not found."
        book = self.find_book_by_title(book_title)
        if book is None:
            return "Book not found."
        if book.available_copies <= 0:
            return "No copies available to borrow."
        success = member.borrow_book(book)
        if not success:
            return "Cannot borrow: either unavailable or already borrowed by this member."
        book.borrow_count += 1
        self._log_transaction("BORROW", member.member_id, book.book_id, book.title)
        self.save_data()
        return "Book borrowed successfully!"

    def return_transaction(self, member_id: str, book_title: str) -> str:
        member = self.find_member_by_id(member_id)
        if member is None:
            return "Member not found."
        book = self.find_book_by_title(book_title)
        if book is None:
            return "Book not found."
        success = member.return_book(book)
        if not success:
            return "Cannot return: this book is not borrowed by the member."
        self._log_transaction("RETURN", member.member_id, book.book_id, book.title)
        self.save_data()
        return "Book returned successfully!"

    def _log_transaction(self, action: str, member_id: str, book_id: str, book_title: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(TRANSACTIONS_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp},{action},{member_id},{book_id},{book_title}\n")

    def most_borrowed_book(self) -> Optional[Book]:
        if not self.books:
            return None
        return max(self.books, key=lambda b: b.borrow_count)

    def search_by_author(self, author: str) -> List[Book]:
        return [b for b in self.books if b.author.lower() == author.lower()]

    def transaction_history(self) -> List[str]:
        lines: List[str] = []
        if os.path.exists(TRANSACTIONS_FILE):
            with open(TRANSACTIONS_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        lines.append(line.strip())
        return lines
