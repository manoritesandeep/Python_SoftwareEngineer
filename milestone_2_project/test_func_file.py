# sample_books = [
#     {
#     "name": "Peter Pan",
#     "author": "abc",
#     }
# ]

# "a": prompt_add_book,
# "l": list_books,
# "r": prompt_read_books
# "d": prompt_delete_books
books_db = []

def prompt_add_book():
    name = input(f"Enter name of the book to add:")
    author = input(f"Enter the name of the author for the book.")
    books_db.append(
        {
            "name":name,
            "author": author,
            "read": False
         }
    )
    print(f"The book {name} by {author} has been added to the database!")

prompt_add_book()
#print(books_db)   # [{'name': 'Peter', 'author': 'Pan', 'read': False}]

def list_books(book_name):
    for book in books_db:
        if book_name == book['name']:
            print(f"Books in the database are: {book['name']} by {book['author']}.")
            break
        else:
            print("Book not in book database. Try another title!")
# list_books() #Books in the database are: Peter Pan.\n Books in the database are: P2.
list_books("abc")


def mark_read():
    user_input = input(f"Enter title to mark as read: ")
    for name in books_db:
        if user_input == name['name']:
            name['read'] = True
            print(f"New condition for title {user_input} has been set to: {name['read']}")
            break
    else:
        print(f"{user_input} not in book database. Try another title!")
#mark_read()

sb = [
    {"name": "P","author": "abc","read": False},
    {"name": "P1","author": "abcd","read": False}
]

def delete_record():
    user_input = input("Enter title name to delete: ")
    for book in sb:
        #print(names['name'])
        if book['name'] == user_input:
            sb.remove(user_input)
            # print(sb)
            break
    else:
        print(f"{user_input} title not valid!")

delete_record()