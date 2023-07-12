# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class TableCell(object):
    _types = {
    }

    def __init__(self, d):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TableCellBuilder":
        return TableCellBuilder()


class TableCellBuilder(object):
    def __init__(self, table_cell: TableCell = TableCell({})) -> None:
        self._table_cell: TableCell = table_cell
    
    def build(self) -> "TableCell":
        return self._table_cell