# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .access_data import AccessData


class BlockAccessData(object):
    _types = {
        "date": str,
        "block_id": str,
        "access_data": AccessData,
    }

    def __init__(self, d):
        self.date: Optional[str] = None
        self.block_id: Optional[str] = None
        self.access_data: Optional[AccessData] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BlockAccessDataBuilder":
        return BlockAccessDataBuilder()


class BlockAccessDataBuilder(object):
    def __init__(self, block_access_data: BlockAccessData = BlockAccessData({})) -> None:
        self._block_access_data: BlockAccessData = block_access_data
    
    def date(self, date: str) -> "BlockAccessDataBuilder":
        self._block_access_data.date = date
        return self
    
    def block_id(self, block_id: str) -> "BlockAccessDataBuilder":
        self._block_access_data.block_id = block_id
        return self
    
    def access_data(self, access_data: AccessData) -> "BlockAccessDataBuilder":
        self._block_access_data.access_data = access_data
        return self
    
    def build(self) -> "BlockAccessData":
        return self._block_access_data