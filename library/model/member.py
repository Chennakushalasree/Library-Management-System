from typing import List


class Member:
    """
    Represents a registered library member.
    Tracks which books the member currently has issued.
    """

    def __init__(self, member_id: str, name: str, email: str):
        if not member_id or not name or not email:
            raise ValueError("member_id, name and email are all required")
        self._member_id = member_id
        self._name = name
        self._email = email
        self._issued_book_isbns: List[str] = []

    @property
    def member_id(self) -> str:
        return self._member_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def issued_book_isbns(self) -> List[str]:
        return list(self._issued_book_isbns)  # defensive copy

    def add_issued_book(self, isbn: str) -> None:
        self._issued_book_isbns.append(isbn)

    def remove_issued_book(self, isbn: str) -> None:
        self._issued_book_isbns.remove(isbn)

    def has_issued_book(self, isbn: str) -> bool:
        return isbn in self._issued_book_isbns

    def __repr__(self) -> str:
        return (f"Member(id='{self._member_id}', name='{self._name}', "
                f"email='{self._email}', books_issued={len(self._issued_book_isbns)})")
