# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class BatchQueryFileCommentRequestBody(object):
    _types = {
        "comment_ids": List[str],
    }

    def __init__(self, d):
        self.comment_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchQueryFileCommentRequestBodyBuilder":
        return BatchQueryFileCommentRequestBodyBuilder()


class BatchQueryFileCommentRequestBodyBuilder(object):
    def __init__(self, batch_query_file_comment_request_body: BatchQueryFileCommentRequestBody = BatchQueryFileCommentRequestBody({})) -> None:
        self._batch_query_file_comment_request_body: BatchQueryFileCommentRequestBody = batch_query_file_comment_request_body
    
    def comment_ids(self, comment_ids: List[str]) -> "BatchQueryFileCommentRequestBodyBuilder":
        self._batch_query_file_comment_request_body.comment_ids = comment_ids
        return self
    
    def build(self) -> "BatchQueryFileCommentRequestBody":
        return self._batch_query_file_comment_request_body