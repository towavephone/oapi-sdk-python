# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .customized_fields_ticket_response_body import CustomizedFieldsTicketResponseBody


class CustomizedFieldsTicketResponse(BaseResponse):
    _types = {
        "data": CustomizedFieldsTicketResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CustomizedFieldsTicketResponseBody] = None
        init(self, d, self._types)
