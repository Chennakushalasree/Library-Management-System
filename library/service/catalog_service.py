from abc import ABC, abstractmethod
from typing import List

from library.model.book import Book
from library.model.member import Member


class CatalogService(ABC):
    """
    Handles catalog-level operations: adding/looking up books and members.
    Kept separate from circulation (issue/return) logic per Single
    Responsibility Principle.
    """

    @abstractmethod
    def add_book(self, isbn: str, title: str, author: str) -> Book:
        ...

    @abstractmethod
    def register_member(self, member_id: str, name: str, email: str) -> Member:
        ...

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        ...

    @abstractmethod
    def search_by_title(self, title: str) -> List[Book]:
        ...

    @abstractmethod
    def get_all_members(self) -> List[Member]:
        ...

    @abstractmethod
    def get_book(self, isbn: str) -> Book:
        ...

    @abstractmethod
    def get_member(self, member_id: str) -> Member:
        ...
