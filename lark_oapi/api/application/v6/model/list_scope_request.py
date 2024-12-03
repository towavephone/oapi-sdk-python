# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListScopeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "ListScopeRequestBuilder":
        return ListScopeRequestBuilder()


class ListScopeRequestBuilder(object):

    def __init__(self) -> None:
        list_scope_request = ListScopeRequest()
        list_scope_request.http_method = HttpMethod.GET
        list_scope_request.uri = "/open-apis/application/v6/scopes"
        list_scope_request.token_types = {AccessTokenType.TENANT}
        self._list_scope_request: ListScopeRequest = list_scope_request

    def build(self) -> ListScopeRequest:
        return self._list_scope_request
