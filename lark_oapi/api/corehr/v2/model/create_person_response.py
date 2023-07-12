# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_person_response_body import CreatePersonResponseBody


class CreatePersonResponse(BaseResponse):
    _types = {
        "data": CreatePersonResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreatePersonResponseBody] = None
        init(self, d, self._types)
