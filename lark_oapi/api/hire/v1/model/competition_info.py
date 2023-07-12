# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CompetitionInfo(object):
    _types = {
        "desc": str,
        "name": str,
    }

    def __init__(self, d):
        self.desc: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CompetitionInfoBuilder":
        return CompetitionInfoBuilder()


class CompetitionInfoBuilder(object):
    def __init__(self, competition_info: CompetitionInfo = CompetitionInfo({})) -> None:
        self._competition_info: CompetitionInfo = competition_info
    
    def desc(self, desc: str) -> "CompetitionInfoBuilder":
        self._competition_info.desc = desc
        return self
    
    def name(self, name: str) -> "CompetitionInfoBuilder":
        self._competition_info.name = name
        return self
    
    def build(self) -> "CompetitionInfo":
        return self._competition_info