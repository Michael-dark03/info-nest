Smart Library Management System (Python)

How to run
1) Ensure you have Python 3.10+ installed.
2) Open a terminal in this folder and run:
   python main.py

Files
- main.py: Entry point with a menu-driven CLI.
- book.py: Book class with display_info and update_copies.
- member.py: Member class with borrow_book, return_book, display_member_info.
- library.py: Library class managing books, members, transactions, and file persistence.
- books.txt: Persistent storage for books (CSV: book_id,title,author,available_copies,borrow_count).
- members.txt: Persistent storage for members (CSV: member_id,name,borrowed_book_ids;... semicolon-separated).
- transactions.txt: Transaction log (CSV: timestamp,action,member_id,book_id,book_title).

Assumptions
- Book titles are unique for borrow/return operations. Internally we also use immutable book_id for persistence and member borrow tracking.
- CSV is used without escaping commas inside fields; please avoid commas in titles or names.
- Adding a book with an existing book_id increases available copies.
- Member re-adding with same member_id is ignored.

Features
- Manage books and members.
- Borrow and return transactions with validation.
- File persistence using with statements.
- Most borrowed book tracking (borrow_count).
- Transaction history report.
- Search by author.
- Simple, readable CLI output.
