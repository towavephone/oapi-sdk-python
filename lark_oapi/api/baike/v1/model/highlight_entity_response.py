# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .highlight_entity_response_body import HighlightEntityResponseBody


class HighlightEntityResponse(BaseResponse):
    _types = {
        "data": HighlightEntityResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[HighlightEntityResponseBody] = None
        init(self, d, self._types)
