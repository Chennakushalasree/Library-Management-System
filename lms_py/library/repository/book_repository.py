from abc import ABC, abstractmethod
from typing import List, Optional

from library.model.book import Book


class BookRepository(ABC):
    """
    Abstraction over book storage. Allows the storage mechanism (in-memory,
    database, file, etc.) to change without affecting service-layer logic.
    """

    @abstractmethod
    def add(self, book: Book) -> None:
        ...

    @abstractmethod
    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        ...

    @abstractmethod
    def find_all(self) -> List[Book]:
        ...

    @abstractmethod
    def find_by_title(self, title: str) -> List[Book]:
        ...

    @abstractmethod
    def exists_by_isbn(self, isbn: str) -> bool:
        ...

    @abstractmethod
    def remove(self, isbn: str) -> None:
        ...
