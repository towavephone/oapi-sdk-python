# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .classification import Classification


class ListClassificationResponseBody(object):
    _types = {
        "items": List[Classification],
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[Classification]] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListClassificationResponseBodyBuilder":
        return ListClassificationResponseBodyBuilder()


class ListClassificationResponseBodyBuilder(object):
    def __init__(self, list_classification_response_body: ListClassificationResponseBody = ListClassificationResponseBody({})) -> None:
        self._list_classification_response_body: ListClassificationResponseBody = list_classification_response_body
    
    def items(self, items: List[Classification]) -> "ListClassificationResponseBodyBuilder":
        self._list_classification_response_body.items = items
        return self
    
    def page_token(self, page_token: str) -> "ListClassificationResponseBodyBuilder":
        self._list_classification_response_body.page_token = page_token
        return self
    
    def build(self) -> "ListClassificationResponseBody":
        return self._list_classification_response_body