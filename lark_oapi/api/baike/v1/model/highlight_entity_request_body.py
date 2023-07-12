# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class HighlightEntityRequestBody(object):
    _types = {
        "text": str,
    }

    def __init__(self, d):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "HighlightEntityRequestBodyBuilder":
        return HighlightEntityRequestBodyBuilder()


class HighlightEntityRequestBodyBuilder(object):
    def __init__(self, highlight_entity_request_body: HighlightEntityRequestBody = HighlightEntityRequestBody({})) -> None:
        self._highlight_entity_request_body: HighlightEntityRequestBody = highlight_entity_request_body
    
    def text(self, text: str) -> "HighlightEntityRequestBodyBuilder":
        self._highlight_entity_request_body.text = text
        return self
    
    def build(self) -> "HighlightEntityRequestBody":
        return self._highlight_entity_request_body