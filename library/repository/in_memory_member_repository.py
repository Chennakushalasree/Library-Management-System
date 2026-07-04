from collections import OrderedDict
from typing import List, Optional

from library.exception.exceptions import DuplicateMemberException
from library.model.member import Member
from library.repository.member_repository import MemberRepository


class InMemoryMemberRepository(MemberRepository):
    """Simple in-memory implementation of MemberRepository backed by a dict."""

    def __init__(self):
        self._members: "OrderedDict[str, Member]" = OrderedDict()

    def add(self, member: Member) -> None:
        if member.member_id in self._members:
            raise DuplicateMemberException(member.member_id)
        self._members[member.member_id] = member

    def find_by_id(self, member_id: str) -> Optional[Member]:
        return self._members.get(member_id)

    def find_all(self) -> List[Member]:
        return list(self._members.values())

    def exists_by_id(self, member_id: str) -> bool:
        return member_id in self._members
