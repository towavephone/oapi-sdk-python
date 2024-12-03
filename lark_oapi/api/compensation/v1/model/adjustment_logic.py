# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .formula import Formula


class AdjustmentLogic(object):
    _types = {
        "fixed": str,
        "formula": Formula,
    }

    def __init__(self, d=None):
        self.fixed: Optional[str] = None
        self.formula: Optional[Formula] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AdjustmentLogicBuilder":
        return AdjustmentLogicBuilder()


class AdjustmentLogicBuilder(object):
    def __init__(self) -> None:
        self._adjustment_logic = AdjustmentLogic()

    def fixed(self, fixed: str) -> "AdjustmentLogicBuilder":
        self._adjustment_logic.fixed = fixed
        return self

    def formula(self, formula: Formula) -> "AdjustmentLogicBuilder":
        self._adjustment_logic.formula = formula
        return self

    def build(self) -> "AdjustmentLogic":
        return self._adjustment_logic
