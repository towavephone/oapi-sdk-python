# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .time_zone import TimeZone


class SearchBasicInfoTimeZoneResponseBody(object):
    _types = {
        "items": List[TimeZone],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[TimeZone]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchBasicInfoTimeZoneResponseBodyBuilder":
        return SearchBasicInfoTimeZoneResponseBodyBuilder()


class SearchBasicInfoTimeZoneResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_basic_info_time_zone_response_body = SearchBasicInfoTimeZoneResponseBody()

    def items(self, items: List[TimeZone]) -> "SearchBasicInfoTimeZoneResponseBodyBuilder":
        self._search_basic_info_time_zone_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchBasicInfoTimeZoneResponseBodyBuilder":
        self._search_basic_info_time_zone_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchBasicInfoTimeZoneResponseBodyBuilder":
        self._search_basic_info_time_zone_response_body.has_more = has_more
        return self

    def build(self) -> "SearchBasicInfoTimeZoneResponseBody":
        return self._search_basic_info_time_zone_response_body
