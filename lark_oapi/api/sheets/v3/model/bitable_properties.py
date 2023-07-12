# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class BitableProperties(object):
    _types = {
        "bitable_token": str,
        "table_id": str,
    }

    def __init__(self, d):
        self.bitable_token: Optional[str] = None
        self.table_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitablePropertiesBuilder":
        return BitablePropertiesBuilder()


class BitablePropertiesBuilder(object):
    def __init__(self, bitable_properties: BitableProperties = BitableProperties({})) -> None:
        self._bitable_properties: BitableProperties = bitable_properties
    
    def bitable_token(self, bitable_token: str) -> "BitablePropertiesBuilder":
        self._bitable_properties.bitable_token = bitable_token
        return self
    
    def table_id(self, table_id: str) -> "BitablePropertiesBuilder":
        self._bitable_properties.table_id = table_id
        return self
    
    def build(self) -> "BitableProperties":
        return self._bitable_properties