# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .chat_tab import ChatTab


class CreateChatTabRequestBody(object):
    _types = {
        "chat_tabs": List[ChatTab],
    }

    def __init__(self, d):
        self.chat_tabs: Optional[List[ChatTab]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateChatTabRequestBodyBuilder":
        return CreateChatTabRequestBodyBuilder()


class CreateChatTabRequestBodyBuilder(object):
    def __init__(self, create_chat_tab_request_body: CreateChatTabRequestBody = CreateChatTabRequestBody({})) -> None:
        self._create_chat_tab_request_body: CreateChatTabRequestBody = create_chat_tab_request_body
    
    def chat_tabs(self, chat_tabs: List[ChatTab]) -> "CreateChatTabRequestBodyBuilder":
        self._create_chat_tab_request_body.chat_tabs = chat_tabs
        return self
    
    def build(self) -> "CreateChatTabRequestBody":
        return self._create_chat_tab_request_body