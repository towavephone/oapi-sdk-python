# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListPreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        self.pre_hire_ids: Optional[List[str]] = None

    @staticmethod
    def builder() -> "ListPreHireRequestBuilder":
        return ListPreHireRequestBuilder()


class ListPreHireRequestBuilder(object):

    def __init__(self, list_pre_hire_request: ListPreHireRequest = ListPreHireRequest()) -> None:
        list_pre_hire_request.http_method = HttpMethod.GET
        list_pre_hire_request.uri = "/open-apis/corehr/v1/pre_hires"
        list_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._list_pre_hire_request: ListPreHireRequest = list_pre_hire_request
    
    def page_token(self, page_token: str) -> "ListPreHireRequestBuilder":
        self._list_pre_hire_request.page_token = page_token
        self._list_pre_hire_request.queries["page_token"] = str(page_token)
        return self
    
    def page_size(self, page_size: str) -> "ListPreHireRequestBuilder":
        self._list_pre_hire_request.page_size = page_size
        self._list_pre_hire_request.queries["page_size"] = str(page_size)
        return self
    
    def pre_hire_ids(self, pre_hire_ids: List[str]) -> "ListPreHireRequestBuilder":
        self._list_pre_hire_request.pre_hire_ids = pre_hire_ids
        self._list_pre_hire_request.queries["pre_hire_ids"] = str(pre_hire_ids)
        return self
    

    def build(self) -> ListPreHireRequest:
        return self._list_pre_hire_request
