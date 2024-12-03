# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SearchPreHireRequestBody(object):
    _types = {
        "worker_ids": List[str],
        "pre_hire_ids": List[str],
        "person_ids": List[str],
        "onboarding_date_start": str,
        "onboarding_date_end": str,
        "updated_date_start": str,
        "updated_date_end": str,
        "onboarding_location_ids": List[str],
        "onboarding_status": str,
        "department_ids": List[str],
        "direct_manager_ids": List[str],
        "employee_type_ids": List[str],
        "employee_subtype_ids": List[str],
        "job_family_ids": List[str],
        "key_word": str,
        "rehire": str,
        "fields": List[str],
    }

    def __init__(self, d=None):
        self.worker_ids: Optional[List[str]] = None
        self.pre_hire_ids: Optional[List[str]] = None
        self.person_ids: Optional[List[str]] = None
        self.onboarding_date_start: Optional[str] = None
        self.onboarding_date_end: Optional[str] = None
        self.updated_date_start: Optional[str] = None
        self.updated_date_end: Optional[str] = None
        self.onboarding_location_ids: Optional[List[str]] = None
        self.onboarding_status: Optional[str] = None
        self.department_ids: Optional[List[str]] = None
        self.direct_manager_ids: Optional[List[str]] = None
        self.employee_type_ids: Optional[List[str]] = None
        self.employee_subtype_ids: Optional[List[str]] = None
        self.job_family_ids: Optional[List[str]] = None
        self.key_word: Optional[str] = None
        self.rehire: Optional[str] = None
        self.fields: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchPreHireRequestBodyBuilder":
        return SearchPreHireRequestBodyBuilder()


class SearchPreHireRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_pre_hire_request_body = SearchPreHireRequestBody()

    def worker_ids(self, worker_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.worker_ids = worker_ids
        return self

    def pre_hire_ids(self, pre_hire_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.pre_hire_ids = pre_hire_ids
        return self

    def person_ids(self, person_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.person_ids = person_ids
        return self

    def onboarding_date_start(self, onboarding_date_start: str) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.onboarding_date_start = onboarding_date_start
        return self

    def onboarding_date_end(self, onboarding_date_end: str) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.onboarding_date_end = onboarding_date_end
        return self

    def updated_date_start(self, updated_date_start: str) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.updated_date_start = updated_date_start
        return self

    def updated_date_end(self, updated_date_end: str) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.updated_date_end = updated_date_end
        return self

    def onboarding_location_ids(self, onboarding_location_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.onboarding_location_ids = onboarding_location_ids
        return self

    def onboarding_status(self, onboarding_status: str) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.onboarding_status = onboarding_status
        return self

    def department_ids(self, department_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.department_ids = department_ids
        return self

    def direct_manager_ids(self, direct_manager_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.direct_manager_ids = direct_manager_ids
        return self

    def employee_type_ids(self, employee_type_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.employee_type_ids = employee_type_ids
        return self

    def employee_subtype_ids(self, employee_subtype_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.employee_subtype_ids = employee_subtype_ids
        return self

    def job_family_ids(self, job_family_ids: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.job_family_ids = job_family_ids
        return self

    def key_word(self, key_word: str) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.key_word = key_word
        return self

    def rehire(self, rehire: str) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.rehire = rehire
        return self

    def fields(self, fields: List[str]) -> "SearchPreHireRequestBodyBuilder":
        self._search_pre_hire_request_body.fields = fields
        return self

    def build(self) -> "SearchPreHireRequestBody":
        return self._search_pre_hire_request_body
