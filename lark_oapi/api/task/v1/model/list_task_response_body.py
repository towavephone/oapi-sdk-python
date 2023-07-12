# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .task import Task


class ListTaskResponseBody(object):
    _types = {
        "items": List[Task],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d):
        self.items: Optional[List[Task]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTaskResponseBodyBuilder":
        return ListTaskResponseBodyBuilder()


class ListTaskResponseBodyBuilder(object):
    def __init__(self, list_task_response_body: ListTaskResponseBody = ListTaskResponseBody({})) -> None:
        self._list_task_response_body: ListTaskResponseBody = list_task_response_body
    
    def items(self, items: List[Task]) -> "ListTaskResponseBodyBuilder":
        self._list_task_response_body.items = items
        return self
    
    def page_token(self, page_token: str) -> "ListTaskResponseBodyBuilder":
        self._list_task_response_body.page_token = page_token
        return self
    
    def has_more(self, has_more: bool) -> "ListTaskResponseBodyBuilder":
        self._list_task_response_body.has_more = has_more
        return self
    
    def build(self) -> "ListTaskResponseBody":
        return self._list_task_response_body