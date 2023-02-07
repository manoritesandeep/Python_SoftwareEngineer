import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_contents = requests.get("http://books.toscrape.com").content
#print(page_content)
page = AllBooksPage(page_contents)

books = page.books

# for book in books:
#     print(book)

for page_num in range(1,page.page_count):
    url = f'http://books.toscrape.com/catalouge/{page_num+1}.html'
    page_contents = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_contents)
    books.extend(page.books)
