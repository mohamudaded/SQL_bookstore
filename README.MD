
## Bookstore Management System

This is a simple **Bookstore Management System** made with Python and SQLite. It lets you easily manage a bookstore’s collection of books, allowing you to add, update, delete, and search for books. Plus, there’s a basic menu to guide you through everything.

## Table of Contents:
1. [How to Get Started](#how-to-get-started)
2. [Sample Books](#sample-books)
3. [Example Use](#example-use)
4. [How it Works](#how-it-works)
5. [Functions](#functions)

## How to Get Started:

1. **Clone the repo** (if there is one) or copy the provided Python code into a new `.py` file.

2. **Install Python** (if you don’t have it yet):
   - Download and install Python 3.x from [python.org](https://www.python.org/downloads/).

3. **Run the script**:
   - Save the script as something like `bookstore_management.py`.
   - Run the script by typing this in your terminal:
     ```bash
     python bookstore_management.py
     ```

4. **Database Creation**:
   - The script will create a `bookstore.db` file (if it doesn’t already exist) in the same directory to store your bookstore’s data.

5. **Using the System**:
   - The program will show you a menu where you can:
     - **Add a book**: Input a new book.
     - **Update a book**: Change details for an existing book.
     - **Delete a book**: Remove a book from the database.
     - **Search for a book**: Find a book by title or author.
     - **Exit**: Quit the program.

6. **Sample Books**:
   - The system will come pre-loaded with a few sample books:
     - "A Tale of Two Cities" by Charles Dickens
     - "Harry Potter and the Philosopher's Stone" by J.K. Rowling
     - "The Lion, the Witch and the Wardrobe" by C.S. Lewis
     - "The Lord of the Rings" by J.R.R. Tolkien
     - "Alice in Wonderland" by Lewis Carroll

## Example Use:

1. **Add a Book**:
   ```
   Enter book title: The Great Gatsby
   Enter the author of the book: F. Scott Fitzgerald
   Enter the quantity of the book: 15
   Book added successfully!
   ```

2. **Update a Book**:
   ```
   Enter the book id to update: 2
   Enter the new title: Harry Potter and the Chamber of Secrets
   Enter the new author: J.K. Rowling
   Enter new quantity: 35
   Book updated successfully!
   ```

3. **Delete a Book**:
   ```
   Enter the book id you want to delete: 3
   Book deleted!
   ```

4. **Search for a Book**:
   ```
   Enter title or author to search: J.K. Rowling
   ID: 2, Title: Harry Potter and the Chamber of Secrets, Author: J.K. Rowling, Quantity: 35
   ```

## How it Works:

- **Database Setup**:
  When you run the script, it creates a database file called `bookstore.db` if it doesn’t exist. There’s a table `BOOK` with columns `id`, `title`, `author`, and `qty`. The `id` is automatically assigned and increments with each new book.

- **Functions**:
  - `add_book()`: Adds a new book with a unique ID.
  - `update_book()`: Allows you to update the title, author, or quantity of a book.
  - `delete_book()`: Deletes a book based on its ID.
  - `search_book()`: Finds books based on the title or author and shows matching results.
  - `populate_table()`: Adds some sample books to get you started (optional).
  - `menu()`: Displays the main menu so you can interact with the system.
