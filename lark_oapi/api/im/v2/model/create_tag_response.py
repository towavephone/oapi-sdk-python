# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_tag_response_body import CreateTagResponseBody


class CreateTagResponse(BaseResponse):
    _types = {
        "data": CreateTagResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateTagResponseBody] = None
        init(self, d, self._types)
