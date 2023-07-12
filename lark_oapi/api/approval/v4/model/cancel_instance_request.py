# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .instance_cancel import InstanceCancel


class CancelInstanceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[InstanceCancel] = None

    @staticmethod
    def builder() -> "CancelInstanceRequestBuilder":
        return CancelInstanceRequestBuilder()


class CancelInstanceRequestBuilder(object):

    def __init__(self, cancel_instance_request: CancelInstanceRequest = CancelInstanceRequest()) -> None:
        cancel_instance_request.http_method = HttpMethod.POST
        cancel_instance_request.uri = "/open-apis/approval/v4/instances/cancel"
        cancel_instance_request.token_types = {AccessTokenType.TENANT}
        self._cancel_instance_request: CancelInstanceRequest = cancel_instance_request
    
    def user_id_type(self, user_id_type: str) -> "CancelInstanceRequestBuilder":
        self._cancel_instance_request.user_id_type = user_id_type
        self._cancel_instance_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def request_body(self, request_body: InstanceCancel) -> "CancelInstanceRequestBuilder":
        self._cancel_instance_request.request_body = request_body
        self._cancel_instance_request.body = request_body
        return self

    def build(self) -> CancelInstanceRequest:
        return self._cancel_instance_request
