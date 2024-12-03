# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UnReadUrgentMessage(object):
    _types = {
        "id": str,
        "message_id": str,
        "chatter_id": str,
        "status": int,
        "confirm_time": str,
        "send_time": str,
        "type": int,
        "from_id": str,
        "chat_id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.message_id: Optional[str] = None
        self.chatter_id: Optional[str] = None
        self.status: Optional[int] = None
        self.confirm_time: Optional[str] = None
        self.send_time: Optional[str] = None
        self.type: Optional[int] = None
        self.from_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UnReadUrgentMessageBuilder":
        return UnReadUrgentMessageBuilder()


class UnReadUrgentMessageBuilder(object):
    def __init__(self) -> None:
        self._un_read_urgent_message = UnReadUrgentMessage()

    def id(self, id: str) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.id = id
        return self

    def message_id(self, message_id: str) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.message_id = message_id
        return self

    def chatter_id(self, chatter_id: str) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.chatter_id = chatter_id
        return self

    def status(self, status: int) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.status = status
        return self

    def confirm_time(self, confirm_time: str) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.confirm_time = confirm_time
        return self

    def send_time(self, send_time: str) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.send_time = send_time
        return self

    def type(self, type: int) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.type = type
        return self

    def from_id(self, from_id: str) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.from_id = from_id
        return self

    def chat_id(self, chat_id: str) -> "UnReadUrgentMessageBuilder":
        self._un_read_urgent_message.chat_id = chat_id
        return self

    def build(self) -> "UnReadUrgentMessage":
        return self._un_read_urgent_message
