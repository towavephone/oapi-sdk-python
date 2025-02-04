# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Status(object):
    _types = {
        "from_status": str,
        "to_status": str,
    }

    def __init__(self, d=None):
        self.from_status: Optional[str] = None
        self.to_status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "StatusBuilder":
        return StatusBuilder()


class StatusBuilder(object):
    def __init__(self) -> None:
        self._status = Status()

    def from_status(self, from_status: str) -> "StatusBuilder":
        self._status.from_status = from_status
        return self

    def to_status(self, to_status: str) -> "StatusBuilder":
        self._status.to_status = to_status
        return self

    def build(self) -> "Status":
        return self._status
