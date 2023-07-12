# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DeleteAppTableRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.record_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteAppTableRecordRequestBuilder":
        return DeleteAppTableRecordRequestBuilder()


class DeleteAppTableRecordRequestBuilder(object):

    def __init__(self, delete_app_table_record_request: DeleteAppTableRecordRequest = DeleteAppTableRecordRequest()) -> None:
        delete_app_table_record_request.http_method = HttpMethod.DELETE
        delete_app_table_record_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id"
        delete_app_table_record_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._delete_app_table_record_request: DeleteAppTableRecordRequest = delete_app_table_record_request
    
    def app_token(self, app_token: str) -> "DeleteAppTableRecordRequestBuilder":
        self._delete_app_table_record_request.app_token = app_token
        self._delete_app_table_record_request.paths["app_token"] = app_token
        return self
    
    def table_id(self, table_id: str) -> "DeleteAppTableRecordRequestBuilder":
        self._delete_app_table_record_request.table_id = table_id
        self._delete_app_table_record_request.paths["table_id"] = table_id
        return self
    
    def record_id(self, record_id: str) -> "DeleteAppTableRecordRequestBuilder":
        self._delete_app_table_record_request.record_id = record_id
        self._delete_app_table_record_request.paths["record_id"] = record_id
        return self
    

    def build(self) -> DeleteAppTableRecordRequest:
        return self._delete_app_table_record_request
