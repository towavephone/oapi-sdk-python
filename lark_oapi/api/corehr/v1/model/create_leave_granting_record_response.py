# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_leave_granting_record_response_body import CreateLeaveGrantingRecordResponseBody


class CreateLeaveGrantingRecordResponse(BaseResponse):
    _types = {
        "data": CreateLeaveGrantingRecordResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateLeaveGrantingRecordResponseBody] = None
        init(self, d, self._types)
