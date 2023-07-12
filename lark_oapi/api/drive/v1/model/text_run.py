# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class TextRun(object):
    _types = {
        "text": str,
    }

    def __init__(self, d):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TextRunBuilder":
        return TextRunBuilder()


class TextRunBuilder(object):
    def __init__(self, text_run: TextRun = TextRun({})) -> None:
        self._text_run: TextRun = text_run
    
    def text(self, text: str) -> "TextRunBuilder":
        self._text_run.text = text
        return self
    
    def build(self) -> "TextRun":
        return self._text_run