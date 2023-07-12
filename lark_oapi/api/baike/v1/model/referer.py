# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class Referer(object):
    _types = {
        "id": str,
        "title": str,
        "url": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.title: Optional[str] = None
        self.url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RefererBuilder":
        return RefererBuilder()


class RefererBuilder(object):
    def __init__(self, referer: Referer = Referer({})) -> None:
        self._referer: Referer = referer
    
    def id(self, id: str) -> "RefererBuilder":
        self._referer.id = id
        return self
    
    def title(self, title: str) -> "RefererBuilder":
        self._referer.title = title
        return self
    
    def url(self, url: str) -> "RefererBuilder":
        self._referer.url = url
        return self
    
    def build(self) -> "Referer":
        return self._referer