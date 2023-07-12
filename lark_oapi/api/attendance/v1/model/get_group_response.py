# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_group_response_body import GetGroupResponseBody


class GetGroupResponse(BaseResponse):
    _types = {
        "data": GetGroupResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetGroupResponseBody] = None
        init(self, d, self._types)
