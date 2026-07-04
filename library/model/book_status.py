from enum import Enum


class BookStatus(Enum):
    """Lifecycle status of a book copy."""
    AVAILABLE = "AVAILABLE"
    ISSUED = "ISSUED"
