# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_entity_response_body import ListEntityResponseBody


class ListEntityResponse(BaseResponse):
    _types = {
        "data": ListEntityResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListEntityResponseBody] = None
        init(self, d, self._types)
