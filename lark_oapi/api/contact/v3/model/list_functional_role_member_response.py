# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_functional_role_member_response_body import ListFunctionalRoleMemberResponseBody


class ListFunctionalRoleMemberResponse(BaseResponse):
    _types = {
        "data": ListFunctionalRoleMemberResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListFunctionalRoleMemberResponseBody] = None
        init(self, d, self._types)
