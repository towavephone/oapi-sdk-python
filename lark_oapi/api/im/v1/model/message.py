# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .sender import Sender
from .message_body import MessageBody
from .mention import Mention


class Message(object):
    _types = {
        "message_id": str,
        "root_id": str,
        "parent_id": str,
        "msg_type": str,
        "create_time": int,
        "update_time": int,
        "deleted": bool,
        "updated": bool,
        "chat_id": str,
        "sender": Sender,
        "body": MessageBody,
        "mentions": List[Mention],
        "upper_message_id": str,
    }

    def __init__(self, d):
        self.message_id: Optional[str] = None
        self.root_id: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.msg_type: Optional[str] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        self.deleted: Optional[bool] = None
        self.updated: Optional[bool] = None
        self.chat_id: Optional[str] = None
        self.sender: Optional[Sender] = None
        self.body: Optional[MessageBody] = None
        self.mentions: Optional[List[Mention]] = None
        self.upper_message_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MessageBuilder":
        return MessageBuilder()


class MessageBuilder(object):
    def __init__(self, message: Message = Message({})) -> None:
        self._message: Message = message
    
    def message_id(self, message_id: str) -> "MessageBuilder":
        self._message.message_id = message_id
        return self
    
    def root_id(self, root_id: str) -> "MessageBuilder":
        self._message.root_id = root_id
        return self
    
    def parent_id(self, parent_id: str) -> "MessageBuilder":
        self._message.parent_id = parent_id
        return self
    
    def msg_type(self, msg_type: str) -> "MessageBuilder":
        self._message.msg_type = msg_type
        return self
    
    def create_time(self, create_time: int) -> "MessageBuilder":
        self._message.create_time = create_time
        return self
    
    def update_time(self, update_time: int) -> "MessageBuilder":
        self._message.update_time = update_time
        return self
    
    def deleted(self, deleted: bool) -> "MessageBuilder":
        self._message.deleted = deleted
        return self
    
    def updated(self, updated: bool) -> "MessageBuilder":
        self._message.updated = updated
        return self
    
    def chat_id(self, chat_id: str) -> "MessageBuilder":
        self._message.chat_id = chat_id
        return self
    
    def sender(self, sender: Sender) -> "MessageBuilder":
        self._message.sender = sender
        return self
    
    def body(self, body: MessageBody) -> "MessageBuilder":
        self._message.body = body
        return self
    
    def mentions(self, mentions: List[Mention]) -> "MessageBuilder":
        self._message.mentions = mentions
        return self
    
    def upper_message_id(self, upper_message_id: str) -> "MessageBuilder":
        self._message.upper_message_id = upper_message_id
        return self
    
    def build(self) -> "Message":
        return self._message