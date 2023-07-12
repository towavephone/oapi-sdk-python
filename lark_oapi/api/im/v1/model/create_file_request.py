# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_file_request_body import CreateFileRequestBody


class CreateFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateFileRequestBody] = None

    @staticmethod
    def builder() -> "CreateFileRequestBuilder":
        return CreateFileRequestBuilder()


class CreateFileRequestBuilder(object):

    def __init__(self, create_file_request: CreateFileRequest = CreateFileRequest()) -> None:
        create_file_request.http_method = HttpMethod.POST
        create_file_request.uri = "/open-apis/im/v1/files"
        create_file_request.token_types = {AccessTokenType.TENANT}
        self._create_file_request: CreateFileRequest = create_file_request
    
    def request_body(self, request_body: CreateFileRequestBody) -> "CreateFileRequestBuilder":
        self._create_file_request.request_body = request_body
        self._create_file_request.body = request_body
        return self

    def build(self) -> CreateFileRequest:
        return self._create_file_request
