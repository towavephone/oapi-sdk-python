# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .create_emp_custom_org import CreateEmpCustomOrg


class JobDataCustomOrg(object):
    _types = {
        "effective_time": str,
        "start_reason": str,
        "custom_org_with_rates": List[CreateEmpCustomOrg],
        "object_api_name": str,
    }

    def __init__(self, d=None):
        self.effective_time: Optional[str] = None
        self.start_reason: Optional[str] = None
        self.custom_org_with_rates: Optional[List[CreateEmpCustomOrg]] = None
        self.object_api_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobDataCustomOrgBuilder":
        return JobDataCustomOrgBuilder()


class JobDataCustomOrgBuilder(object):
    def __init__(self) -> None:
        self._job_data_custom_org = JobDataCustomOrg()

    def effective_time(self, effective_time: str) -> "JobDataCustomOrgBuilder":
        self._job_data_custom_org.effective_time = effective_time
        return self

    def start_reason(self, start_reason: str) -> "JobDataCustomOrgBuilder":
        self._job_data_custom_org.start_reason = start_reason
        return self

    def custom_org_with_rates(self, custom_org_with_rates: List[CreateEmpCustomOrg]) -> "JobDataCustomOrgBuilder":
        self._job_data_custom_org.custom_org_with_rates = custom_org_with_rates
        return self

    def object_api_name(self, object_api_name: str) -> "JobDataCustomOrgBuilder":
        self._job_data_custom_org.object_api_name = object_api_name
        return self

    def build(self) -> "JobDataCustomOrg":
        return self._job_data_custom_org
