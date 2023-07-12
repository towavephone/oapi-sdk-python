# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .unread_special_focus_request_body import UnreadSpecialFocusRequestBody


class UnreadSpecialFocusRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.member_id_type: Optional[str] = None
        self.request_body: Optional[UnreadSpecialFocusRequestBody] = None

    @staticmethod
    def builder() -> "UnreadSpecialFocusRequestBuilder":
        return UnreadSpecialFocusRequestBuilder()


class UnreadSpecialFocusRequestBuilder(object):

    def __init__(self, unread_special_focus_request: UnreadSpecialFocusRequest = UnreadSpecialFocusRequest()) -> None:
        unread_special_focus_request.http_method = HttpMethod.POST
        unread_special_focus_request.uri = "/open-apis/im/v1/special_focus/unread"
        unread_special_focus_request.token_types = {AccessTokenType.USER}
        self._unread_special_focus_request: UnreadSpecialFocusRequest = unread_special_focus_request
    
    def member_id_type(self, member_id_type: str) -> "UnreadSpecialFocusRequestBuilder":
        self._unread_special_focus_request.member_id_type = member_id_type
        self._unread_special_focus_request.queries["member_id_type"] = str(member_id_type)
        return self
    
    def request_body(self, request_body: UnreadSpecialFocusRequestBody) -> "UnreadSpecialFocusRequestBuilder":
        self._unread_special_focus_request.request_body = request_body
        self._unread_special_focus_request.body = request_body
        return self

    def build(self) -> UnreadSpecialFocusRequest:
        return self._unread_special_focus_request
