from typing import Optional
from book import Book
from member import Member
from library import Library


def prompt(msg: str) -> str:
    return input(msg).strip()


def add_new_book(lib: Library) -> None:
    book_id = prompt("Enter Book ID: ")
    title = prompt("Enter Title: ")
    author = prompt("Enter Author: ")
    copies_str = prompt("Enter Available Copies: ")
    try:
        copies = int(copies_str)
        if copies < 0:
            print("Available copies cannot be negative.")
            return
    except ValueError:
        print("Invalid number for available copies.")
        return
    lib.add_book(Book(book_id, title, author, copies))
    lib.save_data()
    print("Book added successfully!")


def add_new_member(lib: Library) -> None:
    member_id = prompt("Enter Member ID: ")
    name = prompt("Enter Name: ")
    lib.add_member(Member(member_id, name))
    lib.save_data()
    print("Member added successfully!")


def display_all_books(lib: Library) -> None:
    infos = lib.display_all_books()
    if not infos:
        print("No books available.")
        return
    for line in infos:
        print(line)


def display_all_members(lib: Library) -> None:
    infos = lib.display_all_members()
    if not infos:
        print("No members available.")
        return
    for line in infos:
        print(line)


def borrow_book(lib: Library) -> None:
    member_id = prompt("Enter Member ID: ")
    book_title = prompt("Enter Book Title to Borrow: ")
    result = lib.borrow_transaction(member_id, book_title)
    print(result)


def return_book(lib: Library) -> None:
    member_id = prompt("Enter Member ID: ")
    book_title = prompt("Enter Book Title to Return: ")
    result = lib.return_transaction(member_id, book_title)
    print(result)


def show_most_borrowed(lib: Library) -> None:
    book = lib.most_borrowed_book()
    if book is None:
        print("No books in library.")
    else:
        print("Most Borrowed Book:")
        print(book.display_info())


def search_by_author(lib: Library) -> None:
    author = prompt("Enter Author to Search: ")
    results = lib.search_by_author(author)
    if not results:
        print("No books found for the given author.")
        return
    for b in results:
        print(b.display_info())


def show_transactions(lib: Library) -> None:
    lines = lib.transaction_history()
    if not lines:
        print("No transactions recorded yet.")
        return
    print("Transaction History:")
    for l in lines:
        print(l)


def menu() -> None:
    lib = Library()
    while True:
        print("===== SMART LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add New Book")
        print("2. Add New Member")
        print("3. Display All Books")
        print("4. Display All Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Show Most Borrowed Book")
        print("8. Search by Author")
        print("9. Transaction History Report")
        print("10. Exit")
        choice = prompt("Enter your choice: ")
        print()
        if choice == "1":
            add_new_book(lib)
        elif choice == "2":
            add_new_member(lib)
        elif choice == "3":
            display_all_books(lib)
        elif choice == "4":
            display_all_members(lib)
        elif choice == "5":
            borrow_book(lib)
        elif choice == "6":
            return_book(lib)
        elif choice == "7":
            show_most_borrowed(lib)
        elif choice == "8":
            search_by_author(lib)
        elif choice == "9":
            show_transactions(lib)
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == "__main__":
    menu()
