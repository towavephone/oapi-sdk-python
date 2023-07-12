# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_delete_follower_task_response_body import BatchDeleteFollowerTaskResponseBody


class BatchDeleteFollowerTaskResponse(BaseResponse):
    _types = {
        "data": BatchDeleteFollowerTaskResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[BatchDeleteFollowerTaskResponseBody] = None
        init(self, d, self._types)
