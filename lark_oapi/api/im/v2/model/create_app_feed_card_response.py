# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_app_feed_card_response_body import CreateAppFeedCardResponseBody


class CreateAppFeedCardResponse(BaseResponse):
    _types = {
        "data": CreateAppFeedCardResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateAppFeedCardResponseBody] = None
        init(self, d, self._types)
