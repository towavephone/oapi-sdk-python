# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .term import Term
from .term import Term
from .term import Term
from .related_meta import RelatedMeta
from .statistics import Statistics
from .outer_info import OuterInfo


class Entity(object):
    _types = {
        "id": str,
        "main_keys": List[Term],
        "aliases": List[Term],
        "description": str,
        "creator": int,
        "create_time": int,
        "updater": int,
        "update_time": int,
        "related_meta": RelatedMeta,
        "statistics": Statistics,
        "outer_info": OuterInfo,
        "rich_text": str,
        "source": int,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.main_keys: Optional[List[Term]] = None
        self.full_names: Optional[List[Term]] = None
        self.aliases: Optional[List[Term]] = None
        self.description: Optional[str] = None
        self.creator: Optional[int] = None
        self.create_time: Optional[int] = None
        self.updater: Optional[int] = None
        self.update_time: Optional[int] = None
        self.related_meta: Optional[RelatedMeta] = None
        self.statistics: Optional[Statistics] = None
        self.outer_info: Optional[OuterInfo] = None
        self.rich_text: Optional[str] = None
        self.source: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EntityBuilder":
        return EntityBuilder()


class EntityBuilder(object):
    def __init__(self, entity: Entity = Entity({})) -> None:
        self._entity: Entity = entity
    
    def id(self, id: str) -> "EntityBuilder":
        self._entity.id = id
        return self
    
    def main_keys(self, main_keys: List[Term]) -> "EntityBuilder":
        self._entity.main_keys = main_keys
        return self
    
    
    def aliases(self, aliases: List[Term]) -> "EntityBuilder":
        self._entity.aliases = aliases
        return self
    
    def description(self, description: str) -> "EntityBuilder":
        self._entity.description = description
        return self
    
    def creator(self, creator: int) -> "EntityBuilder":
        self._entity.creator = creator
        return self
    
    def create_time(self, create_time: int) -> "EntityBuilder":
        self._entity.create_time = create_time
        return self
    
    def updater(self, updater: int) -> "EntityBuilder":
        self._entity.updater = updater
        return self
    
    def update_time(self, update_time: int) -> "EntityBuilder":
        self._entity.update_time = update_time
        return self
    
    def related_meta(self, related_meta: RelatedMeta) -> "EntityBuilder":
        self._entity.related_meta = related_meta
        return self
    
    def statistics(self, statistics: Statistics) -> "EntityBuilder":
        self._entity.statistics = statistics
        return self
    
    def outer_info(self, outer_info: OuterInfo) -> "EntityBuilder":
        self._entity.outer_info = outer_info
        return self
    
    def rich_text(self, rich_text: str) -> "EntityBuilder":
        self._entity.rich_text = rich_text
        return self
    
    def source(self, source: int) -> "EntityBuilder":
        self._entity.source = source
        return self
    
    def build(self) -> "Entity":
        return self._entity