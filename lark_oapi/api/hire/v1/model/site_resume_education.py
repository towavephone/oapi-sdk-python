# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class SiteResumeEducation(object):
    _types = {
        "degree": str,
        "school": str,
        "major": str,
        "start_time": str,
        "end_time": str,
        "education_type": str,
        "academic_ranking": str,
    }

    def __init__(self, d):
        self.degree: Optional[str] = None
        self.school: Optional[str] = None
        self.major: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.education_type: Optional[str] = None
        self.academic_ranking: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteResumeEducationBuilder":
        return SiteResumeEducationBuilder()


class SiteResumeEducationBuilder(object):
    def __init__(self, site_resume_education: SiteResumeEducation = SiteResumeEducation({})) -> None:
        self._site_resume_education: SiteResumeEducation = site_resume_education
    
    def degree(self, degree: str) -> "SiteResumeEducationBuilder":
        self._site_resume_education.degree = degree
        return self
    
    def school(self, school: str) -> "SiteResumeEducationBuilder":
        self._site_resume_education.school = school
        return self
    
    def major(self, major: str) -> "SiteResumeEducationBuilder":
        self._site_resume_education.major = major
        return self
    
    def start_time(self, start_time: str) -> "SiteResumeEducationBuilder":
        self._site_resume_education.start_time = start_time
        return self
    
    def end_time(self, end_time: str) -> "SiteResumeEducationBuilder":
        self._site_resume_education.end_time = end_time
        return self
    
    def education_type(self, education_type: str) -> "SiteResumeEducationBuilder":
        self._site_resume_education.education_type = education_type
        return self
    
    def academic_ranking(self, academic_ranking: str) -> "SiteResumeEducationBuilder":
        self._site_resume_education.academic_ranking = academic_ranking
        return self
    
    def build(self) -> "SiteResumeEducation":
        return self._site_resume_education