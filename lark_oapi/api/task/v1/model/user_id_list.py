# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .user_id import UserId


class UserIdList(object):
    _types = {
        "user_id_list": List[UserId],
    }

    def __init__(self, d):
        self.user_id_list: Optional[List[UserId]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserIdListBuilder":
        return UserIdListBuilder()


class UserIdListBuilder(object):
    def __init__(self, user_id_list: UserIdList = UserIdList({})) -> None:
        self._user_id_list: UserIdList = user_id_list
    
    def user_id_list(self, user_id_list: List[UserId]) -> "UserIdListBuilder":
        self._user_id_list.user_id_list = user_id_list
        return self
    
    def build(self) -> "UserIdList":
        return self._user_id_list