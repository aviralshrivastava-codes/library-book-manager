# Library Book Manager

## Overview

This is a terminal-based Python project for handling basic library book work. Run it, pick a number from the menu, and it does that job.

It covers the usual stuff: adding books, viewing the list, searching, issuing, returning, and checking whether a particular book is in or out.

## Features

- Add a book with a title and author
- Duplicate titles are rejected
- View all the books in the library
- Search by title
- Issue a book if it's available
- Return a book that was issued
- Check if a book is Available or Issued
- Empty inputs and wrong menu choices get handled instead of crashing the program
- A book that's already issued can't be issued again
- A book that's already available can't be returned

## Technologies / Tools Used

- **Language:** Python
- **Interface:** Terminal / command line
- **Data structures:** List and dictionary
- **Editor:** Visual Studio Code
- **Version control:** Git and GitHub

No external Python libraries needed.

## How to Install and Run

### 1. Install Python

Check that Python is already on your computer:

```bash
python3 --version
```

### 2. Download or Clone the Repository

Download the project from GitHub, or clone it with Git.

### 3. Open the Project

Open the project folder in Visual Studio Code.

### 4. Run the Program

In the terminal, from the project folder:

```bash
python3 library.py
```

Named your file something else? Use that name instead of `library.py`.

## How to Use

When the program starts, this menu shows up:

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

Enter the number for the operation you want.

Here's adding a book, for example:

```text
Enter your choice: 1
Enter book title: Python Basics
Enter author name: John
Book added successfully!
```

From there you can view the book, search for it, issue it, return it, or check its status.

## Testing

Try each of these and compare what happens with the expected result:

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
