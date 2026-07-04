from abc import ABC, abstractmethod


class CirculationService(ABC):
    """
    Handles book circulation: issuing to members and processing returns.
    Kept separate from CatalogService per Single Responsibility Principle.
    """

    @abstractmethod
    def issue_book(self, isbn: str, member_id: str) -> None:
        """
        Issues the book with the given ISBN to the member with the given ID.
        Raises if the book/member does not exist or the book is already issued.
        """
        ...

    @abstractmethod
    def return_book(self, isbn: str, member_id: str) -> None:
        """
        Returns the book with the given ISBN on behalf of the member with
        the given ID. Raises if the book/member does not exist or the book
        was not issued to that member.
        """
        ...
