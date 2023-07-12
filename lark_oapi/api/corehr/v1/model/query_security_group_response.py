# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_security_group_response_body import QuerySecurityGroupResponseBody


class QuerySecurityGroupResponse(BaseResponse):
    _types = {
        "data": QuerySecurityGroupResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[QuerySecurityGroupResponseBody] = None
        init(self, d, self._types)
