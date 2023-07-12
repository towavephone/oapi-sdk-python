# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_permission_member_response_body import UpdatePermissionMemberResponseBody


class UpdatePermissionMemberResponse(BaseResponse):
    _types = {
        "data": UpdatePermissionMemberResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UpdatePermissionMemberResponseBody] = None
        init(self, d, self._types)
