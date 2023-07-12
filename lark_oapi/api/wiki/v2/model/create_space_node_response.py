# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_space_node_response_body import CreateSpaceNodeResponseBody


class CreateSpaceNodeResponse(BaseResponse):
    _types = {
        "data": CreateSpaceNodeResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateSpaceNodeResponseBody] = None
        init(self, d, self._types)
