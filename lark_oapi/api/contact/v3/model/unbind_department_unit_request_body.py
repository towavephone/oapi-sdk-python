# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class UnbindDepartmentUnitRequestBody(object):
    _types = {
        "unit_id": str,
        "department_id": str,
        "department_id_type": str,
    }

    def __init__(self, d):
        self.unit_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.department_id_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UnbindDepartmentUnitRequestBodyBuilder":
        return UnbindDepartmentUnitRequestBodyBuilder()


class UnbindDepartmentUnitRequestBodyBuilder(object):
    def __init__(self, unbind_department_unit_request_body: UnbindDepartmentUnitRequestBody = UnbindDepartmentUnitRequestBody({})) -> None:
        self._unbind_department_unit_request_body: UnbindDepartmentUnitRequestBody = unbind_department_unit_request_body
    
    def unit_id(self, unit_id: str) -> "UnbindDepartmentUnitRequestBodyBuilder":
        self._unbind_department_unit_request_body.unit_id = unit_id
        return self
    
    def department_id(self, department_id: str) -> "UnbindDepartmentUnitRequestBodyBuilder":
        self._unbind_department_unit_request_body.department_id = department_id
        return self
    
    def department_id_type(self, department_id_type: str) -> "UnbindDepartmentUnitRequestBodyBuilder":
        self._unbind_department_unit_request_body.department_id_type = department_id_type
        return self
    
    def build(self) -> "UnbindDepartmentUnitRequestBody":
        return self._unbind_department_unit_request_body