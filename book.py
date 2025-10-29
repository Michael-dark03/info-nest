from dataclasses import dataclass


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    available_copies: int
    borrow_count: int = 0

    def display_info(self) -> str:
        return f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Available: {self.available_copies} | Borrowed: {self.borrow_count}"

    def update_copies(self, number: int) -> None:
        new_value = self.available_copies + number
        if new_value < 0:
            raise ValueError("Insufficient copies to decrease by given number.")
        self.available_copies = new_value
