# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class SearchCalendarRequestBody(object):
    _types = {
        "query": str,
    }

    def __init__(self, d):
        self.query: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchCalendarRequestBodyBuilder":
        return SearchCalendarRequestBodyBuilder()


class SearchCalendarRequestBodyBuilder(object):
    def __init__(self, search_calendar_request_body: SearchCalendarRequestBody = SearchCalendarRequestBody({})) -> None:
        self._search_calendar_request_body: SearchCalendarRequestBody = search_calendar_request_body
    
    def query(self, query: str) -> "SearchCalendarRequestBodyBuilder":
        self._search_calendar_request_body.query = query
        return self
    
    def build(self) -> "SearchCalendarRequestBody":
        return self._search_calendar_request_body