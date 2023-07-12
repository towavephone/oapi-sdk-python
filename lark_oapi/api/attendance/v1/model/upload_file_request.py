# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .upload_file_request_body import UploadFileRequestBody


class UploadFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_name: Optional[str] = None
        self.request_body: Optional[UploadFileRequestBody] = None

    @staticmethod
    def builder() -> "UploadFileRequestBuilder":
        return UploadFileRequestBuilder()


class UploadFileRequestBuilder(object):

    def __init__(self, upload_file_request: UploadFileRequest = UploadFileRequest()) -> None:
        upload_file_request.http_method = HttpMethod.POST
        upload_file_request.uri = "/open-apis/attendance/v1/files/upload"
        upload_file_request.token_types = {AccessTokenType.TENANT}
        self._upload_file_request: UploadFileRequest = upload_file_request
    
    def file_name(self, file_name: str) -> "UploadFileRequestBuilder":
        self._upload_file_request.file_name = file_name
        self._upload_file_request.queries["file_name"] = str(file_name)
        return self
    
    def request_body(self, request_body: UploadFileRequestBody) -> "UploadFileRequestBuilder":
        self._upload_file_request.request_body = request_body
        self._upload_file_request.body = request_body
        return self

    def build(self) -> UploadFileRequest:
        return self._upload_file_request
