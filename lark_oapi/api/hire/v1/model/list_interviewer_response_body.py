# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .interviewer import Interviewer


class ListInterviewerResponseBody(object):
    _types = {
        "items": List[Interviewer],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Interviewer]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListInterviewerResponseBodyBuilder":
        return ListInterviewerResponseBodyBuilder()


class ListInterviewerResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_interviewer_response_body = ListInterviewerResponseBody()

    def items(self, items: List[Interviewer]) -> "ListInterviewerResponseBodyBuilder":
        self._list_interviewer_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListInterviewerResponseBodyBuilder":
        self._list_interviewer_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListInterviewerResponseBodyBuilder":
        self._list_interviewer_response_body.has_more = has_more
        return self

    def build(self) -> "ListInterviewerResponseBody":
        return self._list_interviewer_response_body
