# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class PatchFileCommentRequestBody(object):
    _types = {
        "is_solved": bool,
    }

    def __init__(self, d):
        self.is_solved: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchFileCommentRequestBodyBuilder":
        return PatchFileCommentRequestBodyBuilder()


class PatchFileCommentRequestBodyBuilder(object):
    def __init__(self, patch_file_comment_request_body: PatchFileCommentRequestBody = PatchFileCommentRequestBody({})) -> None:
        self._patch_file_comment_request_body: PatchFileCommentRequestBody = patch_file_comment_request_body
    
    def is_solved(self, is_solved: bool) -> "PatchFileCommentRequestBodyBuilder":
        self._patch_file_comment_request_body.is_solved = is_solved
        return self
    
    def build(self) -> "PatchFileCommentRequestBody":
        return self._patch_file_comment_request_body