# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .span import Span


class Phrase(object):
    _types = {
        "name": str,
        "entity_ids": List[str],
        "span": Span,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.entity_ids: Optional[List[str]] = None
        self.span: Optional[Span] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PhraseBuilder":
        return PhraseBuilder()


class PhraseBuilder(object):
    def __init__(self, phrase: Phrase = Phrase({})) -> None:
        self._phrase: Phrase = phrase
    
    def name(self, name: str) -> "PhraseBuilder":
        self._phrase.name = name
        return self
    
    def entity_ids(self, entity_ids: List[str]) -> "PhraseBuilder":
        self._phrase.entity_ids = entity_ids
        return self
    
    def span(self, span: Span) -> "PhraseBuilder":
        self._phrase.span = span
        return self
    
    def build(self) -> "Phrase":
        return self._phrase