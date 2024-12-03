# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .website_job_post import WebsiteJobPost


class SearchWebsiteJobPostResponseBody(object):
    _types = {
        "items": List[WebsiteJobPost],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[WebsiteJobPost]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchWebsiteJobPostResponseBodyBuilder":
        return SearchWebsiteJobPostResponseBodyBuilder()


class SearchWebsiteJobPostResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_website_job_post_response_body = SearchWebsiteJobPostResponseBody()

    def items(self, items: List[WebsiteJobPost]) -> "SearchWebsiteJobPostResponseBodyBuilder":
        self._search_website_job_post_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "SearchWebsiteJobPostResponseBodyBuilder":
        self._search_website_job_post_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "SearchWebsiteJobPostResponseBodyBuilder":
        self._search_website_job_post_response_body.page_token = page_token
        return self

    def build(self) -> "SearchWebsiteJobPostResponseBody":
        return self._search_website_job_post_response_body
