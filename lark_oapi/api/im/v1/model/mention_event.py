# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .user_id import UserId


class MentionEvent(object):
    _types = {
        "key": str,
        "id": UserId,
        "name": str,
        "tenant_key": str,
    }

    def __init__(self, d):
        self.key: Optional[str] = None
        self.id: Optional[UserId] = None
        self.name: Optional[str] = None
        self.tenant_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MentionEventBuilder":
        return MentionEventBuilder()


class MentionEventBuilder(object):
    def __init__(self, mention_event: MentionEvent = MentionEvent({})) -> None:
        self._mention_event: MentionEvent = mention_event
    
    def key(self, key: str) -> "MentionEventBuilder":
        self._mention_event.key = key
        return self
    
    def id(self, id: UserId) -> "MentionEventBuilder":
        self._mention_event.id = id
        return self
    
    def name(self, name: str) -> "MentionEventBuilder":
        self._mention_event.name = name
        return self
    
    def tenant_key(self, tenant_key: str) -> "MentionEventBuilder":
        self._mention_event.tenant_key = tenant_key
        return self
    
    def build(self) -> "MentionEvent":
        return self._mention_event