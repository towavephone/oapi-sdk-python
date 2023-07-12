# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .search_group_request_body import SearchGroupRequestBody


class SearchGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[SearchGroupRequestBody] = None

    @staticmethod
    def builder() -> "SearchGroupRequestBuilder":
        return SearchGroupRequestBuilder()


class SearchGroupRequestBuilder(object):

    def __init__(self, search_group_request: SearchGroupRequest = SearchGroupRequest()) -> None:
        search_group_request.http_method = HttpMethod.POST
        search_group_request.uri = "/open-apis/attendance/v1/groups/search"
        search_group_request.token_types = {AccessTokenType.TENANT}
        self._search_group_request: SearchGroupRequest = search_group_request
    
    def request_body(self, request_body: SearchGroupRequestBody) -> "SearchGroupRequestBuilder":
        self._search_group_request.request_body = request_body
        self._search_group_request.body = request_body
        return self

    def build(self) -> SearchGroupRequest:
        return self._search_group_request
