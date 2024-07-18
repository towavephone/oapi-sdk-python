# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .query_pre_hire_request_body import QueryPreHireRequestBody


class QueryPreHireRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.request_body: Optional[QueryPreHireRequestBody] = None

    @staticmethod
    def builder() -> "QueryPreHireRequestBuilder":
        return QueryPreHireRequestBuilder()


class QueryPreHireRequestBuilder(object):

    def __init__(self) -> None:
        query_pre_hire_request = QueryPreHireRequest()
        query_pre_hire_request.http_method = HttpMethod.POST
        query_pre_hire_request.uri = "/open-apis/corehr/v2/pre_hires/query"
        query_pre_hire_request.token_types = {AccessTokenType.TENANT}
        self._query_pre_hire_request: QueryPreHireRequest = query_pre_hire_request

    def page_size(self, page_size: int) -> "QueryPreHireRequestBuilder":
        self._query_pre_hire_request.page_size = page_size
        self._query_pre_hire_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "QueryPreHireRequestBuilder":
        self._query_pre_hire_request.page_token = page_token
        self._query_pre_hire_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "QueryPreHireRequestBuilder":
        self._query_pre_hire_request.user_id_type = user_id_type
        self._query_pre_hire_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "QueryPreHireRequestBuilder":
        self._query_pre_hire_request.department_id_type = department_id_type
        self._query_pre_hire_request.add_query("department_id_type", department_id_type)
        return self

    def request_body(self, request_body: QueryPreHireRequestBody) -> "QueryPreHireRequestBuilder":
        self._query_pre_hire_request.request_body = request_body
        self._query_pre_hire_request.body = request_body
        return self

    def build(self) -> QueryPreHireRequest:
        return self._query_pre_hire_request
