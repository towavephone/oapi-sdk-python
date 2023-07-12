# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .department import Department


class CreateDepartmentResponseBody(object):
    _types = {
        "department": Department,
    }

    def __init__(self, d):
        self.department: Optional[Department] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateDepartmentResponseBodyBuilder":
        return CreateDepartmentResponseBodyBuilder()


class CreateDepartmentResponseBodyBuilder(object):
    def __init__(self, create_department_response_body: CreateDepartmentResponseBody = CreateDepartmentResponseBody({})) -> None:
        self._create_department_response_body: CreateDepartmentResponseBody = create_department_response_body
    
    def department(self, department: Department) -> "CreateDepartmentResponseBodyBuilder":
        self._create_department_response_body.department = department
        return self
    
    def build(self) -> "CreateDepartmentResponseBody":
        return self._create_department_response_body