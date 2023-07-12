# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .del_room_level_request_body import DelRoomLevelRequestBody


class DelRoomLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[DelRoomLevelRequestBody] = None

    @staticmethod
    def builder() -> "DelRoomLevelRequestBuilder":
        return DelRoomLevelRequestBuilder()


class DelRoomLevelRequestBuilder(object):

    def __init__(self, del_room_level_request: DelRoomLevelRequest = DelRoomLevelRequest()) -> None:
        del_room_level_request.http_method = HttpMethod.POST
        del_room_level_request.uri = "/open-apis/vc/v1/room_levels/del"
        del_room_level_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._del_room_level_request: DelRoomLevelRequest = del_room_level_request
    
    def request_body(self, request_body: DelRoomLevelRequestBody) -> "DelRoomLevelRequestBuilder":
        self._del_room_level_request.request_body = request_body
        self._del_room_level_request.body = request_body
        return self

    def build(self) -> DelRoomLevelRequest:
        return self._del_room_level_request
