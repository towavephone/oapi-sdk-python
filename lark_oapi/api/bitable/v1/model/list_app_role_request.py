# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListAppRoleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.app_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListAppRoleRequestBuilder":
        return ListAppRoleRequestBuilder()


class ListAppRoleRequestBuilder(object):

    def __init__(self, list_app_role_request: ListAppRoleRequest = ListAppRoleRequest()) -> None:
        list_app_role_request.http_method = HttpMethod.GET
        list_app_role_request.uri = "/open-apis/bitable/v1/apps/:app_token/roles"
        list_app_role_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_app_role_request: ListAppRoleRequest = list_app_role_request
    
    def page_size(self, page_size: int) -> "ListAppRoleRequestBuilder":
        self._list_app_role_request.page_size = page_size
        self._list_app_role_request.queries["page_size"] = str(page_size)
        return self
    
    def page_token(self, page_token: str) -> "ListAppRoleRequestBuilder":
        self._list_app_role_request.page_token = page_token
        self._list_app_role_request.queries["page_token"] = str(page_token)
        return self
    
    def app_token(self, app_token: str) -> "ListAppRoleRequestBuilder":
        self._list_app_role_request.app_token = app_token
        self._list_app_role_request.paths["app_token"] = app_token
        return self
    

    def build(self) -> ListAppRoleRequest:
        return self._list_app_role_request
