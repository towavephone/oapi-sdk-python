# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .talent_customized_data_object_value import TalentCustomizedDataObjectValue


class TalentCombinedCareerInfo(object):
    _types = {
        "id": str,
        "company": str,
        "title": str,
        "desc": str,
        "start_time": str,
        "end_time": str,
        "career_type": int,
        "customized_data": List[TalentCustomizedDataObjectValue],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.company: Optional[str] = None
        self.title: Optional[str] = None
        self.desc: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.career_type: Optional[int] = None
        self.customized_data: Optional[List[TalentCustomizedDataObjectValue]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentCombinedCareerInfoBuilder":
        return TalentCombinedCareerInfoBuilder()


class TalentCombinedCareerInfoBuilder(object):
    def __init__(self, talent_combined_career_info: TalentCombinedCareerInfo = TalentCombinedCareerInfo({})) -> None:
        self._talent_combined_career_info: TalentCombinedCareerInfo = talent_combined_career_info
    
    def id(self, id: str) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.id = id
        return self
    
    def company(self, company: str) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.company = company
        return self
    
    def title(self, title: str) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.title = title
        return self
    
    def desc(self, desc: str) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.desc = desc
        return self
    
    def start_time(self, start_time: str) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.start_time = start_time
        return self
    
    def end_time(self, end_time: str) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.end_time = end_time
        return self
    
    def career_type(self, career_type: int) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.career_type = career_type
        return self
    
    def customized_data(self, customized_data: List[TalentCustomizedDataObjectValue]) -> "TalentCombinedCareerInfoBuilder":
        self._talent_combined_career_info.customized_data = customized_data
        return self
    
    def build(self) -> "TalentCombinedCareerInfo":
        return self._talent_combined_career_info