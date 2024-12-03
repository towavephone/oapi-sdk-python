# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class TalentBasicInfoV2(object):
    _types = {
        "id": str,
        "name": str,
        "mobile_code": str,
        "mobile_number": str,
        "email": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.mobile_code: Optional[str] = None
        self.mobile_number: Optional[str] = None
        self.email: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentBasicInfoV2Builder":
        return TalentBasicInfoV2Builder()


class TalentBasicInfoV2Builder(object):
    def __init__(self) -> None:
        self._talent_basic_info_v2 = TalentBasicInfoV2()

    def id(self, id: str) -> "TalentBasicInfoV2Builder":
        self._talent_basic_info_v2.id = id
        return self

    def name(self, name: str) -> "TalentBasicInfoV2Builder":
        self._talent_basic_info_v2.name = name
        return self

    def mobile_code(self, mobile_code: str) -> "TalentBasicInfoV2Builder":
        self._talent_basic_info_v2.mobile_code = mobile_code
        return self

    def mobile_number(self, mobile_number: str) -> "TalentBasicInfoV2Builder":
        self._talent_basic_info_v2.mobile_number = mobile_number
        return self

    def email(self, email: str) -> "TalentBasicInfoV2Builder":
        self._talent_basic_info_v2.email = email
        return self

    def build(self) -> "TalentBasicInfoV2":
        return self._talent_basic_info_v2
