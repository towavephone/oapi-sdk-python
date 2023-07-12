# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_participant_list_response_body import GetParticipantListResponseBody


class GetParticipantListResponse(BaseResponse):
    _types = {
        "data": GetParticipantListResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetParticipantListResponseBody] = None
        init(self, d, self._types)
