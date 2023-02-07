"""
This app builds a book storing database along with other
functionalities such as deleting, updating read status and so forth
"""
from utils import database

USER_CHOICE = """
Enter: 
- 'a' to add a new book
- 'l' to list all pages
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            mark_read()
        elif user_input == 'd':
            delete_record()
        else:
            print("Unknown Command. Please try again!")

        # Reset user input
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input(f"Enter name of the book to add:")
    author = input(f"Enter the name of the author for the book.")
    database.add_book(name, author)
    print(f"The book {name} by {author} has been added to the database!")


def list_books():
    books = database.get_all_books()
    for book in books:
        read = "Yes" if book['read'] else "No" #(same as: "Yes" if book['read'] is True else "No")
        print(f"{book['name']}, by {book['author']}, read: {read}")


def mark_read():
    user_input = input(f"Enter title to mark as read: ")
    database.mark_book_as_read(user_input)


def delete_record():
    user_input = input("Enter title name to delete: ")
    database.delete_book(user_input)

menu()
