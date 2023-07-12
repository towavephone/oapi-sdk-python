# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetPreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.pre_hire_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetPreHireRequestBuilder":
        return GetPreHireRequestBuilder()


class GetPreHireRequestBuilder(object):

    def __init__(self, get_pre_hire_request: GetPreHireRequest = GetPreHireRequest()) -> None:
        get_pre_hire_request.http_method = HttpMethod.GET
        get_pre_hire_request.uri = "/open-apis/corehr/v1/pre_hires/:pre_hire_id"
        get_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._get_pre_hire_request: GetPreHireRequest = get_pre_hire_request
    
    def pre_hire_id(self, pre_hire_id: str) -> "GetPreHireRequestBuilder":
        self._get_pre_hire_request.pre_hire_id = pre_hire_id
        self._get_pre_hire_request.paths["pre_hire_id"] = pre_hire_id
        return self
    

    def build(self) -> GetPreHireRequest:
        return self._get_pre_hire_request
