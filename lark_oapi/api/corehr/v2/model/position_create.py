# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .custom_field_data import CustomFieldData


class PositionCreate(object):
    _types = {
        "code": str,
        "names": List[I18n],
        "descriptions": List[I18n],
        "job_family_ids": List[str],
        "cost_center_id": str,
        "job_id": str,
        "job_level_ids": List[str],
        "employee_type_ids": List[str],
        "job_grade_ids": List[str],
        "work_location_ids": List[str],
        "working_hours_type_id": str,
        "department_id": str,
        "direct_leader_id": str,
        "dotted_line_leader_id": str,
        "is_key_position": bool,
        "effective_time": str,
        "custom_fields": List[CustomFieldData],
    }

    def __init__(self, d=None):
        self.code: Optional[str] = None
        self.names: Optional[List[I18n]] = None
        self.descriptions: Optional[List[I18n]] = None
        self.job_family_ids: Optional[List[str]] = None
        self.cost_center_id: Optional[str] = None
        self.job_id: Optional[str] = None
        self.job_level_ids: Optional[List[str]] = None
        self.employee_type_ids: Optional[List[str]] = None
        self.job_grade_ids: Optional[List[str]] = None
        self.work_location_ids: Optional[List[str]] = None
        self.working_hours_type_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.direct_leader_id: Optional[str] = None
        self.dotted_line_leader_id: Optional[str] = None
        self.is_key_position: Optional[bool] = None
        self.effective_time: Optional[str] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PositionCreateBuilder":
        return PositionCreateBuilder()


class PositionCreateBuilder(object):
    def __init__(self) -> None:
        self._position_create = PositionCreate()

    def code(self, code: str) -> "PositionCreateBuilder":
        self._position_create.code = code
        return self

    def names(self, names: List[I18n]) -> "PositionCreateBuilder":
        self._position_create.names = names
        return self

    def descriptions(self, descriptions: List[I18n]) -> "PositionCreateBuilder":
        self._position_create.descriptions = descriptions
        return self

    def job_family_ids(self, job_family_ids: List[str]) -> "PositionCreateBuilder":
        self._position_create.job_family_ids = job_family_ids
        return self

    def cost_center_id(self, cost_center_id: str) -> "PositionCreateBuilder":
        self._position_create.cost_center_id = cost_center_id
        return self

    def job_id(self, job_id: str) -> "PositionCreateBuilder":
        self._position_create.job_id = job_id
        return self

    def job_level_ids(self, job_level_ids: List[str]) -> "PositionCreateBuilder":
        self._position_create.job_level_ids = job_level_ids
        return self

    def employee_type_ids(self, employee_type_ids: List[str]) -> "PositionCreateBuilder":
        self._position_create.employee_type_ids = employee_type_ids
        return self

    def job_grade_ids(self, job_grade_ids: List[str]) -> "PositionCreateBuilder":
        self._position_create.job_grade_ids = job_grade_ids
        return self

    def work_location_ids(self, work_location_ids: List[str]) -> "PositionCreateBuilder":
        self._position_create.work_location_ids = work_location_ids
        return self

    def working_hours_type_id(self, working_hours_type_id: str) -> "PositionCreateBuilder":
        self._position_create.working_hours_type_id = working_hours_type_id
        return self

    def department_id(self, department_id: str) -> "PositionCreateBuilder":
        self._position_create.department_id = department_id
        return self

    def direct_leader_id(self, direct_leader_id: str) -> "PositionCreateBuilder":
        self._position_create.direct_leader_id = direct_leader_id
        return self

    def dotted_line_leader_id(self, dotted_line_leader_id: str) -> "PositionCreateBuilder":
        self._position_create.dotted_line_leader_id = dotted_line_leader_id
        return self

    def is_key_position(self, is_key_position: bool) -> "PositionCreateBuilder":
        self._position_create.is_key_position = is_key_position
        return self

    def effective_time(self, effective_time: str) -> "PositionCreateBuilder":
        self._position_create.effective_time = effective_time
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "PositionCreateBuilder":
        self._position_create.custom_fields = custom_fields
        return self

    def build(self) -> "PositionCreate":
        return self._position_create
