# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SystemInfo(object):
    _types = {
        "session_id": str,
        "lang": str,
        "locale": str,
    }

    def __init__(self, d=None):
        self.session_id: Optional[str] = None
        self.lang: Optional[str] = None
        self.locale: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SystemInfoBuilder":
        return SystemInfoBuilder()


class SystemInfoBuilder(object):
    def __init__(self) -> None:
        self._system_info = SystemInfo()

    def session_id(self, session_id: str) -> "SystemInfoBuilder":
        self._system_info.session_id = session_id
        return self

    def lang(self, lang: str) -> "SystemInfoBuilder":
        self._system_info.lang = lang
        return self

    def locale(self, locale: str) -> "SystemInfoBuilder":
        self._system_info.locale = locale
        return self

    def build(self) -> "SystemInfo":
        return self._system_info
