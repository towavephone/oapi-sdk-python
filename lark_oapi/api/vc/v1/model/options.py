# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Options(object):
    _types = {
        "text": str,
        "key": str,
        "is_other": bool,
    }

    def __init__(self, d):
        self.text: Optional[str] = None
        self.key: Optional[str] = None
        self.is_other: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OptionsBuilder":
        return OptionsBuilder()


class OptionsBuilder(object):
    def __init__(self, options: Options = Options({})) -> None:
        self._options: Options = options
    
    def text(self, text: str) -> "OptionsBuilder":
        self._options.text = text
        return self
    
    def key(self, key: str) -> "OptionsBuilder":
        self._options.key = key
        return self
    
    def is_other(self, is_other: bool) -> "OptionsBuilder":
        self._options.is_other = is_other
        return self
    
    def build(self) -> "Options":
        return self._options