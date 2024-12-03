# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_interviewer_response_body import ListInterviewerResponseBody


class ListInterviewerResponse(BaseResponse):
    _types = {
        "data": ListInterviewerResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListInterviewerResponseBody] = None
        init(self, d, self._types)
