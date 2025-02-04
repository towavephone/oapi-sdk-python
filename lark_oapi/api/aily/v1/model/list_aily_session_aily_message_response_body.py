# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .aily_message import AilyMessage


class ListAilySessionAilyMessageResponseBody(object):
    _types = {
        "messages": List[AilyMessage],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.messages: Optional[List[AilyMessage]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAilySessionAilyMessageResponseBodyBuilder":
        return ListAilySessionAilyMessageResponseBodyBuilder()


class ListAilySessionAilyMessageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_aily_session_aily_message_response_body = ListAilySessionAilyMessageResponseBody()

    def messages(self, messages: List[AilyMessage]) -> "ListAilySessionAilyMessageResponseBodyBuilder":
        self._list_aily_session_aily_message_response_body.messages = messages
        return self

    def page_token(self, page_token: str) -> "ListAilySessionAilyMessageResponseBodyBuilder":
        self._list_aily_session_aily_message_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListAilySessionAilyMessageResponseBodyBuilder":
        self._list_aily_session_aily_message_response_body.has_more = has_more
        return self

    def build(self) -> "ListAilySessionAilyMessageResponseBody":
        return self._list_aily_session_aily_message_response_body
