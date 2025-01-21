Sure! Here's a README file for the above code.

---

# Bookstore Management System

This is a simple **Bookstore Management System** built using Python and SQLite. It allows users to manage a collection of books in a bookstore. The system supports adding, updating, deleting, and searching for books, along with displaying a basic menu for interaction.

## Features:
- **Add a new book**: Enter the book's title, author, and quantity. The system automatically assigns a unique ID to the book.
- **Update book information**: Modify the title, author, or quantity of an existing book using its unique ID.
- **Delete a book**: Remove a book from the bookstore database using its unique ID.
- **Search for books**: Search by title or author to find matching books.
- **Menu-driven interface**: The user can interact with the system through a simple menu.

## Requirements:
- Python 3.x
- SQLite (integrated with Python, no additional installation needed)

## Setup Instructions:

1. **Clone the repository** (if applicable) or simply copy the provided Python code into a new Python file.

2. **Install Python** (if not already installed):
   - Download and install Python 3.x from [python.org](https://www.python.org/downloads/).

3. **Run the script**:
   - Save the code in a `.py` file (e.g., `bookstore_management.py`).
   - Run the script by executing the following command in your terminal or command prompt:
     ```bash
     python bookstore_management.py
     ```

4. **Database Creation**:
   - When you run the script, it will automatically create a database file called `bookstore.db` in the same directory if it doesn't already exist. This SQLite database will store the bookstore's information.

5. **Interact with the System**:
   - The program will prompt you to interact through a menu.
   - You can choose from the following options:
     - **Enter book**: Add a new book to the system.
     - **Update book**: Modify details of an existing book.
     - **Delete book**: Remove a book from the system.
     - **Search book**: Find a book by title or author.
     - **Exit**: Quit the program.

6. **Sample Data**:
   - When the script runs, a few sample books will be populated in the database. These include:
     - "A Tale of Two Cities" by Charles Dickens
     - "Harry Potter and the Philosopher's Stone" by J.K. Rowling
     - "The Lion, the Witch and the Wardrobe" by C.S. Lewis
     - "The Lord of the Rings" by J.R.R. Tolkien
     - "Alice in Wonderland" by Lewis Carroll

## Example Usage:

1. **Adding a Book**:
   ```
   Enter book title: The Great Gatsby
   Enter the author of the book: F. Scott Fitzgerald
   Enter the quantity of the book: 15
   Book added successfully
   ```

2. **Updating a Book**:
   ```
   Enter the book id to update: 2
   Enter the new title: Harry Potter and the Chamber of Secrets
   Enter the new author: J.K. Rowling
   Enter new quantity: 35
   Book updated successfully.
   ```

3. **Deleting a Book**:
   ```
   Enter the book id you want to delete: 3
   Book deleted
   ```

4. **Searching for a Book**:
   ```
   Enter title or author to search: J.K. Rowling
   ID: 2, Title: Harry Potter and the Chamber of Secrets, Author: J.K. Rowling, Quantity: 35
   ```

## Code Explanation:

- **Database Creation**:
  The SQLite database `bookstore.db` is created if it does not already exist. A table `BOOK` is created with columns `id`, `title`, `author`, and `qty`. The `id` column is an auto-incrementing primary key.

- **Functions**:
  - `add_book()`: Adds a new book to the `BOOK` table. The `id` is auto-generated.
  - `update_book()`: Updates the title, author, or quantity of an existing book using its unique ID.
  - `delete_book()`: Deletes a book from the database based on its ID.
  - `search_book()`: Searches for books by title or author and displays matching results.
  - `populate_table()`: Adds sample data to the database (optional).
  - `menu()`: Displays a menu with options for interacting with the system.


---
