# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n


class InterviewAssessmentDimensionArgsScore(object):
    _types = {
        "id": str,
        "name": I18n,
        "description": I18n,
        "enabled": bool,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.description: Optional[I18n] = None
        self.enabled: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewAssessmentDimensionArgsScoreBuilder":
        return InterviewAssessmentDimensionArgsScoreBuilder()


class InterviewAssessmentDimensionArgsScoreBuilder(object):
    def __init__(self, interview_assessment_dimension_args_score: InterviewAssessmentDimensionArgsScore = InterviewAssessmentDimensionArgsScore({})) -> None:
        self._interview_assessment_dimension_args_score: InterviewAssessmentDimensionArgsScore = interview_assessment_dimension_args_score
    
    def id(self, id: str) -> "InterviewAssessmentDimensionArgsScoreBuilder":
        self._interview_assessment_dimension_args_score.id = id
        return self
    
    def name(self, name: I18n) -> "InterviewAssessmentDimensionArgsScoreBuilder":
        self._interview_assessment_dimension_args_score.name = name
        return self
    
    def description(self, description: I18n) -> "InterviewAssessmentDimensionArgsScoreBuilder":
        self._interview_assessment_dimension_args_score.description = description
        return self
    
    def enabled(self, enabled: bool) -> "InterviewAssessmentDimensionArgsScoreBuilder":
        self._interview_assessment_dimension_args_score.enabled = enabled
        return self
    
    def build(self) -> "InterviewAssessmentDimensionArgsScore":
        return self._interview_assessment_dimension_args_score