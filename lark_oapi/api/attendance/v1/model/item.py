# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .child_item import ChildItem


class Item(object):
    _types = {
        "code": str,
        "title": str,
        "child_items": List[ChildItem],
    }

    def __init__(self, d):
        self.code: Optional[str] = None
        self.title: Optional[str] = None
        self.child_items: Optional[List[ChildItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ItemBuilder":
        return ItemBuilder()


class ItemBuilder(object):
    def __init__(self, item: Item = Item({})) -> None:
        self._item: Item = item
    
    def code(self, code: str) -> "ItemBuilder":
        self._item.code = code
        return self
    
    def title(self, title: str) -> "ItemBuilder":
        self._item.title = title
        return self
    
    def child_items(self, child_items: List[ChildItem]) -> "ItemBuilder":
        self._item.child_items = child_items
        return self
    
    def build(self) -> "Item":
        return self._item