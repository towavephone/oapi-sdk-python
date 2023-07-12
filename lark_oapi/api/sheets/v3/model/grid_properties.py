# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class GridProperties(object):
    _types = {
        "frozen_row_count": int,
        "frozen_column_count": int,
        "row_count": int,
        "column_count": int,
    }

    def __init__(self, d):
        self.frozen_row_count: Optional[int] = None
        self.frozen_column_count: Optional[int] = None
        self.row_count: Optional[int] = None
        self.column_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GridPropertiesBuilder":
        return GridPropertiesBuilder()


class GridPropertiesBuilder(object):
    def __init__(self, grid_properties: GridProperties = GridProperties({})) -> None:
        self._grid_properties: GridProperties = grid_properties
    
    def frozen_row_count(self, frozen_row_count: int) -> "GridPropertiesBuilder":
        self._grid_properties.frozen_row_count = frozen_row_count
        return self
    
    def frozen_column_count(self, frozen_column_count: int) -> "GridPropertiesBuilder":
        self._grid_properties.frozen_column_count = frozen_column_count
        return self
    
    def row_count(self, row_count: int) -> "GridPropertiesBuilder":
        self._grid_properties.row_count = row_count
        return self
    
    def column_count(self, column_count: int) -> "GridPropertiesBuilder":
        self._grid_properties.column_count = column_count
        return self
    
    def build(self) -> "GridProperties":
        return self._grid_properties