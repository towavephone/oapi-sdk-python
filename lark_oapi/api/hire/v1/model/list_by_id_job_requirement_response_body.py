# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .job_requirement_dto import JobRequirementDto


class ListByIdJobRequirementResponseBody(object):
    _types = {
        "items": List[JobRequirementDto],
    }

    def __init__(self, d):
        self.items: Optional[List[JobRequirementDto]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListByIdJobRequirementResponseBodyBuilder":
        return ListByIdJobRequirementResponseBodyBuilder()


class ListByIdJobRequirementResponseBodyBuilder(object):
    def __init__(self, list_by_id_job_requirement_response_body: ListByIdJobRequirementResponseBody = ListByIdJobRequirementResponseBody({})) -> None:
        self._list_by_id_job_requirement_response_body: ListByIdJobRequirementResponseBody = list_by_id_job_requirement_response_body
    
    def items(self, items: List[JobRequirementDto]) -> "ListByIdJobRequirementResponseBodyBuilder":
        self._list_by_id_job_requirement_response_body.items = items
        return self
    
    def build(self) -> "ListByIdJobRequirementResponseBody":
        return self._list_by_id_job_requirement_response_body