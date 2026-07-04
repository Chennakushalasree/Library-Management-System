class BookNotFoundException(Exception):
    def __init__(self, isbn: str):
        super().__init__(f"Book not found with ISBN: {isbn}")


class MemberNotFoundException(Exception):
    def __init__(self, member_id: str):
        super().__init__(f"Member not found with ID: {member_id}")


class BookNotAvailableException(Exception):
    def __init__(self, isbn: str):
        super().__init__(f"Book with ISBN {isbn} is currently issued and not available.")


class BookNotIssuedToMemberException(Exception):
    def __init__(self, isbn: str, member_id: str):
        super().__init__(f"Book with ISBN {isbn} was not issued to member {member_id}.")


class DuplicateBookException(Exception):
    def __init__(self, isbn: str):
        super().__init__(f"Book with ISBN {isbn} already exists.")


class DuplicateMemberException(Exception):
    def __init__(self, member_id: str):
        super().__init__(f"Member with ID {member_id} already exists.")
