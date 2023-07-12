# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .external_interview import ExternalInterview


class CreateExternalInterviewResponseBody(object):
    _types = {
        "external_interview": ExternalInterview,
    }

    def __init__(self, d):
        self.external_interview: Optional[ExternalInterview] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateExternalInterviewResponseBodyBuilder":
        return CreateExternalInterviewResponseBodyBuilder()


class CreateExternalInterviewResponseBodyBuilder(object):
    def __init__(self, create_external_interview_response_body: CreateExternalInterviewResponseBody = CreateExternalInterviewResponseBody({})) -> None:
        self._create_external_interview_response_body: CreateExternalInterviewResponseBody = create_external_interview_response_body
    
    def external_interview(self, external_interview: ExternalInterview) -> "CreateExternalInterviewResponseBodyBuilder":
        self._create_external_interview_response_body.external_interview = external_interview
        return self
    
    def build(self) -> "CreateExternalInterviewResponseBody":
        return self._create_external_interview_response_body