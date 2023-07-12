# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .basic_recognize_image_response_body import BasicRecognizeImageResponseBody


class BasicRecognizeImageResponse(BaseResponse):
    _types = {
        "data": BasicRecognizeImageResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[BasicRecognizeImageResponseBody] = None
        init(self, d, self._types)
