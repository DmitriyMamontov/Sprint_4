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
    book_collector.add_new_book(BOOK_TITLE)
    book_collector.set_book_genre(BOOK_TITLE, GENRE)
    book_collector.add_book_in_favorites(BOOK_TITLE)
    return book_collector

@pytest.fixture()
def collector_many_book(book_collector):
    book_collector.add_new_book(BOOK_TITLE2)
    book_collector.set_book_genre(BOOK_TITLE2, GENRE2)
    book_collector.add_new_book(BOOK_TITLE3)
    book_collector.set_book_genre(BOOK_TITLE3, GENRE3)
    book_collector.add_new_book(BOOK_TITLE4)
    book_collector.set_book_genre(BOOK_TITLE4, GENRE4)
    book_collector.add_new_book(BOOK_TITLE5)
    book_collector.set_book_genre(BOOK_TITLE5, GENRE5)
    return book_collector

@pytest.fixture()
def collector_many_book_in_favorites(book_collector):
    book_collector.add_new_book(BOOK_TITLE2)
    book_collector.set_book_genre(BOOK_TITLE2, GENRE2)
    book_collector.add_new_book(BOOK_TITLE3)
    book_collector.set_book_genre(BOOK_TITLE3, GENRE3)
    book_collector.add_new_book(BOOK_TITLE4)
    book_collector.set_book_genre(BOOK_TITLE4, GENRE4)
    book_collector.add_new_book(BOOK_TITLE5)
    book_collector.set_book_genre(BOOK_TITLE5, GENRE5)
    books_to_add = [BOOK_TITLE2, BOOK_TITLE3, BOOK_TITLE4, BOOK_TITLE5]
    for book in books_to_add:
        book_collector.add_book_in_favorites(book)
    return book_collector
