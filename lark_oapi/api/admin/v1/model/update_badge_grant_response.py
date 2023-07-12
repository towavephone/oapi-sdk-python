# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_badge_grant_response_body import UpdateBadgeGrantResponseBody


class UpdateBadgeGrantResponse(BaseResponse):
    _types = {
        "data": UpdateBadgeGrantResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UpdateBadgeGrantResponseBody] = None
        init(self, d, self._types)
