# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .interview_assessment_dimension import InterviewAssessmentDimension
from .interview_assessment_dimension import InterviewAssessmentDimension
from .interview_assessment_dimension import InterviewAssessmentDimension
from .interview_assessment_dimension import InterviewAssessmentDimension


class InterviewAssessmentTemplateArgs(object):
    _types = {
        "conclusion_dimension": InterviewAssessmentDimension,
        "score_dimension": InterviewAssessmentDimension,
        "content_dimension": InterviewAssessmentDimension,
        "custom_dimension_list": List[InterviewAssessmentDimension],
    }

    def __init__(self, d):
        self.conclusion_dimension: Optional[InterviewAssessmentDimension] = None
        self.score_dimension: Optional[InterviewAssessmentDimension] = None
        self.content_dimension: Optional[InterviewAssessmentDimension] = None
        self.custom_dimension_list: Optional[List[InterviewAssessmentDimension]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewAssessmentTemplateArgsBuilder":
        return InterviewAssessmentTemplateArgsBuilder()


class InterviewAssessmentTemplateArgsBuilder(object):
    def __init__(self, interview_assessment_template_args: InterviewAssessmentTemplateArgs = InterviewAssessmentTemplateArgs({})) -> None:
        self._interview_assessment_template_args: InterviewAssessmentTemplateArgs = interview_assessment_template_args
    
    def conclusion_dimension(self, conclusion_dimension: InterviewAssessmentDimension) -> "InterviewAssessmentTemplateArgsBuilder":
        self._interview_assessment_template_args.conclusion_dimension = conclusion_dimension
        return self
    
    def score_dimension(self, score_dimension: InterviewAssessmentDimension) -> "InterviewAssessmentTemplateArgsBuilder":
        self._interview_assessment_template_args.score_dimension = score_dimension
        return self
    
    def content_dimension(self, content_dimension: InterviewAssessmentDimension) -> "InterviewAssessmentTemplateArgsBuilder":
        self._interview_assessment_template_args.content_dimension = content_dimension
        return self
    
    def custom_dimension_list(self, custom_dimension_list: List[InterviewAssessmentDimension]) -> "InterviewAssessmentTemplateArgsBuilder":
        self._interview_assessment_template_args.custom_dimension_list = custom_dimension_list
        return self
    
    def build(self) -> "InterviewAssessmentTemplateArgs":
        return self._interview_assessment_template_args