# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_interview_feedback_form_response_body import ListInterviewFeedbackFormResponseBody


class ListInterviewFeedbackFormResponse(BaseResponse):
    _types = {
        "data": ListInterviewFeedbackFormResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListInterviewFeedbackFormResponseBody] = None
        init(self, d, self._types)
