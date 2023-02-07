"""
# Q: What is a cursor?
## All operations in SQLite are made by cursors, and not by the connection object itself

# Q: What is commit()?
## "Save the result of this query to disk".

# Q: How do we write SQL?
## SQL is English-like!

### basics:
    connection = sqlite3.connect('data.db')
    # call a cursor, this is used to use SQL queries
    cursor = connection.cursor()

    cursor.execute("YOUR SQL QUERY HERE")
    # Save contents
    connection.commit()

    # once done with the connection always close the connection
    connection.close()

### Data types supported by SQLite
    - Null
    - Integer
    - Real - float
    - Text - string
    - Blob - Binary data field to store images, docs, PDFs and etc

"""
from utils import database_sqlite_old

USER_CHOICE = """
Enter: 
- 'a' to add a new book
- 'l' to list all pages
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database_sqlite.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Try again!")

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input("Enter name of book to add: ")
    author = input("Enter name of author to add: ")
    database_sqlite.add_book(name, author)

def list_books():
    books = database_sqlite.get_all_books()
    for book in books:
        read = "Yes" if book['read'] else "NO"  # if 0:false, if 1:true
        print(f"{book['name']}, {book['author']},{read}")

def prompt_read_book():
    user_input = input("Enter the name of book you just finished reading: ")
    database_sqlite.mark_book_as_read(user_input)

def prompt_delete_book():
    user_input = input("Enter name of book you want to delete: ")
    database_sqlite.delete_book(user_input)

menu()