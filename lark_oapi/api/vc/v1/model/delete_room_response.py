# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse


class DeleteRoomResponse(BaseResponse):
    _types = {
        
    }

    def __init__(self, d):
        super().__init__(d)
        
        init(self, d, self._types)
