# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .check_external_instance_request_body import CheckExternalInstanceRequestBody


class CheckExternalInstanceRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CheckExternalInstanceRequestBody] = None

    @staticmethod
    def builder() -> "CheckExternalInstanceRequestBuilder":
        return CheckExternalInstanceRequestBuilder()


class CheckExternalInstanceRequestBuilder(object):

    def __init__(self, check_external_instance_request: CheckExternalInstanceRequest = CheckExternalInstanceRequest()) -> None:
        check_external_instance_request.http_method = HttpMethod.POST
        check_external_instance_request.uri = "/open-apis/approval/v4/external_instances/check"
        check_external_instance_request.token_types = {AccessTokenType.TENANT}
        self._check_external_instance_request: CheckExternalInstanceRequest = check_external_instance_request
    
    def request_body(self, request_body: CheckExternalInstanceRequestBody) -> "CheckExternalInstanceRequestBuilder":
        self._check_external_instance_request.request_body = request_body
        self._check_external_instance_request.body = request_body
        return self

    def build(self) -> CheckExternalInstanceRequest:
        return self._check_external_instance_request
