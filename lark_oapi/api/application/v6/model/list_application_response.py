# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_application_response_body import ListApplicationResponseBody


class ListApplicationResponse(BaseResponse):
    _types = {
        "data": ListApplicationResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListApplicationResponseBody] = None
        init(self, d, self._types)
