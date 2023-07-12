# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class SheetProperties(object):
    _types = {
        "row_count": int,
        "column_count": int,
        "frozen_row_count": int,
        "frozen_column_count": int,
    }

    def __init__(self, d):
        self.row_count: Optional[int] = None
        self.column_count: Optional[int] = None
        self.frozen_row_count: Optional[int] = None
        self.frozen_column_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SheetPropertiesBuilder":
        return SheetPropertiesBuilder()


class SheetPropertiesBuilder(object):
    def __init__(self, sheet_properties: SheetProperties = SheetProperties({})) -> None:
        self._sheet_properties: SheetProperties = sheet_properties
    
    def row_count(self, row_count: int) -> "SheetPropertiesBuilder":
        self._sheet_properties.row_count = row_count
        return self
    
    def column_count(self, column_count: int) -> "SheetPropertiesBuilder":
        self._sheet_properties.column_count = column_count
        return self
    
    def frozen_row_count(self, frozen_row_count: int) -> "SheetPropertiesBuilder":
        self._sheet_properties.frozen_row_count = frozen_row_count
        return self
    
    def frozen_column_count(self, frozen_column_count: int) -> "SheetPropertiesBuilder":
        self._sheet_properties.frozen_column_count = frozen_column_count
        return self
    
    def build(self) -> "SheetProperties":
        return self._sheet_properties