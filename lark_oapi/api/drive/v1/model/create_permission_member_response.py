# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_permission_member_response_body import CreatePermissionMemberResponseBody


class CreatePermissionMemberResponse(BaseResponse):
    _types = {
        "data": CreatePermissionMemberResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreatePermissionMemberResponseBody] = None
        init(self, d, self._types)
