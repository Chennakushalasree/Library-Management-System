from typing import List

from library.exception.exceptions import BookNotFoundException, MemberNotFoundException
from library.model.book import Book
from library.model.member import Member
from library.repository.book_repository import BookRepository
from library.repository.member_repository import MemberRepository
from library.service.catalog_service import CatalogService


class CatalogServiceImpl(CatalogService):
    """
    Default implementation of CatalogService.
    Depends only on repository abstractions (Dependency Inversion Principle).
    """

    def __init__(self, book_repository: BookRepository, member_repository: MemberRepository):
        self._book_repository = book_repository
        self._member_repository = member_repository

    def add_book(self, isbn: str, title: str, author: str) -> Book:
        book = Book(isbn, title, author)
        self._book_repository.add(book)
        return book

    def register_member(self, member_id: str, name: str, email: str) -> Member:
        member = Member(member_id, name, email)
        self._member_repository.add(member)
        return member

    def get_all_books(self) -> List[Book]:
        return self._book_repository.find_all()

    def search_by_title(self, title: str) -> List[Book]:
        return self._book_repository.find_by_title(title)

    def get_all_members(self) -> List[Member]:
        return self._member_repository.find_all()

    def get_book(self, isbn: str) -> Book:
        book = self._book_repository.find_by_isbn(isbn)
        if book is None:
            raise BookNotFoundException(isbn)
        return book

    def get_member(self, member_id: str) -> Member:
        member = self._member_repository.find_by_id(member_id)
        if member is None:
            raise MemberNotFoundException(member_id)
        return member
