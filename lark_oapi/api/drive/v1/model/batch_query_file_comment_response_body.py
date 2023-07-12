# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .file_comment import FileComment


class BatchQueryFileCommentResponseBody(object):
    _types = {
        "items": List[FileComment],
    }

    def __init__(self, d):
        self.items: Optional[List[FileComment]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchQueryFileCommentResponseBodyBuilder":
        return BatchQueryFileCommentResponseBodyBuilder()


class BatchQueryFileCommentResponseBodyBuilder(object):
    def __init__(self, batch_query_file_comment_response_body: BatchQueryFileCommentResponseBody = BatchQueryFileCommentResponseBody({})) -> None:
        self._batch_query_file_comment_response_body: BatchQueryFileCommentResponseBody = batch_query_file_comment_response_body
    
    def items(self, items: List[FileComment]) -> "BatchQueryFileCommentResponseBodyBuilder":
        self._batch_query_file_comment_response_body.items = items
        return self
    
    def build(self) -> "BatchQueryFileCommentResponseBody":
        return self._batch_query_file_comment_response_body