# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .external_background_check import ExternalBackgroundCheck


class CreateExternalBackgroundCheckRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ExternalBackgroundCheck] = None

    @staticmethod
    def builder() -> "CreateExternalBackgroundCheckRequestBuilder":
        return CreateExternalBackgroundCheckRequestBuilder()


class CreateExternalBackgroundCheckRequestBuilder(object):

    def __init__(self, create_external_background_check_request: CreateExternalBackgroundCheckRequest = CreateExternalBackgroundCheckRequest()) -> None:
        create_external_background_check_request.http_method = HttpMethod.POST
        create_external_background_check_request.uri = "/open-apis/hire/v1/external_background_checks"
        create_external_background_check_request.token_types = {AccessTokenType.TENANT}
        self._create_external_background_check_request: CreateExternalBackgroundCheckRequest = create_external_background_check_request
    
    def request_body(self, request_body: ExternalBackgroundCheck) -> "CreateExternalBackgroundCheckRequestBuilder":
        self._create_external_background_check_request.request_body = request_body
        self._create_external_background_check_request.body = request_body
        return self

    def build(self) -> CreateExternalBackgroundCheckRequest:
        return self._create_external_background_check_request
