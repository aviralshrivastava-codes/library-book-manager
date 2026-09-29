# Library Book Manager

## Overview

Library Book Manager is a simple **terminal-based Python project** that helps users manage basic library book operations.

The program allows users to add books, view books, search for books, issue and return books, and check the current status of a book.

## Features

- Add a new book with its title and author.
- Prevent duplicate book titles.
- View all books in the library.
- Search for a book by title.
- Issue an available book.
- Return an issued book.
- Check whether a book is Available or Issued.
- Handle empty inputs and invalid menu choices.
- Prevent issuing a book that is already issued.
- Prevent returning a book that is already available.

## Technologies / Tools Used

- **Programming Language:** Python
- **Interface:** Terminal / Command Line
- **Data Structures:** List and Dictionary
- **Code Editor:** Visual Studio Code
- **Version Control:** Git and GitHub

No external Python libraries are required.

## How to Install and Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version using:

```bash
python3 --version
```

### 2. Download or Clone the Repository

Download the project from GitHub or clone the repository using Git.

### 3. Open the Project

Open the project folder in Visual Studio Code.

### 4. Run the Program

Open the terminal in the project folder and run:

```bash
python3 library.py
```

If your Python file has a different name, replace `library.py` with the correct filename.

## How to Use

After running the program, the main menu will appear:

```text
===== LIBRARY BOOK MANAGER =====
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Check Book Status
7. Exit
```

Enter the number of the operation you want to perform.

For example:

```text
Enter your choice: 1
Enter book title: Python Basics
Enter author name: John
Book added successfully!
```

The book can then be viewed, searched, issued, returned, or checked for its current status.

## Testing

The project can be tested by performing the following operations:

| Test | Expected Result |
| --- | --- |
| Add a valid book | Book is added successfully |
| Add the same book again | Duplicate book is rejected |
| View books | All stored books are displayed |
| Search for an existing book | Book details are displayed |
| Search for a missing book | "Book not found" is displayed |
| Issue an available book | Book status becomes Issued |
| Issue an already issued book | Program prevents the operation |
| Return an issued book | Book status becomes Available |
| Return an available book | Appropriate message is displayed |
| Enter an invalid menu choice | Invalid choice message is displayed |
