# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .combined_job_result_default_job_post import CombinedJobResultDefaultJobPost
from .job import Job
from .job_manager import JobManager
from .registration_info import RegistrationInfo


class CombinedJobResult(object):
    _types = {
        "default_job_post": CombinedJobResultDefaultJobPost,
        "job": Job,
        "job_manager": JobManager,
        "interview_registration_schema_info": RegistrationInfo,
    }

    def __init__(self, d):
        self.default_job_post: Optional[CombinedJobResultDefaultJobPost] = None
        self.job: Optional[Job] = None
        self.job_manager: Optional[JobManager] = None
        self.interview_registration_schema_info: Optional[RegistrationInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CombinedJobResultBuilder":
        return CombinedJobResultBuilder()


class CombinedJobResultBuilder(object):
    def __init__(self, combined_job_result: CombinedJobResult = CombinedJobResult({})) -> None:
        self._combined_job_result: CombinedJobResult = combined_job_result
    
    def default_job_post(self, default_job_post: CombinedJobResultDefaultJobPost) -> "CombinedJobResultBuilder":
        self._combined_job_result.default_job_post = default_job_post
        return self
    
    def job(self, job: Job) -> "CombinedJobResultBuilder":
        self._combined_job_result.job = job
        return self
    
    def job_manager(self, job_manager: JobManager) -> "CombinedJobResultBuilder":
        self._combined_job_result.job_manager = job_manager
        return self
    
    def interview_registration_schema_info(self, interview_registration_schema_info: RegistrationInfo) -> "CombinedJobResultBuilder":
        self._combined_job_result.interview_registration_schema_info = interview_registration_schema_info
        return self
    
    def build(self) -> "CombinedJobResult":
        return self._combined_job_result