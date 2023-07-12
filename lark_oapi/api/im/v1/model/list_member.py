# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ListMember(object):
    _types = {
        "member_id_type": str,
        "member_id": str,
        "name": str,
        "tenant_key": str,
    }

    def __init__(self, d):
        self.member_id_type: Optional[str] = None
        self.member_id: Optional[str] = None
        self.name: Optional[str] = None
        self.tenant_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListMemberBuilder":
        return ListMemberBuilder()


class ListMemberBuilder(object):
    def __init__(self, list_member: ListMember = ListMember({})) -> None:
        self._list_member: ListMember = list_member
    
    def member_id_type(self, member_id_type: str) -> "ListMemberBuilder":
        self._list_member.member_id_type = member_id_type
        return self
    
    def member_id(self, member_id: str) -> "ListMemberBuilder":
        self._list_member.member_id = member_id
        return self
    
    def name(self, name: str) -> "ListMemberBuilder":
        self._list_member.name = name
        return self
    
    def tenant_key(self, tenant_key: str) -> "ListMemberBuilder":
        self._list_member.tenant_key = tenant_key
        return self
    
    def build(self) -> "ListMember":
        return self._list_member