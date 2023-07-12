# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_file_comment_response_body import ListFileCommentResponseBody


class ListFileCommentResponse(BaseResponse):
    _types = {
        "data": ListFileCommentResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListFileCommentResponseBody] = None
        init(self, d, self._types)
