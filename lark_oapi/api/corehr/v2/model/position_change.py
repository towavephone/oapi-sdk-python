# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .position_adjustment_info import PositionAdjustmentInfo


class PositionChange(object):
    _types = {
        "position_change_id": str,
        "position_id": str,
        "draft_position_id": str,
        "position_change_type": str,
        "position_adjustment_info": PositionAdjustmentInfo,
    }

    def __init__(self, d=None):
        self.position_change_id: Optional[str] = None
        self.position_id: Optional[str] = None
        self.draft_position_id: Optional[str] = None
        self.position_change_type: Optional[str] = None
        self.position_adjustment_info: Optional[PositionAdjustmentInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PositionChangeBuilder":
        return PositionChangeBuilder()


class PositionChangeBuilder(object):
    def __init__(self) -> None:
        self._position_change = PositionChange()

    def position_change_id(self, position_change_id: str) -> "PositionChangeBuilder":
        self._position_change.position_change_id = position_change_id
        return self

    def position_id(self, position_id: str) -> "PositionChangeBuilder":
        self._position_change.position_id = position_id
        return self

    def draft_position_id(self, draft_position_id: str) -> "PositionChangeBuilder":
        self._position_change.draft_position_id = draft_position_id
        return self

    def position_change_type(self, position_change_type: str) -> "PositionChangeBuilder":
        self._position_change.position_change_type = position_change_type
        return self

    def position_adjustment_info(self, position_adjustment_info: PositionAdjustmentInfo) -> "PositionChangeBuilder":
        self._position_change.position_adjustment_info = position_adjustment_info
        return self

    def build(self) -> "PositionChange":
        return self._position_change
