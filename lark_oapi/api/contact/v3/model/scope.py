# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .department import Department
from .user import User
from .user_group import UserGroup


class Scope(object):
    _types = {
        "departments": List[Department],
        "users": List[User],
        "user_groups": List[UserGroup],
    }

    def __init__(self, d):
        self.departments: Optional[List[Department]] = None
        self.users: Optional[List[User]] = None
        self.user_groups: Optional[List[UserGroup]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScopeBuilder":
        return ScopeBuilder()


class ScopeBuilder(object):
    def __init__(self, scope: Scope = Scope({})) -> None:
        self._scope: Scope = scope
    
    def departments(self, departments: List[Department]) -> "ScopeBuilder":
        self._scope.departments = departments
        return self
    
    def users(self, users: List[User]) -> "ScopeBuilder":
        self._scope.users = users
        return self
    
    def user_groups(self, user_groups: List[UserGroup]) -> "ScopeBuilder":
        self._scope.user_groups = user_groups
        return self
    
    def build(self) -> "Scope":
        return self._scope