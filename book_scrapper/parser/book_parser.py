import re
import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:
    """
    A class to take in HTML page (or part of it), and find properties
    of an item in it
    """

    RATINGS = {
        'One':1,
        'Two':2,
        "Three":3,
        "Four":4,
        "Five":5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f"<Book {self.name}, £{self.price}, ({self.rating} stars)>"

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_link}`.')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matches = re.search(pattern, item_price)
        float_price = float(matches.group(1))
        logger.debug(f'Found book matches, `{float_price}`.')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_class = self.parent.select_one(locator).attrs['class']
        star_rating = [e for e in star_rating_class if e != 'star-rating']
        rating_num = BookParser.RATINGS.get(star_rating[0])
        logger.debug(f'Found book rating, `{rating_num}`.')
        return rating_num