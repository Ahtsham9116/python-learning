# 📚 Library Management System

A simple console-based **Library Management System** built in Python to demonstrate core **Object-Oriented Programming (OOP)** concepts such as classes, encapsulation, and clean menu-driven program design.

---

## 🧠 Overview

This project simulates the basic operations of a library — adding books, borrowing them, returning them, and viewing book details — all through a text-based menu in the terminal. It's a beginner/intermediate mini project focused on writing clean, validated, class-based Python code rather than relying on procedural scripts.

---

## ✨ Features

- **Add Book** — Add a new book with a unique ID, title, author, and total copies (with input validation for empty fields, duplicate IDs, and invalid/non-positive numbers).
- **Borrow Book** — Borrow a copy of a book if one is available; automatically updates available/borrowed counts.
- **Return Book** — Return a previously borrowed copy.
- **Display Book Info** — Look up and display details for a single book by ID.
- **Display All Books** — List every book currently in the library with full details.
- **Exit** — Safely close the program.

---

## 🏗️ Project Structure & Design

The project uses two core classes:

### `Book`
Represents a single book and encapsulates its copy-tracking logic:
- `book_id`, `title`, `author` — public attributes
- `__total_copies`, `__borrowed_copies`, `__available_copies` — private attributes (name-mangled), only modified through class methods
- `borrow()` / `return_copy()` — safely update copy counts and return `True`/`False` based on success
- `display_info()` — prints formatted book details

### `Library`
Manages the collection of books:
- Stores books in a dictionary keyed by `book_id` for O(1) lookup
- `add_book()`, `borrow_book()`, `return_book()`, `display_book_info()`, `display_all_books()` — each handles its own user input and validation

A simple `display_menu()` function renders the CLI menu, and `main()` runs the program loop until the user chooses to exit.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Dependencies:** None — uses only the Python standard library (`input()`/`print()`)
- **Storage:** In-memory (data resets each time the program is run — no database or file persistence yet)

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Ahtsham9116/python-learning.git

# Navigate to this mini project
cd python-learning/librarymanagmentsystem

# Run the program (replace with your actual script filename if different)
python library_management_system.py
```

**Requirements:** Python 3.6 or higher (no external packages needed).

---

## 📋 Example Menu

```
===================================
     Library Management System     
===================================
1. Add Book
2. Borrow Book
3. Return Book
4. Display Book Information
5. Display All Books
6. Exit
Enter your choice (1-6):
```

---

## 🔮 Possible Future Improvements

- Persist data using a file (JSON/CSV) or a database (SQLite)
- Add member/user tracking for who borrowed which book
- Add due dates and fine calculation for late returns
- Add search functionality (by title or author)
- Build a GUI (Tkinter) or web version (Flask)

---

## 👤 Author

**Muhammad Ahtsham Javed**
Part of the [python-learning](https://github.com/Ahtsham9116/python-learning) repository — a collection of Python mini projects built while learning core programming and OOP concepts.
