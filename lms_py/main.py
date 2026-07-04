"""
Composition root and demo entry point for the Library Management System.
Wires concrete repository implementations into the services, then
exercises the main functional requirements end-to-end.
"""

from library.exception.exceptions import BookNotAvailableException
from library.repository.in_memory_book_repository import InMemoryBookRepository
from library.repository.in_memory_member_repository import InMemoryMemberRepository
from library.service.catalog_service_impl import CatalogServiceImpl
from library.service.circulation_service_impl import CirculationServiceImpl


def print_books(books) -> None:
    for book in books:
        print(f"  {book}")


def main() -> None:
    # --- Wiring (composition root) ---
    book_repository = InMemoryBookRepository()
    member_repository = InMemoryMemberRepository()

    catalog_service = CatalogServiceImpl(book_repository, member_repository)
    circulation_service = CirculationServiceImpl(book_repository, member_repository)

    # --- Add books ---
    catalog_service.add_book("ISBN001", "Clean Code", "Robert C. Martin")
    catalog_service.add_book("ISBN002", "Design Patterns", "Gang of Four")
    catalog_service.add_book("ISBN003", "Effective Java", "Joshua Bloch")

    # --- Register members ---
    catalog_service.register_member("M001", "Kushala Sree", "kushala@example.com")
    catalog_service.register_member("M002", "Arjun Rao", "arjun@example.com")

    print("=== Initial Catalog ===")
    print_books(catalog_service.get_all_books())

    # --- Issue a book ---
    print("\n=== Issuing ISBN001 to M001 ===")
    circulation_service.issue_book("ISBN001", "M001")
    print_books(catalog_service.get_all_books())

    # --- Attempt to issue the same book to another member (should fail) ---
    print("\n=== Attempting to issue ISBN001 to M002 (already issued) ===")
    try:
        circulation_service.issue_book("ISBN001", "M002")
    except BookNotAvailableException as e:
        print(f"Expected failure: {e}")

    # --- Return the book ---
    print("\n=== Returning ISBN001 from M001 ===")
    circulation_service.return_book("ISBN001", "M001")
    print_books(catalog_service.get_all_books())

    # --- Now issuing to M002 succeeds ---
    print("\n=== Issuing ISBN001 to M002 (now available) ===")
    circulation_service.issue_book("ISBN001", "M002")
    print_books(catalog_service.get_all_books())

    print("\n=== Search by title: 'Effective Java' ===")
    print_books(catalog_service.search_by_title("Effective Java"))


if __name__ == "__main__":
    main()
