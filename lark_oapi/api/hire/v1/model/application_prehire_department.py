# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ApplicationPrehireDepartment(object):
    _types = {
        "id": str,
        "name": str,
        "en_name": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplicationPrehireDepartmentBuilder":
        return ApplicationPrehireDepartmentBuilder()


class ApplicationPrehireDepartmentBuilder(object):
    def __init__(self, application_prehire_department: ApplicationPrehireDepartment = ApplicationPrehireDepartment({})) -> None:
        self._application_prehire_department: ApplicationPrehireDepartment = application_prehire_department
    
    def id(self, id: str) -> "ApplicationPrehireDepartmentBuilder":
        self._application_prehire_department.id = id
        return self
    
    def name(self, name: str) -> "ApplicationPrehireDepartmentBuilder":
        self._application_prehire_department.name = name
        return self
    
    def en_name(self, en_name: str) -> "ApplicationPrehireDepartmentBuilder":
        self._application_prehire_department.en_name = en_name
        return self
    
    def build(self) -> "ApplicationPrehireDepartment":
        return self._application_prehire_department