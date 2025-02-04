# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LlmContent(object):
    _types = {
        "type": str,
        "content": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LlmContentBuilder":
        return LlmContentBuilder()


class LlmContentBuilder(object):
    def __init__(self) -> None:
        self._llm_content = LlmContent()

    def type(self, type: str) -> "LlmContentBuilder":
        self._llm_content.type = type
        return self

    def content(self, content: str) -> "LlmContentBuilder":
        self._llm_content.content = content
        return self

    def build(self) -> "LlmContent":
        return self._llm_content
