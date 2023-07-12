# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class JobProcess(object):
    _types = {
        "your_property_name": str,
    }

    def __init__(self, d):
        self.your_property_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobProcessBuilder":
        return JobProcessBuilder()


class JobProcessBuilder(object):
    def __init__(self, job_process: JobProcess = JobProcess({})) -> None:
        self._job_process: JobProcess = job_process
    
    def your_property_name(self, your_property_name: str) -> "JobProcessBuilder":
        self._job_process.your_property_name = your_property_name
        return self
    
    def build(self) -> "JobProcess":
        return self._job_process