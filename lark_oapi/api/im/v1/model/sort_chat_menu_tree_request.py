# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .sort_chat_menu_tree_request_body import SortChatMenuTreeRequestBody


class SortChatMenuTreeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None
        self.request_body: Optional[SortChatMenuTreeRequestBody] = None

    @staticmethod
    def builder() -> "SortChatMenuTreeRequestBuilder":
        return SortChatMenuTreeRequestBuilder()


class SortChatMenuTreeRequestBuilder(object):

    def __init__(self, sort_chat_menu_tree_request: SortChatMenuTreeRequest = SortChatMenuTreeRequest()) -> None:
        sort_chat_menu_tree_request.http_method = HttpMethod.POST
        sort_chat_menu_tree_request.uri = "/open-apis/im/v1/chats/:chat_id/menu_tree/sort"
        sort_chat_menu_tree_request.token_types = {AccessTokenType.TENANT}
        self._sort_chat_menu_tree_request: SortChatMenuTreeRequest = sort_chat_menu_tree_request
    
    def chat_id(self, chat_id: str) -> "SortChatMenuTreeRequestBuilder":
        self._sort_chat_menu_tree_request.chat_id = chat_id
        self._sort_chat_menu_tree_request.paths["chat_id"] = chat_id
        return self
    
    def request_body(self, request_body: SortChatMenuTreeRequestBody) -> "SortChatMenuTreeRequestBuilder":
        self._sort_chat_menu_tree_request.request_body = request_body
        self._sort_chat_menu_tree_request.body = request_body
        return self

    def build(self) -> SortChatMenuTreeRequest:
        return self._sort_chat_menu_tree_request
