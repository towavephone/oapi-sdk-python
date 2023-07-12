# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_user_response_body import GetUserResponseBody


class GetUserResponse(BaseResponse):
    _types = {
        "data": GetUserResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetUserResponseBody] = None
        init(self, d, self._types)
