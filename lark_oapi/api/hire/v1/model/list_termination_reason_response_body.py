# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .termination_reason import TerminationReason


class ListTerminationReasonResponseBody(object):
    _types = {
        "items": List[TerminationReason],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[TerminationReason]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTerminationReasonResponseBodyBuilder":
        return ListTerminationReasonResponseBodyBuilder()


class ListTerminationReasonResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_termination_reason_response_body = ListTerminationReasonResponseBody()

    def items(self, items: List[TerminationReason]) -> "ListTerminationReasonResponseBodyBuilder":
        self._list_termination_reason_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListTerminationReasonResponseBodyBuilder":
        self._list_termination_reason_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListTerminationReasonResponseBodyBuilder":
        self._list_termination_reason_response_body.page_token = page_token
        return self

    def build(self) -> "ListTerminationReasonResponseBody":
        return self._list_termination_reason_response_body
