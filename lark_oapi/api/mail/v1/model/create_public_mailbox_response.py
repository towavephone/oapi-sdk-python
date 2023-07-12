# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_public_mailbox_response_body import CreatePublicMailboxResponseBody


class CreatePublicMailboxResponse(BaseResponse):
    _types = {
        "data": CreatePublicMailboxResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreatePublicMailboxResponseBody] = None
        init(self, d, self._types)
