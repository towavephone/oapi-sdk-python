# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .job_family import JobFamily


class ListJobFamilyResponseBody(object):
    _types = {
        "items": List[JobFamily],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[JobFamily]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListJobFamilyResponseBodyBuilder":
        return ListJobFamilyResponseBodyBuilder()


class ListJobFamilyResponseBodyBuilder(object):
    def __init__(self, list_job_family_response_body: ListJobFamilyResponseBody = ListJobFamilyResponseBody({})) -> None:
        self._list_job_family_response_body: ListJobFamilyResponseBody = list_job_family_response_body
    
    def items(self, items: List[JobFamily]) -> "ListJobFamilyResponseBodyBuilder":
        self._list_job_family_response_body.items = items
        return self
    
    def has_more(self, has_more: bool) -> "ListJobFamilyResponseBodyBuilder":
        self._list_job_family_response_body.has_more = has_more
        return self
    
    def page_token(self, page_token: str) -> "ListJobFamilyResponseBodyBuilder":
        self._list_job_family_response_body.page_token = page_token
        return self
    
    def build(self) -> "ListJobFamilyResponseBody":
        return self._list_job_family_response_body