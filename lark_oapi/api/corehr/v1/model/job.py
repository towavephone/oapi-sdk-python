# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .i18n import I18n
from .object_field_data import ObjectFieldData


class Job(object):
    _types = {
        "id": str,
        "code": str,
        "name": List[I18n],
        "description": List[I18n],
        "active": bool,
        "job_title": List[I18n],
        "job_family_id_list": List[str],
        "job_level_id_list": List[str],
        "working_hours_type_id": str,
        "effective_time": str,
        "expiration_time": str,
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.code: Optional[str] = None
        self.name: Optional[List[I18n]] = None
        self.description: Optional[List[I18n]] = None
        self.active: Optional[bool] = None
        self.job_title: Optional[List[I18n]] = None
        self.job_family_id_list: Optional[List[str]] = None
        self.job_level_id_list: Optional[List[str]] = None
        self.working_hours_type_id: Optional[str] = None
        self.effective_time: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobBuilder":
        return JobBuilder()


class JobBuilder(object):
    def __init__(self, job: Job = Job({})) -> None:
        self._job: Job = job
    
    def id(self, id: str) -> "JobBuilder":
        self._job.id = id
        return self
    
    def code(self, code: str) -> "JobBuilder":
        self._job.code = code
        return self
    
    def name(self, name: List[I18n]) -> "JobBuilder":
        self._job.name = name
        return self
    
    def description(self, description: List[I18n]) -> "JobBuilder":
        self._job.description = description
        return self
    
    def active(self, active: bool) -> "JobBuilder":
        self._job.active = active
        return self
    
    def job_title(self, job_title: List[I18n]) -> "JobBuilder":
        self._job.job_title = job_title
        return self
    
    def job_family_id_list(self, job_family_id_list: List[str]) -> "JobBuilder":
        self._job.job_family_id_list = job_family_id_list
        return self
    
    def job_level_id_list(self, job_level_id_list: List[str]) -> "JobBuilder":
        self._job.job_level_id_list = job_level_id_list
        return self
    
    def working_hours_type_id(self, working_hours_type_id: str) -> "JobBuilder":
        self._job.working_hours_type_id = working_hours_type_id
        return self
    
    def effective_time(self, effective_time: str) -> "JobBuilder":
        self._job.effective_time = effective_time
        return self
    
    def expiration_time(self, expiration_time: str) -> "JobBuilder":
        self._job.expiration_time = expiration_time
        return self
    
    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "JobBuilder":
        self._job.custom_fields = custom_fields
        return self
    
    def build(self) -> "Job":
        return self._job