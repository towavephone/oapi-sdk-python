# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .job_requirement_customized_data_dto import JobRequirementCustomizedDataDto


class JobRequirementDto(object):
    _types = {
        "id": str,
        "short_code": str,
        "name": str,
        "display_progress": int,
        "head_count": int,
        "recruitment_type": IdNameObject,
        "max_level": IdNameObject,
        "min_level": IdNameObject,
        "sequence": IdNameObject,
        "category": int,
        "department": IdNameObject,
        "recruiter_list": List[IdNameObject],
        "jr_hiring_managers": List[IdNameObject],
        "direct_leader_list": List[IdNameObject],
        "start_time": str,
        "deadline": str,
        "priority": int,
        "required_degree": int,
        "max_salary": str,
        "min_salary": str,
        "address": IdNameObject,
        "description": str,
        "customized_data_list": List[JobRequirementCustomizedDataDto],
        "job_id_list": List[str],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.short_code: Optional[str] = None
        self.name: Optional[str] = None
        self.display_progress: Optional[int] = None
        self.head_count: Optional[int] = None
        self.recruitment_type: Optional[IdNameObject] = None
        self.max_level: Optional[IdNameObject] = None
        self.min_level: Optional[IdNameObject] = None
        self.sequence: Optional[IdNameObject] = None
        self.category: Optional[int] = None
        self.department: Optional[IdNameObject] = None
        self.recruiter_list: Optional[List[IdNameObject]] = None
        self.jr_hiring_managers: Optional[List[IdNameObject]] = None
        self.direct_leader_list: Optional[List[IdNameObject]] = None
        self.start_time: Optional[str] = None
        self.deadline: Optional[str] = None
        self.priority: Optional[int] = None
        self.required_degree: Optional[int] = None
        self.max_salary: Optional[str] = None
        self.min_salary: Optional[str] = None
        self.address: Optional[IdNameObject] = None
        self.description: Optional[str] = None
        self.customized_data_list: Optional[List[JobRequirementCustomizedDataDto]] = None
        self.job_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRequirementDtoBuilder":
        return JobRequirementDtoBuilder()


class JobRequirementDtoBuilder(object):
    def __init__(self, job_requirement_dto: JobRequirementDto = JobRequirementDto({})) -> None:
        self._job_requirement_dto: JobRequirementDto = job_requirement_dto
    
    def id(self, id: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.id = id
        return self
    
    def short_code(self, short_code: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.short_code = short_code
        return self
    
    def name(self, name: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.name = name
        return self
    
    def display_progress(self, display_progress: int) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.display_progress = display_progress
        return self
    
    def head_count(self, head_count: int) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.head_count = head_count
        return self
    
    def recruitment_type(self, recruitment_type: IdNameObject) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.recruitment_type = recruitment_type
        return self
    
    def max_level(self, max_level: IdNameObject) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.max_level = max_level
        return self
    
    def min_level(self, min_level: IdNameObject) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.min_level = min_level
        return self
    
    def sequence(self, sequence: IdNameObject) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.sequence = sequence
        return self
    
    def category(self, category: int) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.category = category
        return self
    
    def department(self, department: IdNameObject) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.department = department
        return self
    
    def recruiter_list(self, recruiter_list: List[IdNameObject]) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.recruiter_list = recruiter_list
        return self
    
    def jr_hiring_managers(self, jr_hiring_managers: List[IdNameObject]) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.jr_hiring_managers = jr_hiring_managers
        return self
    
    def direct_leader_list(self, direct_leader_list: List[IdNameObject]) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.direct_leader_list = direct_leader_list
        return self
    
    def start_time(self, start_time: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.start_time = start_time
        return self
    
    def deadline(self, deadline: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.deadline = deadline
        return self
    
    def priority(self, priority: int) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.priority = priority
        return self
    
    def required_degree(self, required_degree: int) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.required_degree = required_degree
        return self
    
    def max_salary(self, max_salary: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.max_salary = max_salary
        return self
    
    def min_salary(self, min_salary: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.min_salary = min_salary
        return self
    
    def address(self, address: IdNameObject) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.address = address
        return self
    
    def description(self, description: str) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.description = description
        return self
    
    def customized_data_list(self, customized_data_list: List[JobRequirementCustomizedDataDto]) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.customized_data_list = customized_data_list
        return self
    
    def job_id_list(self, job_id_list: List[str]) -> "JobRequirementDtoBuilder":
        self._job_requirement_dto.job_id_list = job_id_list
        return self
    
    def build(self) -> "JobRequirementDto":
        return self._job_requirement_dto