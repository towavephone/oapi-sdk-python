# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .chat_tab import ChatTab


class UpdateTabsChatTabRequestBody(object):
    _types = {
        "chat_tabs": List[ChatTab],
    }

    def __init__(self, d):
        self.chat_tabs: Optional[List[ChatTab]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateTabsChatTabRequestBodyBuilder":
        return UpdateTabsChatTabRequestBodyBuilder()


class UpdateTabsChatTabRequestBodyBuilder(object):
    def __init__(self, update_tabs_chat_tab_request_body: UpdateTabsChatTabRequestBody = UpdateTabsChatTabRequestBody({})) -> None:
        self._update_tabs_chat_tab_request_body: UpdateTabsChatTabRequestBody = update_tabs_chat_tab_request_body
    
    def chat_tabs(self, chat_tabs: List[ChatTab]) -> "UpdateTabsChatTabRequestBodyBuilder":
        self._update_tabs_chat_tab_request_body.chat_tabs = chat_tabs
        return self
    
    def build(self) -> "UpdateTabsChatTabRequestBody":
        return self._update_tabs_chat_tab_request_body