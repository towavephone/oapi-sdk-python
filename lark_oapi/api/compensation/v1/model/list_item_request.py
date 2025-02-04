# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListItemRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.item_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListItemRequestBuilder":
        return ListItemRequestBuilder()


class ListItemRequestBuilder(object):

    def __init__(self) -> None:
        list_item_request = ListItemRequest()
        list_item_request.http_method = HttpMethod.GET
        list_item_request.uri = "/open-apis/compensation/v1/items"
        list_item_request.token_types = {AccessTokenType.TENANT}
        self._list_item_request: ListItemRequest = list_item_request

    def page_size(self, page_size: int) -> "ListItemRequestBuilder":
        self._list_item_request.page_size = page_size
        self._list_item_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListItemRequestBuilder":
        self._list_item_request.page_token = page_token
        self._list_item_request.add_query("page_token", page_token)
        return self

    def item_type(self, item_type: str) -> "ListItemRequestBuilder":
        self._list_item_request.item_type = item_type
        self._list_item_request.add_query("item_type", item_type)
        return self

    def build(self) -> ListItemRequest:
        return self._list_item_request
