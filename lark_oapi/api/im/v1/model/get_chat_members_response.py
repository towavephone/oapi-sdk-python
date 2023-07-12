# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_chat_members_response_body import GetChatMembersResponseBody


class GetChatMembersResponse(BaseResponse):
    _types = {
        "data": GetChatMembersResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetChatMembersResponseBody] = None
        init(self, d, self._types)
