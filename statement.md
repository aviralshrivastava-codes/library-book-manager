# Library Book Manager

## Problem Statement

Small libraries usually keep track of books on paper or in a spreadsheet that nobody updates properly. Things go wrong fast. The same title gets entered twice, nobody remembers which books are out, and a book that's already been issued gets handed to someone else.

This project is a simple terminal program that fixes that. It keeps one list of books and knows at any moment whether each book is Available or Issued.

## Scope of the Project

The project covers these operations:

- Adding books with a title and author, and rejecting duplicate titles
- Viewing all books and searching by title
- Issuing and returning books, with checks that block invalid operations
- Checking whether a book is Available or Issued
- Handling empty input and invalid menu choices

It's built as a command-line program, so everything runs from the terminal.

## Target Users

- Librarians or volunteers at a small library who need a quick way to manage book records
- Students learning Python who want a small project that's easy to read and uses lists and dictionaries

## High-Level Features

- Add a book, with duplicates rejected
- View every book in the library
- Search for a book by title
- Issue a book, blocked if it's already issued
- Return a book, blocked if it's already available
- Check a book's status
- Menu-driven interface that checks the input
