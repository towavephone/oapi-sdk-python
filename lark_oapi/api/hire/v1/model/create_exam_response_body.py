# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateExamResponseBody(object):
    _types = {
        "exam_id": str,
        "application_id": str,
        "exam_resource_name": str,
        "score": float,
        "uuid": str,
        "operator_id": str,
        "operate_time": str,
    }

    def __init__(self, d=None):
        self.exam_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.exam_resource_name: Optional[str] = None
        self.score: Optional[float] = None
        self.uuid: Optional[str] = None
        self.operator_id: Optional[str] = None
        self.operate_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateExamResponseBodyBuilder":
        return CreateExamResponseBodyBuilder()


class CreateExamResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_exam_response_body = CreateExamResponseBody()

    def exam_id(self, exam_id: str) -> "CreateExamResponseBodyBuilder":
        self._create_exam_response_body.exam_id = exam_id
        return self

    def application_id(self, application_id: str) -> "CreateExamResponseBodyBuilder":
        self._create_exam_response_body.application_id = application_id
        return self

    def exam_resource_name(self, exam_resource_name: str) -> "CreateExamResponseBodyBuilder":
        self._create_exam_response_body.exam_resource_name = exam_resource_name
        return self

    def score(self, score: float) -> "CreateExamResponseBodyBuilder":
        self._create_exam_response_body.score = score
        return self

    def uuid(self, uuid: str) -> "CreateExamResponseBodyBuilder":
        self._create_exam_response_body.uuid = uuid
        return self

    def operator_id(self, operator_id: str) -> "CreateExamResponseBodyBuilder":
        self._create_exam_response_body.operator_id = operator_id
        return self

    def operate_time(self, operate_time: str) -> "CreateExamResponseBodyBuilder":
        self._create_exam_response_body.operate_time = operate_time
        return self

    def build(self) -> "CreateExamResponseBody":
        return self._create_exam_response_body
