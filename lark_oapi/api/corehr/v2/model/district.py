# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class District(object):
    _types = {
        "district_id": str,
        "name": List[I18n],
        "city_id": str,
        "subregion_code": str,
        "status": int,
    }

    def __init__(self, d=None):
        self.district_id: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.city_id: Optional[str] = None
        self.subregion_code: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DistrictBuilder":
        return DistrictBuilder()


class DistrictBuilder(object):
    def __init__(self) -> None:
        self._district = District()

    def district_id(self, district_id: str) -> "DistrictBuilder":
        self._district.district_id = district_id
        return self

    def name(self, name: List[I18n]) -> "DistrictBuilder":
        self._district.name = name
        return self

    def city_id(self, city_id: str) -> "DistrictBuilder":
        self._district.city_id = city_id
        return self

    def subregion_code(self, subregion_code: str) -> "DistrictBuilder":
        self._district.subregion_code = subregion_code
        return self

    def status(self, status: int) -> "DistrictBuilder":
        self._district.status = status
        return self

    def build(self) -> "District":
        return self._district
