# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_file_version_response_body import GetFileVersionResponseBody


class GetFileVersionResponse(BaseResponse):
    _types = {
        "data": GetFileVersionResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetFileVersionResponseBody] = None
        init(self, d, self._types)
