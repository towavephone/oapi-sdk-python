# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .app_table_record import AppTableRecord


class UpdateAppTableRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.ignore_consistency_check: Optional[bool] = None
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.record_id: Optional[str] = None
        self.request_body: Optional[AppTableRecord] = None

    @staticmethod
    def builder() -> "UpdateAppTableRecordRequestBuilder":
        return UpdateAppTableRecordRequestBuilder()


class UpdateAppTableRecordRequestBuilder(object):

    def __init__(self) -> None:
        update_app_table_record_request = UpdateAppTableRecordRequest()
        update_app_table_record_request.http_method = HttpMethod.PUT
        update_app_table_record_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id"
        update_app_table_record_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._update_app_table_record_request: UpdateAppTableRecordRequest = update_app_table_record_request

    def user_id_type(self, user_id_type: str) -> "UpdateAppTableRecordRequestBuilder":
        self._update_app_table_record_request.user_id_type = user_id_type
        self._update_app_table_record_request.add_query("user_id_type", user_id_type)
        return self

    def ignore_consistency_check(self, ignore_consistency_check: bool) -> "UpdateAppTableRecordRequestBuilder":
        self._update_app_table_record_request.ignore_consistency_check = ignore_consistency_check
        self._update_app_table_record_request.add_query("ignore_consistency_check", ignore_consistency_check)
        return self

    def app_token(self, app_token: str) -> "UpdateAppTableRecordRequestBuilder":
        self._update_app_table_record_request.app_token = app_token
        self._update_app_table_record_request.paths["app_token"] = str(app_token)
        return self

    def table_id(self, table_id: str) -> "UpdateAppTableRecordRequestBuilder":
        self._update_app_table_record_request.table_id = table_id
        self._update_app_table_record_request.paths["table_id"] = str(table_id)
        return self

    def record_id(self, record_id: str) -> "UpdateAppTableRecordRequestBuilder":
        self._update_app_table_record_request.record_id = record_id
        self._update_app_table_record_request.paths["record_id"] = str(record_id)
        return self

    def request_body(self, request_body: AppTableRecord) -> "UpdateAppTableRecordRequestBuilder":
        self._update_app_table_record_request.request_body = request_body
        self._update_app_table_record_request.body = request_body
        return self

    def build(self) -> UpdateAppTableRecordRequest:
        return self._update_app_table_record_request
