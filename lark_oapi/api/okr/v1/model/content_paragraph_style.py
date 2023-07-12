# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .content_list import ContentList


class ContentParagraphStyle(object):
    _types = {
        "list": ContentList,
    }

    def __init__(self, d):
        self.list: Optional[ContentList] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ContentParagraphStyleBuilder":
        return ContentParagraphStyleBuilder()


class ContentParagraphStyleBuilder(object):
    def __init__(self, content_paragraph_style: ContentParagraphStyle = ContentParagraphStyle({})) -> None:
        self._content_paragraph_style: ContentParagraphStyle = content_paragraph_style
    
    def list(self, list: ContentList) -> "ContentParagraphStyleBuilder":
        self._content_paragraph_style.list = list
        return self
    
    def build(self) -> "ContentParagraphStyle":
        return self._content_paragraph_style