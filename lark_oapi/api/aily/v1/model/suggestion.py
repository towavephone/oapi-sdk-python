# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Suggestion(object):
    _types = {
        "content": str,
        "skill_id": str,
    }

    def __init__(self, d=None):
        self.content: Optional[str] = None
        self.skill_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SuggestionBuilder":
        return SuggestionBuilder()


class SuggestionBuilder(object):
    def __init__(self) -> None:
        self._suggestion = Suggestion()

    def content(self, content: str) -> "SuggestionBuilder":
        self._suggestion.content = content
        return self

    def skill_id(self, skill_id: str) -> "SuggestionBuilder":
        self._suggestion.skill_id = skill_id
        return self

    def build(self) -> "Suggestion":
        return self._suggestion
