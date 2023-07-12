# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .bitable_table_record_action_field_identity import BitableTableRecordActionFieldIdentity


class BitableTableRecordActionField(object):
    _types = {
        "field_id": str,
        "field_value": str,
        "field_identity_value": BitableTableRecordActionFieldIdentity,
    }

    def __init__(self, d):
        self.field_id: Optional[str] = None
        self.field_value: Optional[str] = None
        self.field_identity_value: Optional[BitableTableRecordActionFieldIdentity] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitableTableRecordActionFieldBuilder":
        return BitableTableRecordActionFieldBuilder()


class BitableTableRecordActionFieldBuilder(object):
    def __init__(self, bitable_table_record_action_field: BitableTableRecordActionField = BitableTableRecordActionField({})) -> None:
        self._bitable_table_record_action_field: BitableTableRecordActionField = bitable_table_record_action_field
    
    def field_id(self, field_id: str) -> "BitableTableRecordActionFieldBuilder":
        self._bitable_table_record_action_field.field_id = field_id
        return self
    
    def field_value(self, field_value: str) -> "BitableTableRecordActionFieldBuilder":
        self._bitable_table_record_action_field.field_value = field_value
        return self
    
    def field_identity_value(self, field_identity_value: BitableTableRecordActionFieldIdentity) -> "BitableTableRecordActionFieldBuilder":
        self._bitable_table_record_action_field.field_identity_value = field_identity_value
        return self
    
    def build(self) -> "BitableTableRecordActionField":
        return self._bitable_table_record_action_field