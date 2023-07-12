# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .functional_role_member import FunctionalRoleMember


class GetFunctionalRoleMemberResponseBody(object):
    _types = {
        "member": FunctionalRoleMember,
    }

    def __init__(self, d):
        self.member: Optional[FunctionalRoleMember] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetFunctionalRoleMemberResponseBodyBuilder":
        return GetFunctionalRoleMemberResponseBodyBuilder()


class GetFunctionalRoleMemberResponseBodyBuilder(object):
    def __init__(self, get_functional_role_member_response_body: GetFunctionalRoleMemberResponseBody = GetFunctionalRoleMemberResponseBody({})) -> None:
        self._get_functional_role_member_response_body: GetFunctionalRoleMemberResponseBody = get_functional_role_member_response_body
    
    def member(self, member: FunctionalRoleMember) -> "GetFunctionalRoleMemberResponseBodyBuilder":
        self._get_functional_role_member_response_body.member = member
        return self
    
    def build(self) -> "GetFunctionalRoleMemberResponseBody":
        return self._get_functional_role_member_response_body