# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_offer_response_body import ListOfferResponseBody


class ListOfferResponse(BaseResponse):
    _types = {
        "data": ListOfferResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListOfferResponseBody] = None
        init(self, d, self._types)
