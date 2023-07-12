# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ManagementScope(object):
    _types = {
        "management_dimension": str,
        "obj_id": str,
    }

    def __init__(self, d):
        self.management_dimension: Optional[str] = None
        self.obj_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ManagementScopeBuilder":
        return ManagementScopeBuilder()


class ManagementScopeBuilder(object):
    def __init__(self, management_scope: ManagementScope = ManagementScope({})) -> None:
        self._management_scope: ManagementScope = management_scope
    
    def management_dimension(self, management_dimension: str) -> "ManagementScopeBuilder":
        self._management_scope.management_dimension = management_dimension
        return self
    
    def obj_id(self, obj_id: str) -> "ManagementScopeBuilder":
        self._management_scope.obj_id = obj_id
        return self
    
    def build(self) -> "ManagementScope":
        return self._management_scope