# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .name import Name


class AssignedOrganization(object):
    _types = {
        "org_key": str,
        "org_name": Name,
        "org_id_list": List[str],
    }

    def __init__(self, d):
        self.org_key: Optional[str] = None
        self.org_name: Optional[Name] = None
        self.org_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AssignedOrganizationBuilder":
        return AssignedOrganizationBuilder()


class AssignedOrganizationBuilder(object):
    def __init__(self, assigned_organization: AssignedOrganization = AssignedOrganization({})) -> None:
        self._assigned_organization: AssignedOrganization = assigned_organization
    
    def org_key(self, org_key: str) -> "AssignedOrganizationBuilder":
        self._assigned_organization.org_key = org_key
        return self
    
    def org_name(self, org_name: Name) -> "AssignedOrganizationBuilder":
        self._assigned_organization.org_name = org_name
        return self
    
    def org_id_list(self, org_id_list: List[str]) -> "AssignedOrganizationBuilder":
        self._assigned_organization.org_id_list = org_id_list
        return self
    
    def build(self) -> "AssignedOrganization":
        return self._assigned_organization