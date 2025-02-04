# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n


class JobDetailRecruitmentType(object):
    _types = {
        "id": str,
        "name": I18n,
        "active_status": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.active_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDetailRecruitmentTypeBuilder":
        return JobDetailRecruitmentTypeBuilder()


class JobDetailRecruitmentTypeBuilder(object):
    def __init__(self) -> None:
        self._job_detail_recruitment_type = JobDetailRecruitmentType()

    def id(self, id: str) -> "JobDetailRecruitmentTypeBuilder":
        self._job_detail_recruitment_type.id = id
        return self

    def name(self, name: I18n) -> "JobDetailRecruitmentTypeBuilder":
        self._job_detail_recruitment_type.name = name
        return self

    def active_status(self, active_status: int) -> "JobDetailRecruitmentTypeBuilder":
        self._job_detail_recruitment_type.active_status = active_status
        return self

    def build(self) -> "JobDetailRecruitmentType":
        return self._job_detail_recruitment_type
