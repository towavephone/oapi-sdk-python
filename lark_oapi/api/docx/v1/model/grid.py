# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Grid(object):
    _types = {
        "column_size": int,
    }

    def __init__(self, d):
        self.column_size: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GridBuilder":
        return GridBuilder()


class GridBuilder(object):
    def __init__(self, grid: Grid = Grid({})) -> None:
        self._grid: Grid = grid
    
    def column_size(self, column_size: int) -> "GridBuilder":
        self._grid.column_size = column_size
        return self
    
    def build(self) -> "Grid":
        return self._grid