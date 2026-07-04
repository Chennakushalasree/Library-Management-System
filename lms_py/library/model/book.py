from library.model.book_status import BookStatus


class Book:
    """
    Represents a single physical/catalog copy of a book in the library.
    Responsible only for holding book data and its own status transitions.
    """

    def __init__(self, isbn: str, title: str, author: str):
        if not isbn or not title or not author:
            raise ValueError("isbn, title and author are all required")
        self._isbn = isbn
        self._title = title
        self._author = author
        self._status = BookStatus.AVAILABLE

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def status(self) -> BookStatus:
        return self._status

    def is_available(self) -> bool:
        return self._status == BookStatus.AVAILABLE

    def mark_issued(self) -> None:
        self._status = BookStatus.ISSUED

    def mark_available(self) -> None:
        self._status = BookStatus.AVAILABLE

    def __repr__(self) -> str:
        return (f"Book(isbn='{self._isbn}', title='{self._title}', "
                f"author='{self._author}', status={self._status.value})")
