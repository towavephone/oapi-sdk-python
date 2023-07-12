# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .talent_nationality import TalentNationality
from .talent_city_info import TalentCityInfo
from .talent_city_info import TalentCityInfo
from .talent_city_info import TalentCityInfo
from .talent_identification_info import TalentIdentificationInfo
from .talent_customized_data_child import TalentCustomizedDataChild


class TalentBasicInfo(object):
    _types = {
        "name": str,
        "mobile": str,
        "mobile_code": str,
        "mobile_country_code": str,
        "email": str,
        "experience_years": int,
        "age": int,
        "nationality": TalentNationality,
        "gender": int,
        "current_city": TalentCityInfo,
        "hometown_city": TalentCityInfo,
        "preferred_city_list": List[TalentCityInfo],
        "identification_type": int,
        "identification_number": str,
        "birthday": int,
        "creator_id": str,
        "marital_status": int,
        "current_home_address": str,
        "customized_data_list": List[TalentCustomizedDataChild],
        "modify_time": str,
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.mobile: Optional[str] = None
        self.mobile_code: Optional[str] = None
        self.mobile_country_code: Optional[str] = None
        self.email: Optional[str] = None
        self.experience_years: Optional[int] = None
        self.age: Optional[int] = None
        self.nationality: Optional[TalentNationality] = None
        self.gender: Optional[int] = None
        self.current_city: Optional[TalentCityInfo] = None
        self.hometown_city: Optional[TalentCityInfo] = None
        self.preferred_city_list: Optional[List[TalentCityInfo]] = None
        self.identification_type: Optional[int] = None
        self.identification_number: Optional[str] = None
        self.identification: Optional[TalentIdentificationInfo] = None
        self.birthday: Optional[int] = None
        self.creator_id: Optional[str] = None
        self.marital_status: Optional[int] = None
        self.current_home_address: Optional[str] = None
        self.customized_data_list: Optional[List[TalentCustomizedDataChild]] = None
        self.modify_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentBasicInfoBuilder":
        return TalentBasicInfoBuilder()


class TalentBasicInfoBuilder(object):
    def __init__(self, talent_basic_info: TalentBasicInfo = TalentBasicInfo({})) -> None:
        self._talent_basic_info: TalentBasicInfo = talent_basic_info
    
    def name(self, name: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.name = name
        return self
    
    def mobile(self, mobile: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.mobile = mobile
        return self
    
    def mobile_code(self, mobile_code: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.mobile_code = mobile_code
        return self
    
    def mobile_country_code(self, mobile_country_code: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.mobile_country_code = mobile_country_code
        return self
    
    def email(self, email: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.email = email
        return self
    
    def experience_years(self, experience_years: int) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.experience_years = experience_years
        return self
    
    def age(self, age: int) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.age = age
        return self
    
    def nationality(self, nationality: TalentNationality) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.nationality = nationality
        return self
    
    def gender(self, gender: int) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.gender = gender
        return self
    
    def current_city(self, current_city: TalentCityInfo) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.current_city = current_city
        return self
    
    def hometown_city(self, hometown_city: TalentCityInfo) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.hometown_city = hometown_city
        return self
    
    def preferred_city_list(self, preferred_city_list: List[TalentCityInfo]) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.preferred_city_list = preferred_city_list
        return self
    
    def identification_type(self, identification_type: int) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.identification_type = identification_type
        return self
    
    def identification_number(self, identification_number: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.identification_number = identification_number
        return self
    
    
    def birthday(self, birthday: int) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.birthday = birthday
        return self
    
    def creator_id(self, creator_id: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.creator_id = creator_id
        return self
    
    def marital_status(self, marital_status: int) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.marital_status = marital_status
        return self
    
    def current_home_address(self, current_home_address: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.current_home_address = current_home_address
        return self
    
    def customized_data_list(self, customized_data_list: List[TalentCustomizedDataChild]) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.customized_data_list = customized_data_list
        return self
    
    def modify_time(self, modify_time: str) -> "TalentBasicInfoBuilder":
        self._talent_basic_info.modify_time = modify_time
        return self
    
    def build(self) -> "TalentBasicInfo":
        return self._talent_basic_info