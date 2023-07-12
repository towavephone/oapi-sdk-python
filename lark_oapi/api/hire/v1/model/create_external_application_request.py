# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .external_application import ExternalApplication


class CreateExternalApplicationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ExternalApplication] = None

    @staticmethod
    def builder() -> "CreateExternalApplicationRequestBuilder":
        return CreateExternalApplicationRequestBuilder()


class CreateExternalApplicationRequestBuilder(object):

    def __init__(self, create_external_application_request: CreateExternalApplicationRequest = CreateExternalApplicationRequest()) -> None:
        create_external_application_request.http_method = HttpMethod.POST
        create_external_application_request.uri = "/open-apis/hire/v1/external_applications"
        create_external_application_request.token_types = {AccessTokenType.TENANT}
        self._create_external_application_request: CreateExternalApplicationRequest = create_external_application_request
    
    def request_body(self, request_body: ExternalApplication) -> "CreateExternalApplicationRequestBuilder":
        self._create_external_application_request.request_body = request_body
        self._create_external_application_request.body = request_body
        return self

    def build(self) -> CreateExternalApplicationRequest:
        return self._create_external_application_request
