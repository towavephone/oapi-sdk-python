# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_app_table_form_response_body import GetAppTableFormResponseBody


class GetAppTableFormResponse(BaseResponse):
    _types = {
        "data": GetAppTableFormResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetAppTableFormResponseBody] = None
        init(self, d, self._types)
