# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ReservePermissionChecker(object):
    _types = {
        "check_field": int,
        "check_mode": int,
        "check_list": List[str],
    }

    def __init__(self, d):
        self.check_field: Optional[int] = None
        self.check_mode: Optional[int] = None
        self.check_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReservePermissionCheckerBuilder":
        return ReservePermissionCheckerBuilder()


class ReservePermissionCheckerBuilder(object):
    def __init__(self, reserve_permission_checker: ReservePermissionChecker = ReservePermissionChecker({})) -> None:
        self._reserve_permission_checker: ReservePermissionChecker = reserve_permission_checker
    
    def check_field(self, check_field: int) -> "ReservePermissionCheckerBuilder":
        self._reserve_permission_checker.check_field = check_field
        return self
    
    def check_mode(self, check_mode: int) -> "ReservePermissionCheckerBuilder":
        self._reserve_permission_checker.check_mode = check_mode
        return self
    
    def check_list(self, check_list: List[str]) -> "ReservePermissionCheckerBuilder":
        self._reserve_permission_checker.check_list = check_list
        return self
    
    def build(self) -> "ReservePermissionChecker":
        return self._reserve_permission_checker