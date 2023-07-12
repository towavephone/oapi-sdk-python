# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .mailgroup_permission_member import MailgroupPermissionMember


class ListMailgroupPermissionMemberResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[MailgroupPermissionMember],
    }

    def __init__(self, d):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[MailgroupPermissionMember]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListMailgroupPermissionMemberResponseBodyBuilder":
        return ListMailgroupPermissionMemberResponseBodyBuilder()


class ListMailgroupPermissionMemberResponseBodyBuilder(object):
    def __init__(self, list_mailgroup_permission_member_response_body: ListMailgroupPermissionMemberResponseBody = ListMailgroupPermissionMemberResponseBody({})) -> None:
        self._list_mailgroup_permission_member_response_body: ListMailgroupPermissionMemberResponseBody = list_mailgroup_permission_member_response_body
    
    def has_more(self, has_more: bool) -> "ListMailgroupPermissionMemberResponseBodyBuilder":
        self._list_mailgroup_permission_member_response_body.has_more = has_more
        return self
    
    def page_token(self, page_token: str) -> "ListMailgroupPermissionMemberResponseBodyBuilder":
        self._list_mailgroup_permission_member_response_body.page_token = page_token
        return self
    
    def items(self, items: List[MailgroupPermissionMember]) -> "ListMailgroupPermissionMemberResponseBodyBuilder":
        self._list_mailgroup_permission_member_response_body.items = items
        return self
    
    def build(self) -> "ListMailgroupPermissionMemberResponseBody":
        return self._list_mailgroup_permission_member_response_body