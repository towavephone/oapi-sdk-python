# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_task_comment_response_body import ListTaskCommentResponseBody


class ListTaskCommentResponse(BaseResponse):
    _types = {
        "data": ListTaskCommentResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListTaskCommentResponseBody] = None
        init(self, d, self._types)
