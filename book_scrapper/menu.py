import logging
from app import books

logger =  logging.getLogger('scraping.menu')

USER_CHOICE = """ Enter one of the following:

- 'b' to look at 5-star books
- 'c' to look at cheapest books
- 'n' to just get the next available book on the catalog
- 'q' to exit
Enter your choice: """


def print_best_rating_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)

# Sort by multiple things. above we sort by rating, lets say we want to
# do by rating (first) and then price
# we multiply by -1 to get desc order

def print_best_books():
    logger.info('Finding best books by rating and price...')
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)
def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b','c','n'):
            user_choices[user_input]()
        else:
            print("Please choose a valid command.")

        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')


menu()
# print("--- BEST RATED BOOKS")
# print_best_rating_books()
# print('--- BEST and PRICE ----')
# print_best_books()
# print('--- CHEAPEST ----')
# print_cheapest_books()