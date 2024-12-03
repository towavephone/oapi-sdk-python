# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class RecordQueryOption(object):
    _types = {
        "stringify_number": bool,
        "normalize_column_name": bool,
    }

    def __init__(self, d=None):
        self.stringify_number: Optional[bool] = None
        self.normalize_column_name: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecordQueryOptionBuilder":
        return RecordQueryOptionBuilder()


class RecordQueryOptionBuilder(object):
    def __init__(self) -> None:
        self._record_query_option = RecordQueryOption()

    def stringify_number(self, stringify_number: bool) -> "RecordQueryOptionBuilder":
        self._record_query_option.stringify_number = stringify_number
        return self

    def normalize_column_name(self, normalize_column_name: bool) -> "RecordQueryOptionBuilder":
        self._record_query_option.normalize_column_name = normalize_column_name
        return self

    def build(self) -> "RecordQueryOption":
        return self._record_query_option
