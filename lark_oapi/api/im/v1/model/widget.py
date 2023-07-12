# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .widget_url import WidgetUrl


class Widget(object):
    _types = {
        "widget_id": int,
        "widget_type": str,
        "widget_url": WidgetUrl,
    }

    def __init__(self, d):
        self.widget_id: Optional[int] = None
        self.widget_type: Optional[str] = None
        self.widget_url: Optional[WidgetUrl] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WidgetBuilder":
        return WidgetBuilder()


class WidgetBuilder(object):
    def __init__(self, widget: Widget = Widget({})) -> None:
        self._widget: Widget = widget
    
    def widget_id(self, widget_id: int) -> "WidgetBuilder":
        self._widget.widget_id = widget_id
        return self
    
    def widget_type(self, widget_type: str) -> "WidgetBuilder":
        self._widget.widget_type = widget_type
        return self
    
    def widget_url(self, widget_url: WidgetUrl) -> "WidgetBuilder":
        self._widget.widget_url = widget_url
        return self
    
    def build(self) -> "Widget":
        return self._widget