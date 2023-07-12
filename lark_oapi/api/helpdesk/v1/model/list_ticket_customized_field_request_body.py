# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class ListTicketCustomizedFieldRequestBody(object):
    _types = {
        "visible": bool,
    }

    def __init__(self, d):
        self.visible: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTicketCustomizedFieldRequestBodyBuilder":
        return ListTicketCustomizedFieldRequestBodyBuilder()


class ListTicketCustomizedFieldRequestBodyBuilder(object):
    def __init__(self, list_ticket_customized_field_request_body: ListTicketCustomizedFieldRequestBody = ListTicketCustomizedFieldRequestBody({})) -> None:
        self._list_ticket_customized_field_request_body: ListTicketCustomizedFieldRequestBody = list_ticket_customized_field_request_body
    
    def visible(self, visible: bool) -> "ListTicketCustomizedFieldRequestBodyBuilder":
        self._list_ticket_customized_field_request_body.visible = visible
        return self
    
    def build(self) -> "ListTicketCustomizedFieldRequestBody":
        return self._list_ticket_customized_field_request_body