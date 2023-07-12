# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .read_user_batch_message_response_body import ReadUserBatchMessageResponseBody


class ReadUserBatchMessageResponse(BaseResponse):
    _types = {
        "data": ReadUserBatchMessageResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ReadUserBatchMessageResponseBody] = None
        init(self, d, self._types)
