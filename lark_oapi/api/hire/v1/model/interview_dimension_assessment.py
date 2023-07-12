# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .i18n import I18n
from .interview_dimension_score import InterviewDimensionScore
from .interview_dimension_score import InterviewDimensionScore


class InterviewDimensionAssessment(object):
    _types = {
        "id": str,
        "name": I18n,
        "content": str,
        "dimension_id": str,
        "dimension_score": InterviewDimensionScore,
        "dimension_score_list": List[InterviewDimensionScore],
        "dimension_type": int,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.content: Optional[str] = None
        self.dimension_id: Optional[str] = None
        self.dimension_score: Optional[InterviewDimensionScore] = None
        self.dimension_score_list: Optional[List[InterviewDimensionScore]] = None
        self.dimension_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewDimensionAssessmentBuilder":
        return InterviewDimensionAssessmentBuilder()


class InterviewDimensionAssessmentBuilder(object):
    def __init__(self, interview_dimension_assessment: InterviewDimensionAssessment = InterviewDimensionAssessment({})) -> None:
        self._interview_dimension_assessment: InterviewDimensionAssessment = interview_dimension_assessment
    
    def id(self, id: str) -> "InterviewDimensionAssessmentBuilder":
        self._interview_dimension_assessment.id = id
        return self
    
    def name(self, name: I18n) -> "InterviewDimensionAssessmentBuilder":
        self._interview_dimension_assessment.name = name
        return self
    
    def content(self, content: str) -> "InterviewDimensionAssessmentBuilder":
        self._interview_dimension_assessment.content = content
        return self
    
    def dimension_id(self, dimension_id: str) -> "InterviewDimensionAssessmentBuilder":
        self._interview_dimension_assessment.dimension_id = dimension_id
        return self
    
    def dimension_score(self, dimension_score: InterviewDimensionScore) -> "InterviewDimensionAssessmentBuilder":
        self._interview_dimension_assessment.dimension_score = dimension_score
        return self
    
    def dimension_score_list(self, dimension_score_list: List[InterviewDimensionScore]) -> "InterviewDimensionAssessmentBuilder":
        self._interview_dimension_assessment.dimension_score_list = dimension_score_list
        return self
    
    def dimension_type(self, dimension_type: int) -> "InterviewDimensionAssessmentBuilder":
        self._interview_dimension_assessment.dimension_type = dimension_type
        return self
    
    def build(self) -> "InterviewDimensionAssessment":
        return self._interview_dimension_assessment