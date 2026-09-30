# Library Book Manager

## Overview

This is a terminal-based Python project for handling basic library book work. Run it, pick a number from the menu, and it does that job.

It covers the usual stuff: adding books, viewing the list, searching, issuing, returning, and checking whether a particular book is available or not.

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

## Screenshots
### Main Menu
<img width="488" height="168" alt="Screenshot 2026-09-30 at 10 58 42 AM" src="https://github.com/user-attachments/assets/be959242-038a-495f-b6de-7eb4897761ed" />

### Adding a Book
<img width="381" height="183" alt="Screenshot 2026-09-30 at 10 59 33 AM" src="https://github.com/user-attachments/assets/c150cbdd-81bc-43bf-9fb6-2d4384f69c28" />

### Viewing All Books
<img width="352" height="178" alt="Screenshot 2026-09-30 at 11 00 00 AM" src="https://github.com/user-attachments/assets/29076af1-62a9-43b9-aade-97a13fb8cf24" />

### Searching for a Book
<img width="366" height="217" alt="Screenshot 2026-09-30 at 11 00 46 AM" src="https://github.com/user-attachments/assets/c0758f03-1c4a-4b30-a3fc-44656cdfe33c" />

### Issuing a Book
<img width="363" height="161" alt="Screenshot 2026-09-30 at 11 01 08 AM" src="https://github.com/user-attachments/assets/b8cebaf4-e457-4d97-af80-0bc9107bf651" />

### Returning a Book
<img width="343" height="167" alt="Screenshot 2026-09-30 at 11 01 29 AM" src="https://github.com/user-attachments/assets/67283df3-d5da-485b-b84d-b21c3c1eb12d" />

### Checking Book Status
<img width="404" height="203" alt="Screenshot 2026-09-30 at 11 01 55 AM" src="https://github.com/user-attachments/assets/a2501e2d-4f3e-4f17-a98d-8d71c27e71c9" />

### Exiting the Program
<img width="390" height="154" alt="Screenshot 2026-09-30 at 11 02 37 AM" src="https://github.com/user-attachments/assets/643d7606-8dfe-46f9-b976-3a864b4ec8e1" />








