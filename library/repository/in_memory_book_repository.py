from collections import OrderedDict
from typing import List, Optional

from library.exception.exceptions import DuplicateBookException
from library.model.book import Book
from library.repository.book_repository import BookRepository


class InMemoryBookRepository(BookRepository):
    """
    Simple in-memory implementation of BookRepository backed by a dict.
    Keyed by ISBN for O(1) lookups.
    """

    def __init__(self):
        self._books: "OrderedDict[str, Book]" = OrderedDict()

    def add(self, book: Book) -> None:
        if book.isbn in self._books:
            raise DuplicateBookException(book.isbn)
        self._books[book.isbn] = book

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        return self._books.get(isbn)

    def find_all(self) -> List[Book]:
        return list(self._books.values())

    def find_by_title(self, title: str) -> List[Book]:
        return [b for b in self._books.values() if b.title.lower() == title.lower()]

    def exists_by_isbn(self, isbn: str) -> bool:
        return isbn in self._books

    def remove(self, isbn: str) -> None:
        self._books.pop(isbn, None)
