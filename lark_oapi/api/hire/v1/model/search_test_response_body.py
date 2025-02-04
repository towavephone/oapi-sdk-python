# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .test import Test


class SearchTestResponseBody(object):
    _types = {
        "items": List[Test],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Test]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchTestResponseBodyBuilder":
        return SearchTestResponseBodyBuilder()


class SearchTestResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_test_response_body = SearchTestResponseBody()

    def items(self, items: List[Test]) -> "SearchTestResponseBodyBuilder":
        self._search_test_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "SearchTestResponseBodyBuilder":
        self._search_test_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "SearchTestResponseBodyBuilder":
        self._search_test_response_body.page_token = page_token
        return self

    def build(self) -> "SearchTestResponseBody":
        return self._search_test_response_body
