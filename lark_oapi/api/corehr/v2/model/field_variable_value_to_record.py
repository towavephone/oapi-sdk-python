# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FieldVariableValueToRecord(object):
    _types = {
        "variable_api_name": str,
        "sub_value_key": str,
    }

    def __init__(self, d=None):
        self.variable_api_name: Optional[str] = None
        self.sub_value_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FieldVariableValueToRecordBuilder":
        return FieldVariableValueToRecordBuilder()


class FieldVariableValueToRecordBuilder(object):
    def __init__(self) -> None:
        self._field_variable_value_to_record = FieldVariableValueToRecord()

    def variable_api_name(self, variable_api_name: str) -> "FieldVariableValueToRecordBuilder":
        self._field_variable_value_to_record.variable_api_name = variable_api_name
        return self

    def sub_value_key(self, sub_value_key: str) -> "FieldVariableValueToRecordBuilder":
        self._field_variable_value_to_record.sub_value_key = sub_value_key
        return self

    def build(self) -> "FieldVariableValueToRecord":
        return self._field_variable_value_to_record
