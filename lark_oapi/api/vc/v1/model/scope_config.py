# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .room_config import RoomConfig


class ScopeConfig(object):
    _types = {
        "scope_type": int,
        "scope_id": str,
        "scope_config": RoomConfig,
    }

    def __init__(self, d):
        self.scope_type: Optional[int] = None
        self.scope_id: Optional[str] = None
        self.scope_config: Optional[RoomConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScopeConfigBuilder":
        return ScopeConfigBuilder()


class ScopeConfigBuilder(object):
    def __init__(self, scope_config: ScopeConfig = ScopeConfig({})) -> None:
        self._scope_config: ScopeConfig = scope_config
    
    def scope_type(self, scope_type: int) -> "ScopeConfigBuilder":
        self._scope_config.scope_type = scope_type
        return self
    
    def scope_id(self, scope_id: str) -> "ScopeConfigBuilder":
        self._scope_config.scope_id = scope_id
        return self
    
    def scope_config(self, scope_config: RoomConfig) -> "ScopeConfigBuilder":
        self._scope_config.scope_config = scope_config
        return self
    
    def build(self) -> "ScopeConfig":
        return self._scope_config