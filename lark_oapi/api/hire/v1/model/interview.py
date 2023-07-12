# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .interview_record import InterviewRecord


class Interview(object):
    _types = {
        "id": str,
        "begin_time": int,
        "end_time": int,
        "round": int,
        "stage_id": str,
        "interview_record_list": List[InterviewRecord],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.begin_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.round: Optional[int] = None
        self.stage_id: Optional[str] = None
        self.interview_record_list: Optional[List[InterviewRecord]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewBuilder":
        return InterviewBuilder()


class InterviewBuilder(object):
    def __init__(self, interview: Interview = Interview({})) -> None:
        self._interview: Interview = interview
    
    def id(self, id: str) -> "InterviewBuilder":
        self._interview.id = id
        return self
    
    def begin_time(self, begin_time: int) -> "InterviewBuilder":
        self._interview.begin_time = begin_time
        return self
    
    def end_time(self, end_time: int) -> "InterviewBuilder":
        self._interview.end_time = end_time
        return self
    
    def round(self, round: int) -> "InterviewBuilder":
        self._interview.round = round
        return self
    
    def stage_id(self, stage_id: str) -> "InterviewBuilder":
        self._interview.stage_id = stage_id
        return self
    
    def interview_record_list(self, interview_record_list: List[InterviewRecord]) -> "InterviewBuilder":
        self._interview.interview_record_list = interview_record_list
        return self
    
    def build(self) -> "Interview":
        return self._interview