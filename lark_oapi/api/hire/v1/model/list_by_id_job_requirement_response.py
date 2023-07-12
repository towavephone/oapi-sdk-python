# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_by_id_job_requirement_response_body import ListByIdJobRequirementResponseBody


class ListByIdJobRequirementResponse(BaseResponse):
    _types = {
        "data": ListByIdJobRequirementResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListByIdJobRequirementResponseBody] = None
        init(self, d, self._types)
