# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .flexible_rule import FlexibleRule
from .punch_time_rule import PunchTimeRule
from .late_off_late_on_rule import LateOffLateOnRule
from .rest_rule import RestRule
from .overtime_rule import OvertimeRule


class Shift(object):
    _types = {
        "shift_id": str,
        "shift_name": str,
        "punch_times": int,
        "is_flexible": bool,
        "flexible_minutes": int,
        "flexible_rule": List[FlexibleRule],
        "no_need_off": bool,
        "punch_time_rule": List[PunchTimeRule],
        "late_off_late_on_rule": List[LateOffLateOnRule],
        "rest_time_rule": List[RestRule],
        "overtime_rule": List[OvertimeRule],
    }

    def __init__(self, d):
        self.shift_id: Optional[str] = None
        self.shift_name: Optional[str] = None
        self.punch_times: Optional[int] = None
        self.is_flexible: Optional[bool] = None
        self.flexible_minutes: Optional[int] = None
        self.flexible_rule: Optional[List[FlexibleRule]] = None
        self.no_need_off: Optional[bool] = None
        self.punch_time_rule: Optional[List[PunchTimeRule]] = None
        self.late_off_late_on_rule: Optional[List[LateOffLateOnRule]] = None
        self.rest_time_rule: Optional[List[RestRule]] = None
        self.overtime_rule: Optional[List[OvertimeRule]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ShiftBuilder":
        return ShiftBuilder()


class ShiftBuilder(object):
    def __init__(self, shift: Shift = Shift({})) -> None:
        self._shift: Shift = shift
    
    def shift_id(self, shift_id: str) -> "ShiftBuilder":
        self._shift.shift_id = shift_id
        return self
    
    def shift_name(self, shift_name: str) -> "ShiftBuilder":
        self._shift.shift_name = shift_name
        return self
    
    def punch_times(self, punch_times: int) -> "ShiftBuilder":
        self._shift.punch_times = punch_times
        return self
    
    def is_flexible(self, is_flexible: bool) -> "ShiftBuilder":
        self._shift.is_flexible = is_flexible
        return self
    
    def flexible_minutes(self, flexible_minutes: int) -> "ShiftBuilder":
        self._shift.flexible_minutes = flexible_minutes
        return self
    
    def flexible_rule(self, flexible_rule: List[FlexibleRule]) -> "ShiftBuilder":
        self._shift.flexible_rule = flexible_rule
        return self
    
    def no_need_off(self, no_need_off: bool) -> "ShiftBuilder":
        self._shift.no_need_off = no_need_off
        return self
    
    def punch_time_rule(self, punch_time_rule: List[PunchTimeRule]) -> "ShiftBuilder":
        self._shift.punch_time_rule = punch_time_rule
        return self
    
    def late_off_late_on_rule(self, late_off_late_on_rule: List[LateOffLateOnRule]) -> "ShiftBuilder":
        self._shift.late_off_late_on_rule = late_off_late_on_rule
        return self
    
    def rest_time_rule(self, rest_time_rule: List[RestRule]) -> "ShiftBuilder":
        self._shift.rest_time_rule = rest_time_rule
        return self
    
    def overtime_rule(self, overtime_rule: List[OvertimeRule]) -> "ShiftBuilder":
        self._shift.overtime_rule = overtime_rule
        return self
    
    def build(self) -> "Shift":
        return self._shift