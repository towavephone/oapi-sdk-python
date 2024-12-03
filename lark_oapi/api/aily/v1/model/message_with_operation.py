# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .message import Message


class MessageWithOperation(object):
    _types = {
        "message": Message,
        "operation_type": str,
        "operation_id": int,
        "intent_id": int,
    }

    def __init__(self, d=None):
        self.message: Optional[Message] = None
        self.operation_type: Optional[str] = None
        self.operation_id: Optional[int] = None
        self.intent_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MessageWithOperationBuilder":
        return MessageWithOperationBuilder()


class MessageWithOperationBuilder(object):
    def __init__(self) -> None:
        self._message_with_operation = MessageWithOperation()

    def message(self, message: Message) -> "MessageWithOperationBuilder":
        self._message_with_operation.message = message
        return self

    def operation_type(self, operation_type: str) -> "MessageWithOperationBuilder":
        self._message_with_operation.operation_type = operation_type
        return self

    def operation_id(self, operation_id: int) -> "MessageWithOperationBuilder":
        self._message_with_operation.operation_id = operation_id
        return self

    def intent_id(self, intent_id: int) -> "MessageWithOperationBuilder":
        self._message_with_operation.intent_id = intent_id
        return self

    def build(self) -> "MessageWithOperation":
        return self._message_with_operation
