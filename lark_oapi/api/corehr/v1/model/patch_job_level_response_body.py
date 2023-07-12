# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .job_level import JobLevel


class PatchJobLevelResponseBody(object):
    _types = {
        "job_level": JobLevel,
    }

    def __init__(self, d):
        self.job_level: Optional[JobLevel] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchJobLevelResponseBodyBuilder":
        return PatchJobLevelResponseBodyBuilder()


class PatchJobLevelResponseBodyBuilder(object):
    def __init__(self, patch_job_level_response_body: PatchJobLevelResponseBody = PatchJobLevelResponseBody({})) -> None:
        self._patch_job_level_response_body: PatchJobLevelResponseBody = patch_job_level_response_body
    
    def job_level(self, job_level: JobLevel) -> "PatchJobLevelResponseBodyBuilder":
        self._patch_job_level_response_body.job_level = job_level
        return self
    
    def build(self) -> "PatchJobLevelResponseBody":
        return self._patch_job_level_response_body