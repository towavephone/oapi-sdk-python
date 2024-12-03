# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enum import Enum
from .enum import Enum


class PersonInfoChn(object):
    _types = {
        "native_region": str,
        "hukou_type": Enum,
        "hukou_location": str,
        "first_entry_time": str,
        "leave_time": str,
        "political_affiliations": List[Enum],
    }

    def __init__(self, d=None):
        self.native_region: Optional[str] = None
        self.hukou_type: Optional[Enum] = None
        self.hukou_location: Optional[str] = None
        self.first_entry_time: Optional[str] = None
        self.leave_time: Optional[str] = None
        self.political_affiliations: Optional[List[Enum]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PersonInfoChnBuilder":
        return PersonInfoChnBuilder()


class PersonInfoChnBuilder(object):
    def __init__(self) -> None:
        self._person_info_chn = PersonInfoChn()

    def native_region(self, native_region: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.native_region = native_region
        return self

    def hukou_type(self, hukou_type: Enum) -> "PersonInfoChnBuilder":
        self._person_info_chn.hukou_type = hukou_type
        return self

    def hukou_location(self, hukou_location: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.hukou_location = hukou_location
        return self

    def first_entry_time(self, first_entry_time: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.first_entry_time = first_entry_time
        return self

    def leave_time(self, leave_time: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.leave_time = leave_time
        return self

    def political_affiliations(self, political_affiliations: List[Enum]) -> "PersonInfoChnBuilder":
        self._person_info_chn.political_affiliations = political_affiliations
        return self

    def build(self) -> "PersonInfoChn":
        return self._person_info_chn
