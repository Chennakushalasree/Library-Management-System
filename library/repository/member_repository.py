from abc import ABC, abstractmethod
from typing import List, Optional

from library.model.member import Member


class MemberRepository(ABC):
    """Abstraction over member storage."""

    @abstractmethod
    def add(self, member: Member) -> None:
        ...

    @abstractmethod
    def find_by_id(self, member_id: str) -> Optional[Member]:
        ...

    @abstractmethod
    def find_all(self) -> List[Member]:
        ...

    @abstractmethod
    def exists_by_id(self, member_id: str) -> bool:
        ...
