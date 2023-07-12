# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_create_app_table_request_body import BatchCreateAppTableRequestBody


class BatchCreateAppTableRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.app_token: Optional[str] = None
        self.request_body: Optional[BatchCreateAppTableRequestBody] = None

    @staticmethod
    def builder() -> "BatchCreateAppTableRequestBuilder":
        return BatchCreateAppTableRequestBuilder()


class BatchCreateAppTableRequestBuilder(object):

    def __init__(self, batch_create_app_table_request: BatchCreateAppTableRequest = BatchCreateAppTableRequest()) -> None:
        batch_create_app_table_request.http_method = HttpMethod.POST
        batch_create_app_table_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/batch_create"
        batch_create_app_table_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._batch_create_app_table_request: BatchCreateAppTableRequest = batch_create_app_table_request
    
    def user_id_type(self, user_id_type: str) -> "BatchCreateAppTableRequestBuilder":
        self._batch_create_app_table_request.user_id_type = user_id_type
        self._batch_create_app_table_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def app_token(self, app_token: str) -> "BatchCreateAppTableRequestBuilder":
        self._batch_create_app_table_request.app_token = app_token
        self._batch_create_app_table_request.paths["app_token"] = app_token
        return self
    
    def request_body(self, request_body: BatchCreateAppTableRequestBody) -> "BatchCreateAppTableRequestBuilder":
        self._batch_create_app_table_request.request_body = request_body
        self._batch_create_app_table_request.body = request_body
        return self

    def build(self) -> BatchCreateAppTableRequest:
        return self._batch_create_app_table_request
