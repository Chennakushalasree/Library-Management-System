# Library Management System — Low-Level Design (LLD)

## Overview
A Python implementation of a Library Management System built around clean
OOP and SOLID principles. It models real-world library operations: adding
books, registering members, issuing books, returning books, and preventing
issuance of unavailable books.

## Problem Statement
Design and implement a Library Management System that supports:
- Adding and managing books in the library
- Registering and managing members
- Issuing a book to a member
- Returning a book
- Tracking whether a book is available or issued
- Preventing issuing of unavailable books

## High-Level Design

The system is split into layers, each with a single responsibility:

```
library/model/       -> Plain data + behavior for core entities (Book, Member, BookStatus)
library/repository/  -> Storage abstraction (ABCs) + in-memory implementations
library/service/     -> Business logic, split into CatalogService and CirculationService
library/exception/   -> Domain-specific custom exceptions
main.py              -> Composition root; wires dependencies and demos the flow
```

### Why this structure (SOLID)
- **Single Responsibility**: `CatalogService` only manages books/members.
  `CirculationService` only handles issue/return logic. `Book` and `Member`
  only manage their own state.
- **Open/Closed**: Storage can be swapped (e.g. in-memory → database) by
  writing a new `BookRepository`/`MemberRepository` implementation — no
  service code changes needed.
- **Liskov Substitution**: Any `BookRepository`/`MemberRepository` or
  `CatalogService`/`CirculationService` implementation can replace the
  provided one without breaking callers, since all interactions go through
  abstract base classes.
- **Interface Segregation**: Repository and service ABCs expose only the
  methods relevant to their consumers — no bloated "God interfaces."
- **Dependency Inversion**: Services depend on repository *abstractions*
  (`ABC`s), not concrete classes. `main.py` (the composition root) is the
  only place concrete classes are instantiated and wired together.

## Key Classes and Responsibilities

| Class                       | Responsibility                                                     |
|------------------------------|----------------------------------------------------------------------|
| `Book`                       | Holds book data (ISBN, title, author) and its own `BookStatus`      |
| `Member`                     | Holds member data and the list of ISBNs currently issued to them    |
| `BookStatus`                 | Enum: `AVAILABLE` / `ISSUED`                                         |
| `BookRepository`             | ABC for book storage/retrieval                                       |
| `InMemoryBookRepository`     | In-memory `dict`-backed implementation of `BookRepository`           |
| `MemberRepository`           | ABC for member storage/retrieval                                     |
| `InMemoryMemberRepository`   | In-memory `dict`-backed implementation of `MemberRepository`         |
| `CatalogService`             | ABC: add books/members, search books, fetch books/members            |
| `CatalogServiceImpl`         | Default implementation of `CatalogService`                          |
| `CirculationService`         | ABC: issue and return books                                          |
| `CirculationServiceImpl`     | Default implementation, enforces availability rules                 |
| `main.py`                    | Composition root — wires everything together and runs a demo        |

### Exceptions (`library/exception/exceptions.py`)
- `BookNotFoundException` — raised when an ISBN doesn't exist
- `MemberNotFoundException` — raised when a member ID doesn't exist
- `BookNotAvailableException` — raised when trying to issue an already-issued book
- `BookNotIssuedToMemberException` — raised when trying to return a book the member doesn't have
- `DuplicateBookException` / `DuplicateMemberException` — raised on duplicate ISBN/member ID registration

## Core Flow

1. `CatalogService.add_book(...)` creates a `Book` (default status `AVAILABLE`) and stores it.
2. `CatalogService.register_member(...)` creates a `Member` and stores it.
3. `CirculationService.issue_book(isbn, member_id)`:
   - Looks up the book and member (raises if either doesn't exist).
   - Raises `BookNotAvailableException` if the book is already `ISSUED`.
   - Otherwise marks the book `ISSUED` and adds the ISBN to the member's issued list.
4. `CirculationService.return_book(isbn, member_id)`:
   - Looks up the book and member.
   - Raises `BookNotIssuedToMemberException` if that member doesn't currently hold the book.
   - Otherwise marks the book `AVAILABLE` and removes the ISBN from the member's issued list.

## Project Structure

```
lms_py/
├── README.md
├── main.py
└── library/
    ├── __init__.py
    ├── model/
    │   ├── __init__.py
    │   ├── book.py
    │   ├── book_status.py
    │   └── member.py
    ├── repository/
    │   ├── __init__.py
    │   ├── book_repository.py
    │   ├── in_memory_book_repository.py
    │   ├── member_repository.py
    │   └── in_memory_member_repository.py
    ├── service/
    │   ├── __init__.py
    │   ├── catalog_service.py
    │   ├── catalog_service_impl.py
    │   ├── circulation_service.py
    │   └── circulation_service_impl.py
    └── exception/
        ├── __init__.py
        └── exceptions.py
```

## Instructions to Run

Requires Python 3.8+. No external dependencies (standard library only).

```bash
# From the repository root:
python3 main.py
```

Expected output demonstrates: adding books, registering members, issuing a
book, a blocked re-issue of an already-issued book, a return, and a
successful re-issue after the return — plus a title search.

## Extending the System

- **New storage backend**: implement `BookRepository`/`MemberRepository`
  (e.g. `SqliteBookRepository`) and pass it into the existing services — no
  service-layer changes required.
- **Due dates / fines**: extend `Member`/`Book` or introduce an `Issue`
  entity (issue date, due date) without touching `CatalogService`.
- **Multiple copies per title**: introduce a `BookCopy` entity distinct
  from a catalog `Title` entity if copy-level tracking is needed.
