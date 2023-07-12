# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class DeleteFileResponseBody(object):
    _types = {
        "task_id": str,
    }

    def __init__(self, d):
        self.task_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteFileResponseBodyBuilder":
        return DeleteFileResponseBodyBuilder()


class DeleteFileResponseBodyBuilder(object):
    def __init__(self, delete_file_response_body: DeleteFileResponseBody = DeleteFileResponseBody({})) -> None:
        self._delete_file_response_body: DeleteFileResponseBody = delete_file_response_body
    
    def task_id(self, task_id: str) -> "DeleteFileResponseBodyBuilder":
        self._delete_file_response_body.task_id = task_id
        return self
    
    def build(self) -> "DeleteFileResponseBody":
        return self._delete_file_response_body