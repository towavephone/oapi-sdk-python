# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetRoomRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.room_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetRoomRequestBuilder":
        return GetRoomRequestBuilder()


class GetRoomRequestBuilder(object):

    def __init__(self) -> None:
        get_room_request = GetRoomRequest()
        get_room_request.http_method = HttpMethod.GET
        get_room_request.uri = "/open-apis/vc/v1/rooms/:room_id"
        get_room_request.token_types = {AccessTokenType.TENANT}
        self._get_room_request: GetRoomRequest = get_room_request

    def user_id_type(self, user_id_type: str) -> "GetRoomRequestBuilder":
        self._get_room_request.user_id_type = user_id_type
        self._get_room_request.add_query("user_id_type", user_id_type)
        return self

    def room_id(self, room_id: str) -> "GetRoomRequestBuilder":
        self._get_room_request.room_id = room_id
        self._get_room_request.paths["room_id"] = str(room_id)
        return self

    def build(self) -> GetRoomRequest:
        return self._get_room_request
