# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListJobFunctionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobFunctionRequestBuilder":
        return ListJobFunctionRequestBuilder()


class ListJobFunctionRequestBuilder(object):

    def __init__(self) -> None:
        list_job_function_request = ListJobFunctionRequest()
        list_job_function_request.http_method = HttpMethod.GET
        list_job_function_request.uri = "/open-apis/hire/v1/job_functions"
        list_job_function_request.token_types = {AccessTokenType.TENANT}
        self._list_job_function_request: ListJobFunctionRequest = list_job_function_request

    def page_size(self, page_size: int) -> "ListJobFunctionRequestBuilder":
        self._list_job_function_request.page_size = page_size
        self._list_job_function_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListJobFunctionRequestBuilder":
        self._list_job_function_request.page_token = page_token
        self._list_job_function_request.add_query("page_token", page_token)
        return self

    def build(self) -> ListJobFunctionRequest:
        return self._list_job_function_request
