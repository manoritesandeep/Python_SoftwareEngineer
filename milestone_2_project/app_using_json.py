from utils import database_json

USER_CHOICE = """
Enter: 
- 'a' to add a new book
- 'l' to list all pages
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database_json.create_book_table()
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
    database_json.add_book(name, author)

def list_books():
    books = database_json.get_all_books()
    for book in books:
        read = "Yes" if book['read'] is True else "NO"
        print(f"{book['name']}, {book['author']},{read}")

def prompt_read_book():
    user_input = input("Enter the name of book you just finished reading: ")
    database_json.mark_book_as_read(user_input)

def prompt_delete_book():
    user_input = input("Enter name of book you want to delete: ")
    database_json.delete_book(user_input)

menu()