# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .lang_text import LangText


class LeaveEmployExpireRecord(object):
    _types = {
        "id": str,
        "employment_id": str,
        "leave_type_id": str,
        "granting_quantity": str,
        "left_granting_quantity": str,
        "granting_unit": int,
        "effective_date": str,
        "expiration_date": str,
        "reason": List[LangText],
        "is_update_by_external": bool,
        "accrual_source": int,
        "leave_sub_type_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.leave_type_id: Optional[str] = None
        self.granting_quantity: Optional[str] = None
        self.left_granting_quantity: Optional[str] = None
        self.granting_unit: Optional[int] = None
        self.effective_date: Optional[str] = None
        self.expiration_date: Optional[str] = None
        self.reason: Optional[List[LangText]] = None
        self.is_update_by_external: Optional[bool] = None
        self.accrual_source: Optional[int] = None
        self.leave_sub_type_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveEmployExpireRecordBuilder":
        return LeaveEmployExpireRecordBuilder()


class LeaveEmployExpireRecordBuilder(object):
    def __init__(self) -> None:
        self._leave_employ_expire_record = LeaveEmployExpireRecord()

    def id(self, id: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.id = id
        return self

    def employment_id(self, employment_id: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.employment_id = employment_id
        return self

    def leave_type_id(self, leave_type_id: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.leave_type_id = leave_type_id
        return self

    def granting_quantity(self, granting_quantity: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.granting_quantity = granting_quantity
        return self

    def left_granting_quantity(self, left_granting_quantity: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.left_granting_quantity = left_granting_quantity
        return self

    def granting_unit(self, granting_unit: int) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.granting_unit = granting_unit
        return self

    def effective_date(self, effective_date: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.effective_date = effective_date
        return self

    def expiration_date(self, expiration_date: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.expiration_date = expiration_date
        return self

    def reason(self, reason: List[LangText]) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.reason = reason
        return self

    def is_update_by_external(self, is_update_by_external: bool) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.is_update_by_external = is_update_by_external
        return self

    def accrual_source(self, accrual_source: int) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.accrual_source = accrual_source
        return self

    def leave_sub_type_id(self, leave_sub_type_id: str) -> "LeaveEmployExpireRecordBuilder":
        self._leave_employ_expire_record.leave_sub_type_id = leave_sub_type_id
        return self

    def build(self) -> "LeaveEmployExpireRecord":
        return self._leave_employ_expire_record
