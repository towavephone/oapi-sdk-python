# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class WebApp(object):
    _types = {
        "pc_url": str,
        "mobile_url": str,
    }

    def __init__(self, d):
        self.pc_url: Optional[str] = None
        self.mobile_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebAppBuilder":
        return WebAppBuilder()


class WebAppBuilder(object):
    def __init__(self, web_app: WebApp = WebApp({})) -> None:
        self._web_app: WebApp = web_app
    
    def pc_url(self, pc_url: str) -> "WebAppBuilder":
        self._web_app.pc_url = pc_url
        return self
    
    def mobile_url(self, mobile_url: str) -> "WebAppBuilder":
        self._web_app.mobile_url = mobile_url
        return self
    
    def build(self) -> "WebApp":
        return self._web_app