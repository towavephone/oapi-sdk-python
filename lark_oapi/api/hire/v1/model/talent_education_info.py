# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .talent_customized_data_child import TalentCustomizedDataChild


class TalentEducationInfo(object):
    _types = {
        "id": str,
        "degree": int,
        "school": str,
        "field_of_study": str,
        "start_time": str,
        "end_time": str,
        "education_type": int,
        "academic_ranking": int,
        "tag_list": List[int],
        "customized_data_list": List[TalentCustomizedDataChild],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.degree: Optional[int] = None
        self.school: Optional[str] = None
        self.field_of_study: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.education_type: Optional[int] = None
        self.academic_ranking: Optional[int] = None
        self.tag_list: Optional[List[int]] = None
        self.customized_data_list: Optional[List[TalentCustomizedDataChild]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentEducationInfoBuilder":
        return TalentEducationInfoBuilder()


class TalentEducationInfoBuilder(object):
    def __init__(self, talent_education_info: TalentEducationInfo = TalentEducationInfo({})) -> None:
        self._talent_education_info: TalentEducationInfo = talent_education_info
    
    def id(self, id: str) -> "TalentEducationInfoBuilder":
        self._talent_education_info.id = id
        return self
    
    def degree(self, degree: int) -> "TalentEducationInfoBuilder":
        self._talent_education_info.degree = degree
        return self
    
    def school(self, school: str) -> "TalentEducationInfoBuilder":
        self._talent_education_info.school = school
        return self
    
    def field_of_study(self, field_of_study: str) -> "TalentEducationInfoBuilder":
        self._talent_education_info.field_of_study = field_of_study
        return self
    
    def start_time(self, start_time: str) -> "TalentEducationInfoBuilder":
        self._talent_education_info.start_time = start_time
        return self
    
    def end_time(self, end_time: str) -> "TalentEducationInfoBuilder":
        self._talent_education_info.end_time = end_time
        return self
    
    def education_type(self, education_type: int) -> "TalentEducationInfoBuilder":
        self._talent_education_info.education_type = education_type
        return self
    
    def academic_ranking(self, academic_ranking: int) -> "TalentEducationInfoBuilder":
        self._talent_education_info.academic_ranking = academic_ranking
        return self
    
    def tag_list(self, tag_list: List[int]) -> "TalentEducationInfoBuilder":
        self._talent_education_info.tag_list = tag_list
        return self
    
    def customized_data_list(self, customized_data_list: List[TalentCustomizedDataChild]) -> "TalentEducationInfoBuilder":
        self._talent_education_info.customized_data_list = customized_data_list
        return self
    
    def build(self) -> "TalentEducationInfo":
        return self._talent_education_info