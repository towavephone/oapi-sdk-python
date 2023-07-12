# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .unit_department import UnitDepartment


class ListDepartmentUnitResponseBody(object):
    _types = {
        "departmentlist": List[UnitDepartment],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d):
        self.departmentlist: Optional[List[UnitDepartment]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListDepartmentUnitResponseBodyBuilder":
        return ListDepartmentUnitResponseBodyBuilder()


class ListDepartmentUnitResponseBodyBuilder(object):
    def __init__(self, list_department_unit_response_body: ListDepartmentUnitResponseBody = ListDepartmentUnitResponseBody({})) -> None:
        self._list_department_unit_response_body: ListDepartmentUnitResponseBody = list_department_unit_response_body
    
    def departmentlist(self, departmentlist: List[UnitDepartment]) -> "ListDepartmentUnitResponseBodyBuilder":
        self._list_department_unit_response_body.departmentlist = departmentlist
        return self
    
    def has_more(self, has_more: bool) -> "ListDepartmentUnitResponseBodyBuilder":
        self._list_department_unit_response_body.has_more = has_more
        return self
    
    def page_token(self, page_token: str) -> "ListDepartmentUnitResponseBodyBuilder":
        self._list_department_unit_response_body.page_token = page_token
        return self
    
    def build(self) -> "ListDepartmentUnitResponseBody":
        return self._list_department_unit_response_body