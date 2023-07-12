# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_user_response_body import ListUserResponseBody


class ListUserResponse(BaseResponse):
    _types = {
        "data": ListUserResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListUserResponseBody] = None
        init(self, d, self._types)
