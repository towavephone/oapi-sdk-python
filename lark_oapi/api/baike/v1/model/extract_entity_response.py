# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .extract_entity_response_body import ExtractEntityResponseBody


class ExtractEntityResponse(BaseResponse):
    _types = {
        "data": ExtractEntityResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ExtractEntityResponseBody] = None
        init(self, d, self._types)
