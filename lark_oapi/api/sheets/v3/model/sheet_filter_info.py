# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .filter_info import FilterInfo


class SheetFilterInfo(object):
    _types = {
        "range": str,
        "filtered_out_rows": List[int],
        "filter_infos": List[FilterInfo],
    }

    def __init__(self, d):
        self.range: Optional[str] = None
        self.filtered_out_rows: Optional[List[int]] = None
        self.filter_infos: Optional[List[FilterInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SheetFilterInfoBuilder":
        return SheetFilterInfoBuilder()


class SheetFilterInfoBuilder(object):
    def __init__(self, sheet_filter_info: SheetFilterInfo = SheetFilterInfo({})) -> None:
        self._sheet_filter_info: SheetFilterInfo = sheet_filter_info
    
    def range(self, range: str) -> "SheetFilterInfoBuilder":
        self._sheet_filter_info.range = range
        return self
    
    def filtered_out_rows(self, filtered_out_rows: List[int]) -> "SheetFilterInfoBuilder":
        self._sheet_filter_info.filtered_out_rows = filtered_out_rows
        return self
    
    def filter_infos(self, filter_infos: List[FilterInfo]) -> "SheetFilterInfoBuilder":
        self._sheet_filter_info.filter_infos = filter_infos
        return self
    
    def build(self) -> "SheetFilterInfo":
        return self._sheet_filter_info