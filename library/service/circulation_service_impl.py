from library.exception.exceptions import (
    BookNotAvailableException,
    BookNotFoundException,
    BookNotIssuedToMemberException,
    MemberNotFoundException,
)
from library.repository.book_repository import BookRepository
from library.repository.member_repository import MemberRepository
from library.service.circulation_service import CirculationService


class CirculationServiceImpl(CirculationService):
    """
    Default implementation of CirculationService.
    Coordinates state changes across Book and Member without exposing
    repository details to callers.
    """

    def __init__(self, book_repository: BookRepository, member_repository: MemberRepository):
        self._book_repository = book_repository
        self._member_repository = member_repository

    def issue_book(self, isbn: str, member_id: str) -> None:
        book = self._book_repository.find_by_isbn(isbn)
        if book is None:
            raise BookNotFoundException(isbn)

        member = self._member_repository.find_by_id(member_id)
        if member is None:
            raise MemberNotFoundException(member_id)

        if not book.is_available():
            raise BookNotAvailableException(isbn)

        book.mark_issued()
        member.add_issued_book(isbn)

    def return_book(self, isbn: str, member_id: str) -> None:
        book = self._book_repository.find_by_isbn(isbn)
        if book is None:
            raise BookNotFoundException(isbn)

        member = self._member_repository.find_by_id(member_id)
        if member is None:
            raise MemberNotFoundException(member_id)

        if not member.has_issued_book(isbn):
            raise BookNotIssuedToMemberException(isbn, member_id)

        book.mark_available()
        member.remove_issued_book(isbn)
