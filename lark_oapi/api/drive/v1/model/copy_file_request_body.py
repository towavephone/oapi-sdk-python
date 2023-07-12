# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .property import Property


class CopyFileRequestBody(object):
    _types = {
        "name": str,
        "type": str,
        "folder_token": str,
        "extra": List[Property],
    }

    def __init__(self, d):
        self.name: Optional[str] = None
        self.type: Optional[str] = None
        self.folder_token: Optional[str] = None
        self.extra: Optional[List[Property]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CopyFileRequestBodyBuilder":
        return CopyFileRequestBodyBuilder()


class CopyFileRequestBodyBuilder(object):
    def __init__(self, copy_file_request_body: CopyFileRequestBody = CopyFileRequestBody({})) -> None:
        self._copy_file_request_body: CopyFileRequestBody = copy_file_request_body
    
    def name(self, name: str) -> "CopyFileRequestBodyBuilder":
        self._copy_file_request_body.name = name
        return self
    
    def type(self, type: str) -> "CopyFileRequestBodyBuilder":
        self._copy_file_request_body.type = type
        return self
    
    def folder_token(self, folder_token: str) -> "CopyFileRequestBodyBuilder":
        self._copy_file_request_body.folder_token = folder_token
        return self
    
    def extra(self, extra: List[Property]) -> "CopyFileRequestBodyBuilder":
        self._copy_file_request_body.extra = extra
        return self
    
    def build(self) -> "CopyFileRequestBody":
        return self._copy_file_request_body