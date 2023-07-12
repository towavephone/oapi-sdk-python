# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_faq_response_body import CreateFaqResponseBody


class CreateFaqResponse(BaseResponse):
    _types = {
        "data": CreateFaqResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateFaqResponseBody] = None
        init(self, d, self._types)
