# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .employee_type_enum import EmployeeTypeEnum


class UpdateEmployeeTypeEnumResponseBody(object):
    _types = {
        "employee_type_enum": EmployeeTypeEnum,
    }

    def __init__(self, d):
        self.employee_type_enum: Optional[EmployeeTypeEnum] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateEmployeeTypeEnumResponseBodyBuilder":
        return UpdateEmployeeTypeEnumResponseBodyBuilder()


class UpdateEmployeeTypeEnumResponseBodyBuilder(object):
    def __init__(self, update_employee_type_enum_response_body: UpdateEmployeeTypeEnumResponseBody = UpdateEmployeeTypeEnumResponseBody({})) -> None:
        self._update_employee_type_enum_response_body: UpdateEmployeeTypeEnumResponseBody = update_employee_type_enum_response_body
    
    def employee_type_enum(self, employee_type_enum: EmployeeTypeEnum) -> "UpdateEmployeeTypeEnumResponseBodyBuilder":
        self._update_employee_type_enum_response_body.employee_type_enum = employee_type_enum
        return self
    
    def build(self) -> "UpdateEmployeeTypeEnumResponseBody":
        return self._update_employee_type_enum_response_body