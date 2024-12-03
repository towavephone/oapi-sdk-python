# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .agency_account_user import AgencyAccountUser


class AgencyAccount(object):
    _types = {
        "id": str,
        "reason": str,
        "create_time": str,
        "status": int,
        "user_info": AgencyAccountUser,
        "role": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.reason: Optional[str] = None
        self.create_time: Optional[str] = None
        self.status: Optional[int] = None
        self.user_info: Optional[AgencyAccountUser] = None
        self.role: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AgencyAccountBuilder":
        return AgencyAccountBuilder()


class AgencyAccountBuilder(object):
    def __init__(self) -> None:
        self._agency_account = AgencyAccount()

    def id(self, id: str) -> "AgencyAccountBuilder":
        self._agency_account.id = id
        return self

    def reason(self, reason: str) -> "AgencyAccountBuilder":
        self._agency_account.reason = reason
        return self

    def create_time(self, create_time: str) -> "AgencyAccountBuilder":
        self._agency_account.create_time = create_time
        return self

    def status(self, status: int) -> "AgencyAccountBuilder":
        self._agency_account.status = status
        return self

    def user_info(self, user_info: AgencyAccountUser) -> "AgencyAccountBuilder":
        self._agency_account.user_info = user_info
        return self

    def role(self, role: int) -> "AgencyAccountBuilder":
        self._agency_account.role = role
        return self

    def build(self) -> "AgencyAccount":
        return self._agency_account
