# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class LeaveGrantingRecord(object):
    _types = {
        "id": str,
        "employment_id": str,
        "leave_type_id": str,
        "granting_quantity": str,
        "granting_unit": int,
        "effective_date": str,
        "expiration_date": str,
        "granted_by": int,
        "reason": List[I18n],
        "created_at": str,
        "created_by": str,
        "updated_at": str,
        "updated_by": str,
        "section_type": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.employment_id: Optional[str] = None
        self.leave_type_id: Optional[str] = None
        self.granting_quantity: Optional[str] = None
        self.granting_unit: Optional[int] = None
        self.effective_date: Optional[str] = None
        self.expiration_date: Optional[str] = None
        self.granted_by: Optional[int] = None
        self.reason: Optional[List[I18n]] = None
        self.created_at: Optional[str] = None
        self.created_by: Optional[str] = None
        self.updated_at: Optional[str] = None
        self.updated_by: Optional[str] = None
        self.section_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveGrantingRecordBuilder":
        return LeaveGrantingRecordBuilder()


class LeaveGrantingRecordBuilder(object):
    def __init__(self) -> None:
        self._leave_granting_record = LeaveGrantingRecord()

    def id(self, id: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.id = id
        return self

    def employment_id(self, employment_id: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.employment_id = employment_id
        return self

    def leave_type_id(self, leave_type_id: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.leave_type_id = leave_type_id
        return self

    def granting_quantity(self, granting_quantity: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.granting_quantity = granting_quantity
        return self

    def granting_unit(self, granting_unit: int) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.granting_unit = granting_unit
        return self

    def effective_date(self, effective_date: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.effective_date = effective_date
        return self

    def expiration_date(self, expiration_date: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.expiration_date = expiration_date
        return self

    def granted_by(self, granted_by: int) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.granted_by = granted_by
        return self

    def reason(self, reason: List[I18n]) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.reason = reason
        return self

    def created_at(self, created_at: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.created_at = created_at
        return self

    def created_by(self, created_by: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.created_by = created_by
        return self

    def updated_at(self, updated_at: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.updated_at = updated_at
        return self

    def updated_by(self, updated_by: str) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.updated_by = updated_by
        return self

    def section_type(self, section_type: int) -> "LeaveGrantingRecordBuilder":
        self._leave_granting_record.section_type = section_type
        return self

    def build(self) -> "LeaveGrantingRecord":
        return self._leave_granting_record
