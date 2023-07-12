# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListGroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListGroupRequestBuilder":
        return ListGroupRequestBuilder()


class ListGroupRequestBuilder(object):

    def __init__(self, list_group_request: ListGroupRequest = ListGroupRequest()) -> None:
        list_group_request.http_method = HttpMethod.GET
        list_group_request.uri = "/open-apis/attendance/v1/groups"
        list_group_request.token_types = {AccessTokenType.TENANT}
        self._list_group_request: ListGroupRequest = list_group_request
    
    def page_size(self, page_size: int) -> "ListGroupRequestBuilder":
        self._list_group_request.page_size = page_size
        self._list_group_request.queries["page_size"] = str(page_size)
        return self
    
    def page_token(self, page_token: str) -> "ListGroupRequestBuilder":
        self._list_group_request.page_token = page_token
        self._list_group_request.queries["page_token"] = str(page_token)
        return self
    

    def build(self) -> ListGroupRequest:
        return self._list_group_request
