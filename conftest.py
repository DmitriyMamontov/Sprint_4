from main import BooksCollector


import pytest


from data import *


@pytest.fixture()
def book_collector():
    collector = BooksCollector()
    collector.books_genre = {}
    return collector

@pytest.fixture()
def collector_with_book(book_collector):
    book_collector.books_genre = {
        BOOK_TITLE: GENRE, BOOK_TITLE2: GENRE2, BOOK_TITLE3: GENRE3, BOOK_TITLE4: GENRE4, BOOK_TITLE5: GENRE5
    }
    return book_collector

@pytest.fixture()
def collector_many_book_in_favorites(book_collector):
    book_collector.favorites = [BOOK_TITLE2, BOOK_TITLE3, BOOK_TITLE4, BOOK_TITLE5]
    return book_collector
