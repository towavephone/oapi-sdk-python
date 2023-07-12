# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class CreateTicketMessageRequestBody(object):
    _types = {
        "msg_type": str,
        "content": str,
    }

    def __init__(self, d):
        self.msg_type: Optional[str] = None
        self.content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateTicketMessageRequestBodyBuilder":
        return CreateTicketMessageRequestBodyBuilder()


class CreateTicketMessageRequestBodyBuilder(object):
    def __init__(self, create_ticket_message_request_body: CreateTicketMessageRequestBody = CreateTicketMessageRequestBody({})) -> None:
        self._create_ticket_message_request_body: CreateTicketMessageRequestBody = create_ticket_message_request_body
    
    def msg_type(self, msg_type: str) -> "CreateTicketMessageRequestBodyBuilder":
        self._create_ticket_message_request_body.msg_type = msg_type
        return self
    
    def content(self, content: str) -> "CreateTicketMessageRequestBodyBuilder":
        self._create_ticket_message_request_body.content = content
        return self
    
    def build(self) -> "CreateTicketMessageRequestBody":
        return self._create_ticket_message_request_body