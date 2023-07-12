# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_shortcut_file_request_body import CreateShortcutFileRequestBody


class CreateShortcutFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateShortcutFileRequestBody] = None

    @staticmethod
    def builder() -> "CreateShortcutFileRequestBuilder":
        return CreateShortcutFileRequestBuilder()


class CreateShortcutFileRequestBuilder(object):

    def __init__(self, create_shortcut_file_request: CreateShortcutFileRequest = CreateShortcutFileRequest()) -> None:
        create_shortcut_file_request.http_method = HttpMethod.POST
        create_shortcut_file_request.uri = "/open-apis/drive/v1/files/create_shortcut"
        create_shortcut_file_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._create_shortcut_file_request: CreateShortcutFileRequest = create_shortcut_file_request
    
    def request_body(self, request_body: CreateShortcutFileRequestBody) -> "CreateShortcutFileRequestBuilder":
        self._create_shortcut_file_request.request_body = request_body
        self._create_shortcut_file_request.body = request_body
        return self

    def build(self) -> CreateShortcutFileRequest:
        return self._create_shortcut_file_request
