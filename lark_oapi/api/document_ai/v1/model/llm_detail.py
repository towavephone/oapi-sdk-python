# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .llm_usage import LlmUsage


class LlmDetail(object):
    _types = {
        "query_id": int,
        "usage": LlmUsage,
        "finish_reason": str,
    }

    def __init__(self, d=None):
        self.query_id: Optional[int] = None
        self.usage: Optional[LlmUsage] = None
        self.finish_reason: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LlmDetailBuilder":
        return LlmDetailBuilder()


class LlmDetailBuilder(object):
    def __init__(self) -> None:
        self._llm_detail = LlmDetail()

    def query_id(self, query_id: int) -> "LlmDetailBuilder":
        self._llm_detail.query_id = query_id
        return self

    def usage(self, usage: LlmUsage) -> "LlmDetailBuilder":
        self._llm_detail.usage = usage
        return self

    def finish_reason(self, finish_reason: str) -> "LlmDetailBuilder":
        self._llm_detail.finish_reason = finish_reason
        return self

    def build(self) -> "LlmDetail":
        return self._llm_detail
