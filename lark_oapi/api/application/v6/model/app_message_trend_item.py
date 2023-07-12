# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .usage_trend_item import UsageTrendItem


class AppMessageTrendItem(object):
    _types = {
        "chat_type": str,
        "event_type": str,
        "message_type": str,
        "trend": List[UsageTrendItem],
    }

    def __init__(self, d):
        self.chat_type: Optional[str] = None
        self.event_type: Optional[str] = None
        self.message_type: Optional[str] = None
        self.trend: Optional[List[UsageTrendItem]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppMessageTrendItemBuilder":
        return AppMessageTrendItemBuilder()


class AppMessageTrendItemBuilder(object):
    def __init__(self, app_message_trend_item: AppMessageTrendItem = AppMessageTrendItem({})) -> None:
        self._app_message_trend_item: AppMessageTrendItem = app_message_trend_item
    
    def chat_type(self, chat_type: str) -> "AppMessageTrendItemBuilder":
        self._app_message_trend_item.chat_type = chat_type
        return self
    
    def event_type(self, event_type: str) -> "AppMessageTrendItemBuilder":
        self._app_message_trend_item.event_type = event_type
        return self
    
    def message_type(self, message_type: str) -> "AppMessageTrendItemBuilder":
        self._app_message_trend_item.message_type = message_type
        return self
    
    def trend(self, trend: List[UsageTrendItem]) -> "AppMessageTrendItemBuilder":
        self._app_message_trend_item.trend = trend
        return self
    
    def build(self) -> "AppMessageTrendItem":
        return self._app_message_trend_item