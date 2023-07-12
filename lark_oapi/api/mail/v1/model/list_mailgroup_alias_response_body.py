# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .email_alias import EmailAlias


class ListMailgroupAliasResponseBody(object):
    _types = {
        "items": List[EmailAlias],
    }

    def __init__(self, d):
        self.items: Optional[List[EmailAlias]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListMailgroupAliasResponseBodyBuilder":
        return ListMailgroupAliasResponseBodyBuilder()


class ListMailgroupAliasResponseBodyBuilder(object):
    def __init__(self, list_mailgroup_alias_response_body: ListMailgroupAliasResponseBody = ListMailgroupAliasResponseBody({})) -> None:
        self._list_mailgroup_alias_response_body: ListMailgroupAliasResponseBody = list_mailgroup_alias_response_body
    
    def items(self, items: List[EmailAlias]) -> "ListMailgroupAliasResponseBodyBuilder":
        self._list_mailgroup_alias_response_body.items = items
        return self
    
    def build(self) -> "ListMailgroupAliasResponseBody":
        return self._list_mailgroup_alias_response_body