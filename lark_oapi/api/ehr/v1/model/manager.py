# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Manager(object):
    _types = {
        "user_id": str,
        "name": str,
        "en_name": str,
    }

    def __init__(self, d):
        self.user_id: Optional[str] = None
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ManagerBuilder":
        return ManagerBuilder()


class ManagerBuilder(object):
    def __init__(self, manager: Manager = Manager({})) -> None:
        self._manager: Manager = manager
    
    def user_id(self, user_id: str) -> "ManagerBuilder":
        self._manager.user_id = user_id
        return self
    
    def name(self, name: str) -> "ManagerBuilder":
        self._manager.name = name
        return self
    
    def en_name(self, en_name: str) -> "ManagerBuilder":
        self._manager.en_name = en_name
        return self
    
    def build(self) -> "Manager":
        return self._manager