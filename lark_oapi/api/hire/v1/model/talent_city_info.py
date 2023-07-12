# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class TalentCityInfo(object):
    _types = {
        "city_code": str,
        "zh_name": str,
        "en_name": str,
    }

    def __init__(self, d):
        self.city_code: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCityInfoBuilder":
        return TalentCityInfoBuilder()


class TalentCityInfoBuilder(object):
    def __init__(self, talent_city_info: TalentCityInfo = TalentCityInfo({})) -> None:
        self._talent_city_info: TalentCityInfo = talent_city_info
    
    def city_code(self, city_code: str) -> "TalentCityInfoBuilder":
        self._talent_city_info.city_code = city_code
        return self
    
    def zh_name(self, zh_name: str) -> "TalentCityInfoBuilder":
        self._talent_city_info.zh_name = zh_name
        return self
    
    def en_name(self, en_name: str) -> "TalentCityInfoBuilder":
        self._talent_city_info.en_name = en_name
        return self
    
    def build(self) -> "TalentCityInfo":
        return self._talent_city_info