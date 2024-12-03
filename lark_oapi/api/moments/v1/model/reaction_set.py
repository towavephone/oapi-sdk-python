# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .reaction_list import ReactionList


class ReactionSet(object):
    _types = {
        "reactions": List[ReactionList],
        "total_count": int,
    }

    def __init__(self, d=None):
        self.reactions: Optional[List[ReactionList]] = None
        self.total_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReactionSetBuilder":
        return ReactionSetBuilder()


class ReactionSetBuilder(object):
    def __init__(self) -> None:
        self._reaction_set = ReactionSet()

    def reactions(self, reactions: List[ReactionList]) -> "ReactionSetBuilder":
        self._reaction_set.reactions = reactions
        return self

    def total_count(self, total_count: int) -> "ReactionSetBuilder":
        self._reaction_set.total_count = total_count
        return self

    def build(self) -> "ReactionSet":
        return self._reaction_set
