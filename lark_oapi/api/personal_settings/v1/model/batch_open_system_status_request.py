# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_open_system_status_request_body import BatchOpenSystemStatusRequestBody


class BatchOpenSystemStatusRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.system_status_id: Optional[int] = None
        self.request_body: Optional[BatchOpenSystemStatusRequestBody] = None

    @staticmethod
    def builder() -> "BatchOpenSystemStatusRequestBuilder":
        return BatchOpenSystemStatusRequestBuilder()


class BatchOpenSystemStatusRequestBuilder(object):

    def __init__(self, batch_open_system_status_request: BatchOpenSystemStatusRequest = BatchOpenSystemStatusRequest()) -> None:
        batch_open_system_status_request.http_method = HttpMethod.POST
        batch_open_system_status_request.uri = "/open-apis/personal_settings/v1/system_statuses/:system_status_id/batch_open"
        batch_open_system_status_request.token_types = {AccessTokenType.TENANT}
        self._batch_open_system_status_request: BatchOpenSystemStatusRequest = batch_open_system_status_request
    
    def user_id_type(self, user_id_type: str) -> "BatchOpenSystemStatusRequestBuilder":
        self._batch_open_system_status_request.user_id_type = user_id_type
        self._batch_open_system_status_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def system_status_id(self, system_status_id: int) -> "BatchOpenSystemStatusRequestBuilder":
        self._batch_open_system_status_request.system_status_id = system_status_id
        self._batch_open_system_status_request.paths["system_status_id"] = system_status_id
        return self
    
    def request_body(self, request_body: BatchOpenSystemStatusRequestBody) -> "BatchOpenSystemStatusRequestBuilder":
        self._batch_open_system_status_request.request_body = request_body
        self._batch_open_system_status_request.body = request_body
        return self

    def build(self) -> BatchOpenSystemStatusRequest:
        return self._batch_open_system_status_request
