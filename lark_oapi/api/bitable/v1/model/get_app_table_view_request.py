# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetAppTableViewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.view_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetAppTableViewRequestBuilder":
        return GetAppTableViewRequestBuilder()


class GetAppTableViewRequestBuilder(object):

    def __init__(self, get_app_table_view_request: GetAppTableViewRequest = GetAppTableViewRequest()) -> None:
        get_app_table_view_request.http_method = HttpMethod.GET
        get_app_table_view_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views/:view_id"
        get_app_table_view_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_app_table_view_request: GetAppTableViewRequest = get_app_table_view_request
    
    def app_token(self, app_token: str) -> "GetAppTableViewRequestBuilder":
        self._get_app_table_view_request.app_token = app_token
        self._get_app_table_view_request.paths["app_token"] = app_token
        return self
    
    def table_id(self, table_id: str) -> "GetAppTableViewRequestBuilder":
        self._get_app_table_view_request.table_id = table_id
        self._get_app_table_view_request.paths["table_id"] = table_id
        return self
    
    def view_id(self, view_id: str) -> "GetAppTableViewRequestBuilder":
        self._get_app_table_view_request.view_id = view_id
        self._get_app_table_view_request.paths["view_id"] = view_id
        return self
    

    def build(self) -> GetAppTableViewRequest:
        return self._get_app_table_view_request
