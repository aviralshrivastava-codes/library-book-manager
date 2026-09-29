# Library Book Manager
# Terminal-based Python project

books = []


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if title == "" or author == "":
        print("Please enter all the details.")
        return

    # Check if the same book already exists
    for book in books:
        if book["title"].lower() == title.lower():
            print("A book with this title already exists.")
            return

    book = {
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    print("Book added successfully!")


def view_books():
    if len(books) == 0:
        print("There are no books in the library.")
        return

    print("\n--- Books in Library ---")

    for number, book in enumerate(books, start=1):
        if book["issued"]:
            status = "Issued"
        else:
            status = "Available"

        print(number, ".", book["title"], "-", book["author"], "-", status)


def search_book():
    title = input("Enter book title to search: ").strip()

    if title == "":
        print("Please enter a book title.")
        return

    for book in books:
        if title.lower() == book["title"].lower():
            if book["issued"]:
                status = "Issued"
            else:
                status = "Available"

            print("\nBook found!")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", status)
            return

    print("Sorry, book not found.")


def issue_book():
    title = input("Enter book title to issue: ").strip()

    if title == "":
        print("Please enter a book title.")
        return

    for book in books:
        if title.lower() == book["title"].lower():

            if book["issued"]:
                print("This book is already issued.")
            else:
                book["issued"] = True
                print("Book issued successfully!")

            return

    print("Book not found.")


def return_book():
    title = input("Enter book title to return: ").strip()

    if title == "":
        print("Please enter a book title.")
        return

    for book in books:
        if title.lower() == book["title"].lower():

            if book["issued"]:
                book["issued"] = False
                print("Book returned successfully!")
            else:
                print("This book is already available.")

            return

    print("Book not found.")


def check_status():
    title = input("Enter book title: ").strip()

    if title == "":
        print("Please enter a book title.")
        return

    for book in books:
        if title.lower() == book["title"].lower():

            print("\nTitle:", book["title"])
            print("Author:", book["author"])

            if book["issued"]:
                print("Status: Issued")
            else:
                print("Status: Available")

            return

    print("Book not found.")


def main():
    while True:
        print("\n===== LIBRARY BOOK MANAGER =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Check Book Status")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            check_status()

        elif choice == "7":
            print("Thank you for using the Library Book Manager.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 7.")


main()
