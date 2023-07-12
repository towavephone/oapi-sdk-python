# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .site_name import SiteName


class SiteJobRecruitmentType(object):
    _types = {
        "id": str,
        "name": SiteName,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[SiteName] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SiteJobRecruitmentTypeBuilder":
        return SiteJobRecruitmentTypeBuilder()


class SiteJobRecruitmentTypeBuilder(object):
    def __init__(self, site_job_recruitment_type: SiteJobRecruitmentType = SiteJobRecruitmentType({})) -> None:
        self._site_job_recruitment_type: SiteJobRecruitmentType = site_job_recruitment_type
    
    def id(self, id: str) -> "SiteJobRecruitmentTypeBuilder":
        self._site_job_recruitment_type.id = id
        return self
    
    def name(self, name: SiteName) -> "SiteJobRecruitmentTypeBuilder":
        self._site_job_recruitment_type.name = name
        return self
    
    def build(self) -> "SiteJobRecruitmentType":
        return self._site_job_recruitment_type