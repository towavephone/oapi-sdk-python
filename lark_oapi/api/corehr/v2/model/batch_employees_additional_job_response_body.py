# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .employees_additional_job import EmployeesAdditionalJob


class BatchEmployeesAdditionalJobResponseBody(object):
    _types = {
        "items": List[EmployeesAdditionalJob],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[EmployeesAdditionalJob]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchEmployeesAdditionalJobResponseBodyBuilder":
        return BatchEmployeesAdditionalJobResponseBodyBuilder()


class BatchEmployeesAdditionalJobResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_employees_additional_job_response_body = BatchEmployeesAdditionalJobResponseBody()

    def items(self, items: List[EmployeesAdditionalJob]) -> "BatchEmployeesAdditionalJobResponseBodyBuilder":
        self._batch_employees_additional_job_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "BatchEmployeesAdditionalJobResponseBodyBuilder":
        self._batch_employees_additional_job_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "BatchEmployeesAdditionalJobResponseBodyBuilder":
        self._batch_employees_additional_job_response_body.has_more = has_more
        return self

    def build(self) -> "BatchEmployeesAdditionalJobResponseBody":
        return self._batch_employees_additional_job_response_body
