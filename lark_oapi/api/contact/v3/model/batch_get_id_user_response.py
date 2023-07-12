# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_get_id_user_response_body import BatchGetIdUserResponseBody


class BatchGetIdUserResponse(BaseResponse):
    _types = {
        "data": BatchGetIdUserResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[BatchGetIdUserResponseBody] = None
        init(self, d, self._types)
