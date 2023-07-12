# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class QueryCustomFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.object_api_name_list: Optional[List[str]] = None

    @staticmethod
    def builder() -> "QueryCustomFieldRequestBuilder":
        return QueryCustomFieldRequestBuilder()


class QueryCustomFieldRequestBuilder(object):

    def __init__(self, query_custom_field_request: QueryCustomFieldRequest = QueryCustomFieldRequest()) -> None:
        query_custom_field_request.http_method = HttpMethod.GET
        query_custom_field_request.uri = "/open-apis/corehr/v1/custom_fields/query"
        query_custom_field_request.token_types = {AccessTokenType.TENANT}
        self._query_custom_field_request: QueryCustomFieldRequest = query_custom_field_request
    
    def object_api_name_list(self, object_api_name_list: List[str]) -> "QueryCustomFieldRequestBuilder":
        self._query_custom_field_request.object_api_name_list = object_api_name_list
        self._query_custom_field_request.queries["object_api_name_list"] = str(object_api_name_list)
        return self
    

    def build(self) -> QueryCustomFieldRequest:
        return self._query_custom_field_request
