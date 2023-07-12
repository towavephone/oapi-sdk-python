# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_task_reminder_response_body import ListTaskReminderResponseBody


class ListTaskReminderResponse(BaseResponse):
    _types = {
        "data": ListTaskReminderResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListTaskReminderResponseBody] = None
        init(self, d, self._types)
