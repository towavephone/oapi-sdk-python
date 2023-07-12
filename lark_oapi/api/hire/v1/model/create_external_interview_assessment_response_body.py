# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .external_interview_assessment import ExternalInterviewAssessment


class CreateExternalInterviewAssessmentResponseBody(object):
    _types = {
        "external_interview_assessment": ExternalInterviewAssessment,
    }

    def __init__(self, d):
        self.external_interview_assessment: Optional[ExternalInterviewAssessment] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateExternalInterviewAssessmentResponseBodyBuilder":
        return CreateExternalInterviewAssessmentResponseBodyBuilder()


class CreateExternalInterviewAssessmentResponseBodyBuilder(object):
    def __init__(self, create_external_interview_assessment_response_body: CreateExternalInterviewAssessmentResponseBody = CreateExternalInterviewAssessmentResponseBody({})) -> None:
        self._create_external_interview_assessment_response_body: CreateExternalInterviewAssessmentResponseBody = create_external_interview_assessment_response_body
    
    def external_interview_assessment(self, external_interview_assessment: ExternalInterviewAssessment) -> "CreateExternalInterviewAssessmentResponseBodyBuilder":
        self._create_external_interview_assessment_response_body.external_interview_assessment = external_interview_assessment
        return self
    
    def build(self) -> "CreateExternalInterviewAssessmentResponseBody":
        return self._create_external_interview_assessment_response_body