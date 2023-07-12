# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .group import Group


class GetGroupResponseBody(object):
    _types = {
        "group": Group,
    }

    def __init__(self, d):
        self.group: Optional[Group] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetGroupResponseBodyBuilder":
        return GetGroupResponseBodyBuilder()


class GetGroupResponseBodyBuilder(object):
    def __init__(self, get_group_response_body: GetGroupResponseBody = GetGroupResponseBody({})) -> None:
        self._get_group_response_body: GetGroupResponseBody = get_group_response_body
    
    def group(self, group: Group) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.group = group
        return self
    
    def build(self) -> "GetGroupResponseBody":
        return self._get_group_response_body