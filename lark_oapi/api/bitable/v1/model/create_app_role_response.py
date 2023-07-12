# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_app_role_response_body import CreateAppRoleResponseBody


class CreateAppRoleResponse(BaseResponse):
    _types = {
        "data": CreateAppRoleResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateAppRoleResponseBody] = None
        init(self, d, self._types)
