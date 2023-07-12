# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .enum import Enum
from .object_field_data import ObjectFieldData
from .enum import Enum
from .support_cost_center_item import SupportCostCenterItem
from .email import Email


class PreHireQuery(object):
    _types = {
        "ats_application_id": str,
        "id": str,
        "hire_date": str,
        "employee_type": Enum,
        "worker_id": str,
        "employee_type_id": str,
        "person_id": str,
        "custom_fields": List[ObjectFieldData],
        "onboarding_status": Enum,
        "cost_center_rate": List[SupportCostCenterItem],
        "work_email_list": List[Email],
        "department_id": str,
    }

    def __init__(self, d):
        self.ats_application_id: Optional[str] = None
        self.id: Optional[str] = None
        self.hire_date: Optional[str] = None
        self.employee_type: Optional[Enum] = None
        self.worker_id: Optional[str] = None
        self.employee_type_id: Optional[str] = None
        self.person_id: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        self.onboarding_status: Optional[Enum] = None
        self.cost_center_rate: Optional[List[SupportCostCenterItem]] = None
        self.work_email_list: Optional[List[Email]] = None
        self.department_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PreHireQueryBuilder":
        return PreHireQueryBuilder()


class PreHireQueryBuilder(object):
    def __init__(self, pre_hire_query: PreHireQuery = PreHireQuery({})) -> None:
        self._pre_hire_query: PreHireQuery = pre_hire_query
    
    def ats_application_id(self, ats_application_id: str) -> "PreHireQueryBuilder":
        self._pre_hire_query.ats_application_id = ats_application_id
        return self
    
    def id(self, id: str) -> "PreHireQueryBuilder":
        self._pre_hire_query.id = id
        return self
    
    def hire_date(self, hire_date: str) -> "PreHireQueryBuilder":
        self._pre_hire_query.hire_date = hire_date
        return self
    
    def employee_type(self, employee_type: Enum) -> "PreHireQueryBuilder":
        self._pre_hire_query.employee_type = employee_type
        return self
    
    def worker_id(self, worker_id: str) -> "PreHireQueryBuilder":
        self._pre_hire_query.worker_id = worker_id
        return self
    
    def employee_type_id(self, employee_type_id: str) -> "PreHireQueryBuilder":
        self._pre_hire_query.employee_type_id = employee_type_id
        return self
    
    def person_id(self, person_id: str) -> "PreHireQueryBuilder":
        self._pre_hire_query.person_id = person_id
        return self
    
    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "PreHireQueryBuilder":
        self._pre_hire_query.custom_fields = custom_fields
        return self
    
    def onboarding_status(self, onboarding_status: Enum) -> "PreHireQueryBuilder":
        self._pre_hire_query.onboarding_status = onboarding_status
        return self
    
    def cost_center_rate(self, cost_center_rate: List[SupportCostCenterItem]) -> "PreHireQueryBuilder":
        self._pre_hire_query.cost_center_rate = cost_center_rate
        return self
    
    def work_email_list(self, work_email_list: List[Email]) -> "PreHireQueryBuilder":
        self._pre_hire_query.work_email_list = work_email_list
        return self
    
    def department_id(self, department_id: str) -> "PreHireQueryBuilder":
        self._pre_hire_query.department_id = department_id
        return self
    
    def build(self) -> "PreHireQuery":
        return self._pre_hire_query