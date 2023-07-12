# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .text_style import TextStyle
from .text_element import TextElement


class Text(object):
    _types = {
        "style": TextStyle,
        "elements": List[TextElement],
    }

    def __init__(self, d):
        self.style: Optional[TextStyle] = None
        self.elements: Optional[List[TextElement]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TextBuilder":
        return TextBuilder()


class TextBuilder(object):
    def __init__(self, text: Text = Text({})) -> None:
        self._text: Text = text
    
    def style(self, style: TextStyle) -> "TextBuilder":
        self._text.style = style
        return self
    
    def elements(self, elements: List[TextElement]) -> "TextBuilder":
        self._text.elements = elements
        return self
    
    def build(self) -> "Text":
        return self._text