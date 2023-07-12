# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class UploadFileRequestBody(object):
    _types = {
        "file": IO[Any],
    }

    def __init__(self, d):
        self.file: Optional[IO[Any]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UploadFileRequestBodyBuilder":
        return UploadFileRequestBodyBuilder()


class UploadFileRequestBodyBuilder(object):
    def __init__(self, upload_file_request_body: UploadFileRequestBody = UploadFileRequestBody({})) -> None:
        self._upload_file_request_body: UploadFileRequestBody = upload_file_request_body
    
    def file(self, file: IO[Any]) -> "UploadFileRequestBodyBuilder":
        self._upload_file_request_body.file = file
        return self
    
    def build(self) -> "UploadFileRequestBody":
        return self._upload_file_request_body