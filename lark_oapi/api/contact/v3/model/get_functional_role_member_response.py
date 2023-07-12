# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_functional_role_member_response_body import GetFunctionalRoleMemberResponseBody


class GetFunctionalRoleMemberResponse(BaseResponse):
    _types = {
        "data": GetFunctionalRoleMemberResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetFunctionalRoleMemberResponseBody] = None
        init(self, d, self._types)
