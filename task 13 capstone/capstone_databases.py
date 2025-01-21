import sqlite3

'''COMPULSORY TASK'''

# Connect to the bookstore database or create if it does not exist
con = sqlite3.connect('bookstore.db')
cursor = con.cursor()

# Create book table
cursor.execute('''
CREATE TABLE IF NOT EXISTS BOOK(
    id INTEGER PRIMARY KEY ,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    qty INTEGER NOT NULL
)
''')
con.commit()

# Funtionto add new books


def add_book():
    id = int(input("Enter book id: "))
    title = input("Enter book title: ")
    author = input("Enter the author of the book:")
    qty = int(input("Enter the quantity of the book: "))
    cursor.execute("INSERT OR IGNORE INTO book(id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    con.commit()
    print(" Book added successfully")


# Function to update book information
def update_book():
    id = int(input("Enter the book id to update: "))
    new_title = input("Enter the new title: ")
    new_author = input("Enter the new author: ")
    new_qyt = int(input("Enter new quantity: "))
    cursor.execute("UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?", (id, new_title, new_author, new_qyt))
    con.commit()
    print("Book updated successfully.")


# Funtion to delete book
def delete_book():
    id = int(input("Enter the book id you want to delete: "))
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    con.commit()
    print("Book deleted")


# Funtion to search for book
def search_book():
    search = input("Enter title or author to search: ")
    cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?", ('%' + search + '%', '%' + search + '%'))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Quantity: {row[3]}")
    else:
        print("Book not found...")


# Funtion to dispaly menu
def menu():
    while True:
        print("\n BOOKSTORE MANAGEMENT SYSTEM")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4.Search book")
        print("0. Exit")
        choice = input("Enter your choice:")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_book()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again")


# Populate table
def populate_table():
    books = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 30),
        (3002, "Harry Potter and the Philosopher's Stone", "J.k.Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C.S.Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
        (3005, "Alice in Wonderland", "Lewis Carroll", 12)
    ]
    cursor.executemany("INSERT OR IGNORE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)", books)
    con.commit()


populate_table()


# Run menu function
menu()


# Close the database connection
con.close()
