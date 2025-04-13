import pytest


from conftest import book_collector


from data import *


class TestBooksCollector:

    def test_add_new_valid_book_add_one_book(self, book_collector):
        book_collector.add_new_book(BOOK_TITLE)
        assert BOOK_TITLE in book_collector.books_genre

    def test_add_new_book_not_genre_shows_not_genre(self, book_collector):
        book_collector.add_new_book(BOOK_TITLE)
        assert book_collector.books_genre[BOOK_TITLE] == ''

    @pytest.mark.parametrize(
        'name, book_count',
        [
            (['Гордость и предубеждение'], 1),
            (['Гордость и предубеждение', 'Что делать если ваш кот хочет вас убить'], 2),
            ([], 0),
            (['Название которое явно превышает сорок символов'], 0),
            (['Преступление', 'Преступление'], 1)
        ]
    )
    def test_add_new_book_add_different_quantity_books_shows_all_books(self, book_collector, name, book_count):
        for book_name in name:
            book_collector.add_new_book(book_name)
        book = book_collector.get_books_genre()
        assert len(book) == book_count

    @pytest.mark.parametrize(
        'name, genre, result',
        [
            ('Преступление и наказание', 'Детективы', {'Преступление и наказание': 'Детективы'}),
            ('Русалочка', 'Сказка', {'Русалочка': ''}),
            ('История России', '', {'История России': ''})

        ]
    )
    def test_set_book_genre_key_is_book_value_is_genre(self, book_collector, name, genre, result):
        if name in result:
            book_collector.add_new_book(name)
        book_collector.set_book_genre(name, genre)
        assert book_collector.books_genre == result

    def test_get_book_genre_shows_genre(self, collector_with_book):
        actual_genre = collector_with_book.get_book_genre(BOOK_TITLE)
        assert actual_genre == GENRE

    def test_get_books_with_specific_genre_shows_books_picked_genre(self, collector_many_book):
        result = collector_many_book.get_books_with_specific_genre(GENRE5)
        assert result == [BOOK_TITLE4, BOOK_TITLE5]

    def test_get_books_for_children_shows_books_with_children_genre(self, collector_many_book):
        children = collector_many_book.get_books_for_children()
        assert children == [BOOK_TITLE2]

    def test_get_books_for_children_dont_shows_books_with_not_children_genre(self, collector_many_book):
        children_books = collector_many_book.get_books_for_children()
        assert BOOK_TITLE4 not in children_books

    def test_add_book_in_favorites_favorites_add_book(self, collector_with_book):
        favorite = collector_with_book.get_list_of_favorites_books()
        assert BOOK_TITLE in favorite

    def test_delete_book_from_favorites_book_not_in_favorites(self, collector_with_book):
        collector_with_book.delete_book_from_favorites(BOOK_TITLE)
        assert BOOK_TITLE not in collector_with_book.favorites


    def test_get_list_of_favorites_books_shows_books_in_favorites(self, collector_many_book_in_favorites):
        favorites = collector_many_book_in_favorites.get_list_of_favorites_books()
        assert BOOK_TITLE4 in favorites and BOOK_TITLE2 in favorites
