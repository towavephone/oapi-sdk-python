# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OrderCondition(object):
    _types = {
        "field": str,
        "direction": str,
    }

    def __init__(self, d=None):
        self.field: Optional[str] = None
        self.direction: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OrderConditionBuilder":
        return OrderConditionBuilder()


class OrderConditionBuilder(object):
    def __init__(self) -> None:
        self._order_condition = OrderCondition()

    def field(self, field: str) -> "OrderConditionBuilder":
        self._order_condition.field = field
        return self

    def direction(self, direction: str) -> "OrderConditionBuilder":
        self._order_condition.direction = direction
        return self

    def build(self) -> "OrderCondition":
        return self._order_condition
