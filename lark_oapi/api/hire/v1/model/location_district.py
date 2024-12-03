# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .location_name_info import LocationNameInfo


class LocationDistrict(object):
    _types = {
        "district_code": str,
        "city_code": str,
        "state_code": str,
        "country_code": str,
        "district_name_info": LocationNameInfo,
    }

    def __init__(self, d=None):
        self.district_code: Optional[str] = None
        self.city_code: Optional[str] = None
        self.state_code: Optional[str] = None
        self.country_code: Optional[str] = None
        self.district_name_info: Optional[LocationNameInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LocationDistrictBuilder":
        return LocationDistrictBuilder()


class LocationDistrictBuilder(object):
    def __init__(self) -> None:
        self._location_district = LocationDistrict()

    def district_code(self, district_code: str) -> "LocationDistrictBuilder":
        self._location_district.district_code = district_code
        return self

    def city_code(self, city_code: str) -> "LocationDistrictBuilder":
        self._location_district.city_code = city_code
        return self

    def state_code(self, state_code: str) -> "LocationDistrictBuilder":
        self._location_district.state_code = state_code
        return self

    def country_code(self, country_code: str) -> "LocationDistrictBuilder":
        self._location_district.country_code = country_code
        return self

    def district_name_info(self, district_name_info: LocationNameInfo) -> "LocationDistrictBuilder":
        self._location_district.district_name_info = district_name_info
        return self

    def build(self) -> "LocationDistrict":
        return self._location_district
