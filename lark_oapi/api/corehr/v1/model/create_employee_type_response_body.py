# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .employee_type import EmployeeType


class CreateEmployeeTypeResponseBody(object):
    _types = {
        "employee_type": EmployeeType,
    }

    def __init__(self, d):
        self.employee_type: Optional[EmployeeType] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateEmployeeTypeResponseBodyBuilder":
        return CreateEmployeeTypeResponseBodyBuilder()


class CreateEmployeeTypeResponseBodyBuilder(object):
    def __init__(self, create_employee_type_response_body: CreateEmployeeTypeResponseBody = CreateEmployeeTypeResponseBody({})) -> None:
        self._create_employee_type_response_body: CreateEmployeeTypeResponseBody = create_employee_type_response_body
    
    def employee_type(self, employee_type: EmployeeType) -> "CreateEmployeeTypeResponseBodyBuilder":
        self._create_employee_type_response_body.employee_type = employee_type
        return self
    
    def build(self) -> "CreateEmployeeTypeResponseBody":
        return self._create_employee_type_response_body