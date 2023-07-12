# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .subscribe_event_request_body import SubscribeEventRequestBody


class SubscribeEventRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[SubscribeEventRequestBody] = None

    @staticmethod
    def builder() -> "SubscribeEventRequestBuilder":
        return SubscribeEventRequestBuilder()


class SubscribeEventRequestBuilder(object):

    def __init__(self, subscribe_event_request: SubscribeEventRequest = SubscribeEventRequest()) -> None:
        subscribe_event_request.http_method = HttpMethod.POST
        subscribe_event_request.uri = "/open-apis/helpdesk/v1/events/subscribe"
        subscribe_event_request.token_types = {AccessTokenType.TENANT}
        self._subscribe_event_request: SubscribeEventRequest = subscribe_event_request
    
    def request_body(self, request_body: SubscribeEventRequestBody) -> "SubscribeEventRequestBuilder":
        self._subscribe_event_request.request_body = request_body
        self._subscribe_event_request.body = request_body
        return self

    def build(self) -> SubscribeEventRequest:
        return self._subscribe_event_request
