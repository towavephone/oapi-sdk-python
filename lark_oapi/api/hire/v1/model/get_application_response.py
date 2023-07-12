# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_application_response_body import GetApplicationResponseBody


class GetApplicationResponse(BaseResponse):
    _types = {
        "data": GetApplicationResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetApplicationResponseBody] = None
        init(self, d, self._types)
