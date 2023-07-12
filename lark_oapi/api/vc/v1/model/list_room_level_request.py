# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListRoomLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.room_level_id: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListRoomLevelRequestBuilder":
        return ListRoomLevelRequestBuilder()


class ListRoomLevelRequestBuilder(object):

    def __init__(self, list_room_level_request: ListRoomLevelRequest = ListRoomLevelRequest()) -> None:
        list_room_level_request.http_method = HttpMethod.GET
        list_room_level_request.uri = "/open-apis/vc/v1/room_levels"
        list_room_level_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_room_level_request: ListRoomLevelRequest = list_room_level_request
    
    def room_level_id(self, room_level_id: str) -> "ListRoomLevelRequestBuilder":
        self._list_room_level_request.room_level_id = room_level_id
        self._list_room_level_request.queries["room_level_id"] = str(room_level_id)
        return self
    
    def page_size(self, page_size: int) -> "ListRoomLevelRequestBuilder":
        self._list_room_level_request.page_size = page_size
        self._list_room_level_request.queries["page_size"] = str(page_size)
        return self
    
    def page_token(self, page_token: str) -> "ListRoomLevelRequestBuilder":
        self._list_room_level_request.page_token = page_token
        self._list_room_level_request.queries["page_token"] = str(page_token)
        return self
    

    def build(self) -> ListRoomLevelRequest:
        return self._list_room_level_request
