# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .employees_additional_job_write_resp import EmployeesAdditionalJobWriteResp


class CreateEmployeesAdditionalJobResponseBody(object):
    _types = {
        "additional_job": EmployeesAdditionalJobWriteResp,
    }

    def __init__(self, d=None):
        self.additional_job: Optional[EmployeesAdditionalJobWriteResp] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateEmployeesAdditionalJobResponseBodyBuilder":
        return CreateEmployeesAdditionalJobResponseBodyBuilder()


class CreateEmployeesAdditionalJobResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_employees_additional_job_response_body = CreateEmployeesAdditionalJobResponseBody()

    def additional_job(self,
                       additional_job: EmployeesAdditionalJobWriteResp) -> "CreateEmployeesAdditionalJobResponseBodyBuilder":
        self._create_employees_additional_job_response_body.additional_job = additional_job
        return self

    def build(self) -> "CreateEmployeesAdditionalJobResponseBody":
        return self._create_employees_additional_job_response_body
