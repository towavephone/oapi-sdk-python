# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class LeftBorderStyle(object):
    _types = {
        "style": str,
        "color": str,
    }

    def __init__(self, d):
        self.style: Optional[str] = None
        self.color: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeftBorderStyleBuilder":
        return LeftBorderStyleBuilder()


class LeftBorderStyleBuilder(object):
    def __init__(self, left_border_style: LeftBorderStyle = LeftBorderStyle({})) -> None:
        self._left_border_style: LeftBorderStyle = left_border_style
    
    def style(self, style: str) -> "LeftBorderStyleBuilder":
        self._left_border_style.style = style
        return self
    
    def color(self, color: str) -> "LeftBorderStyleBuilder":
        self._left_border_style.color = color
        return self
    
    def build(self) -> "LeftBorderStyle":
        return self._left_border_style