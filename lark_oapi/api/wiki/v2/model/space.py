# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Space(object):
    _types = {
        "name": str,
        "description": str,
        "space_id": str,
        "space_type": str,
        "visibility": str,
        "open_sharing": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.space_id: Optional[str] = None
        self.space_type: Optional[str] = None
        self.visibility: Optional[str] = None
        self.open_sharing: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SpaceBuilder":
        return SpaceBuilder()


class SpaceBuilder(object):
    def __init__(self) -> None:
        self._space = Space()

    def name(self, name: str) -> "SpaceBuilder":
        self._space.name = name
        return self

    def description(self, description: str) -> "SpaceBuilder":
        self._space.description = description
        return self

    def space_id(self, space_id: str) -> "SpaceBuilder":
        self._space.space_id = space_id
        return self

    def space_type(self, space_type: str) -> "SpaceBuilder":
        self._space.space_type = space_type
        return self

    def visibility(self, visibility: str) -> "SpaceBuilder":
        self._space.visibility = visibility
        return self

    def open_sharing(self, open_sharing: str) -> "SpaceBuilder":
        self._space.open_sharing = open_sharing
        return self

    def build(self) -> "Space":
        return self._space
