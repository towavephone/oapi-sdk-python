# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .block_i18n_info import BlockI18nInfo


class DocsBlock(object):
    _types = {
        "block_type_id": str,
        "i18n": List[BlockI18nInfo],
        "mobile_icon_url": str,
        "pc_icon_url": str,
    }

    def __init__(self, d):
        self.block_type_id: Optional[str] = None
        self.i18n: Optional[List[BlockI18nInfo]] = None
        self.mobile_icon_url: Optional[str] = None
        self.pc_icon_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocsBlockBuilder":
        return DocsBlockBuilder()


class DocsBlockBuilder(object):
    def __init__(self, docs_block: DocsBlock = DocsBlock({})) -> None:
        self._docs_block: DocsBlock = docs_block
    
    def block_type_id(self, block_type_id: str) -> "DocsBlockBuilder":
        self._docs_block.block_type_id = block_type_id
        return self
    
    def i18n(self, i18n: List[BlockI18nInfo]) -> "DocsBlockBuilder":
        self._docs_block.i18n = i18n
        return self
    
    def mobile_icon_url(self, mobile_icon_url: str) -> "DocsBlockBuilder":
        self._docs_block.mobile_icon_url = mobile_icon_url
        return self
    
    def pc_icon_url(self, pc_icon_url: str) -> "DocsBlockBuilder":
        self._docs_block.pc_icon_url = pc_icon_url
        return self
    
    def build(self) -> "DocsBlock":
        return self._docs_block