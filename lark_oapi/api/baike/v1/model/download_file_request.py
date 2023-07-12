# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class DownloadFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_token: Optional[str] = None

    @staticmethod
    def builder() -> "DownloadFileRequestBuilder":
        return DownloadFileRequestBuilder()


class DownloadFileRequestBuilder(object):

    def __init__(self, download_file_request: DownloadFileRequest = DownloadFileRequest()) -> None:
        download_file_request.http_method = HttpMethod.GET
        download_file_request.uri = "/open-apis/baike/v1/files/:file_token/download"
        download_file_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._download_file_request: DownloadFileRequest = download_file_request
    
    def file_token(self, file_token: str) -> "DownloadFileRequestBuilder":
        self._download_file_request.file_token = file_token
        self._download_file_request.paths["file_token"] = file_token
        return self
    

    def build(self) -> DownloadFileRequest:
        return self._download_file_request
