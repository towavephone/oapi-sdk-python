# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .enum import Enum
from .enum import Enum
from .object_field_data import ObjectFieldData


class PersonInfoChn(object):
    _types = {
        "id": str,
        "native_region": str,
        "political_affiliation_list": List[Enum],
        "hukou_type": Enum,
        "hukou_location": str,
        "person_id": str,
        "custom_fields": List[ObjectFieldData],
        "working_years": int,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.native_region: Optional[str] = None
        self.political_affiliation_list: Optional[List[Enum]] = None
        self.hukou_type: Optional[Enum] = None
        self.hukou_location: Optional[str] = None
        self.person_id: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        self.working_years: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PersonInfoChnBuilder":
        return PersonInfoChnBuilder()


class PersonInfoChnBuilder(object):
    def __init__(self, person_info_chn: PersonInfoChn = PersonInfoChn({})) -> None:
        self._person_info_chn: PersonInfoChn = person_info_chn
    
    def id(self, id: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.id = id
        return self
    
    def native_region(self, native_region: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.native_region = native_region
        return self
    
    def political_affiliation_list(self, political_affiliation_list: List[Enum]) -> "PersonInfoChnBuilder":
        self._person_info_chn.political_affiliation_list = political_affiliation_list
        return self
    
    def hukou_type(self, hukou_type: Enum) -> "PersonInfoChnBuilder":
        self._person_info_chn.hukou_type = hukou_type
        return self
    
    def hukou_location(self, hukou_location: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.hukou_location = hukou_location
        return self
    
    def person_id(self, person_id: str) -> "PersonInfoChnBuilder":
        self._person_info_chn.person_id = person_id
        return self
    
    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "PersonInfoChnBuilder":
        self._person_info_chn.custom_fields = custom_fields
        return self
    
    def working_years(self, working_years: int) -> "PersonInfoChnBuilder":
        self._person_info_chn.working_years = working_years
        return self
    
    def build(self) -> "PersonInfoChn":
        return self._person_info_chn