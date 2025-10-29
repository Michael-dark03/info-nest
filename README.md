
# 📚 Smart Library Management System

A comprehensive Python-based library management system implementing Object-Oriented Programming principles with persistent data storage.

## 🌟 Features

- **Book Management**: Add, display, and track books with availability status
- **Member Management**: Register members and track their borrowing history
- **Borrowing System**: Borrow and return books with validation
- **Transaction History**: Complete audit trail of all library transactions
- **Advanced Features**:
  - Track and display most borrowed books
  - Search books by author
  - Generate transaction history reports
- **Data Persistence**: All data saved to files and persists between sessions

## 🏗️ Architecture

The system follows OOP principles with three main classes:

### `Book` Class
- **Attributes**: `book_id`, `title`, `author`, `available_copies`, `borrow_count`
- **Methods**:
  - `display_info()` - Display book details
  - `update_copies(number)` - Update available copies

### `Member` Class
- **Attributes**: `member_id`, `name`, `borrowed_books`
- **Methods**:
  - `borrow_book(book)` - Borrow a book if available
  - `return_book(book)` - Return a borrowed book
  - `display_member_info()` - Display member details

### `Library` Class
- **Attributes**: `books`, `members`
- **Methods**:
  - `add_book(book)`, `add_member(member)`
  - `display_all_books()`, `display_all_members()`
  - `borrow_transaction()`, `return_transaction()`
  - `most_borrowed_book()` - Find most popular book
  - `search_by_author(author)` - Search books by author
  - `transaction_history()` - View all transactions

## 🚀 How to Run

### Prerequisites
- Python 3.10 or higher

### Running the Program

1. Clone and navigate to the project directory:
   ```bash
   git clone https://github.com/Michael-dark03/info-nest.git
   cd info-nest
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

3. Follow the interactive menu to manage your library!

## 📋 Menu Options

```
===== SMART LIBRARY MANAGEMENT SYSTEM =====
1. Add New Book
2. Add New Member
3. Display All Books
4. Display All Members
5. Borrow Book
6. Return Book
7. Show Most Borrowed Book
8. Search by Author
9. Transaction History Report
10. Exit
```

## 📁 Project Structure

```
info-nest/
├── main.py              # Entry point with menu-driven interface
├── book.py              # Book class definition
├── member.py            # Member class definition
├── library.py           # Library class with core logic
├── books.txt            # Persistent storage for books
├── members.txt          # Persistent storage for members
├── transactions.txt     # Transaction log file
└── README.md            # This file
```

## 💾 Data Storage

The system uses CSV-based file storage:

- **books.txt**: `book_id,title,author,available_copies,borrow_count`
- **members.txt**: `member_id,name,borrowed_book_ids` (semicolon-separated)
- **transactions.txt**: `timestamp,action,member_id,book_id,book_title`

## 🎯 Sample Usage

### Adding a Book
```
Enter your choice: 1
Enter Book ID: B001
Enter Title: Python for Beginners
Enter Author: Jane Doe
Enter Available Copies: 5
Book added successfully!
```

### Displaying Books
```
Enter your choice: 3
Book ID: B001 | Title: Python for Beginners | Author: Jane Doe | Available: 5 | Borrowed: 0
Book ID: B002 | Title: Data Structures | Author: John Smith | Available: 3 | Borrowed: 2
```

### Borrowing a Book
```
Enter your choice: 5
Enter Member ID: M001
Enter Book Title to Borrow: Python for Beginners
Book borrowed successfully!
```

## ⚠️ Assumptions

- Book titles are case-insensitive and treated as unique for borrow/return operations
- Avoid using commas in book titles, author names, or member names (CSV limitation)
- Adding a book with an existing `book_id` increases available copies
- Re-adding a member with the same `member_id` is ignored
- Transaction history is append-only and persists indefinitely

## 🔍 Error Handling

The system handles:
- Borrowing unavailable books
- Returning books not borrowed by the member
- Invalid member or book lookups
- Negative copy counts
- Invalid input validation

## 👨‍💻 Code Quality

- Follows **PEP 8** style guidelines
- Uses **type hints** for better code clarity
- Implements proper **error handling**
- Utilizes Python's **`with` statements** for file operations
- Uses **`@dataclass`** for clean class definitions

## 📝 License

This project is created for educational purposes as part of a Python scripting class.
