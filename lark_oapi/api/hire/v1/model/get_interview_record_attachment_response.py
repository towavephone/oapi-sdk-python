# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_interview_record_attachment_response_body import GetInterviewRecordAttachmentResponseBody


class GetInterviewRecordAttachmentResponse(BaseResponse):
    _types = {
        "data": GetInterviewRecordAttachmentResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetInterviewRecordAttachmentResponseBody] = None
        init(self, d, self._types)
