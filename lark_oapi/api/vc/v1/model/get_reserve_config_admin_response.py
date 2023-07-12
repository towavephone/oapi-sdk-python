# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_reserve_config_admin_response_body import GetReserveConfigAdminResponseBody


class GetReserveConfigAdminResponse(BaseResponse):
    _types = {
        "data": GetReserveConfigAdminResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetReserveConfigAdminResponseBody] = None
        init(self, d, self._types)
