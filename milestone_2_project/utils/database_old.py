"""
Concerned with storing and retrieving pages from a csv file.
Format of the csv file:
name, author, read\n
(read: 0 for false, 1 for true)
"""

books_file = "pages.txt"

def add_book(name, author):
    with open(books_file, "a") as file:
        file.write(f"{name}, {author},0\n")


def get_all_books():
    with open(books_file, 'r') as file:
        books = [book.strip().split(',') for book in file.readlines()]
        for book in books:
            return book

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
            read = "Yes" if book['read'] else "No"
            print(f"New condition for title {book['name']} has been set to: {read}")
            break
    else:
        print(f"{book} not in book database. Try another title!")

# can use method below below but we have better alternative
# def delete_book(name):
#     for book in pages:
#         if book['name'] == name:
#             pages.remove(book)

def delete_book(name):
    # use global pages variable i.e. pages in the local scope(below) is equal to outer scope variable.
    books = [book for book in books if book['name'] != name]