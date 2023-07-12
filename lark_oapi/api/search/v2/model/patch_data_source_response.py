# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_data_source_response_body import PatchDataSourceResponseBody


class PatchDataSourceResponse(BaseResponse):
    _types = {
        "data": PatchDataSourceResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[PatchDataSourceResponseBody] = None
        init(self, d, self._types)
