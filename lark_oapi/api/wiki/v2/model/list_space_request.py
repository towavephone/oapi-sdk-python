# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListSpaceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListSpaceRequestBuilder":
        return ListSpaceRequestBuilder()


class ListSpaceRequestBuilder(object):

    def __init__(self, list_space_request: ListSpaceRequest = ListSpaceRequest()) -> None:
        list_space_request.http_method = HttpMethod.GET
        list_space_request.uri = "/open-apis/wiki/v2/spaces"
        list_space_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_space_request: ListSpaceRequest = list_space_request
    
    def page_size(self, page_size: int) -> "ListSpaceRequestBuilder":
        self._list_space_request.page_size = page_size
        self._list_space_request.queries["page_size"] = str(page_size)
        return self
    
    def page_token(self, page_token: str) -> "ListSpaceRequestBuilder":
        self._list_space_request.page_token = page_token
        self._list_space_request.queries["page_token"] = str(page_token)
        return self
    

    def build(self) -> ListSpaceRequest:
        return self._list_space_request
