# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .room_level import RoomLevel


class CreateRoomLevelResponseBody(object):
    _types = {
        "room_level": RoomLevel,
    }

    def __init__(self, d):
        self.room_level: Optional[RoomLevel] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateRoomLevelResponseBodyBuilder":
        return CreateRoomLevelResponseBodyBuilder()


class CreateRoomLevelResponseBodyBuilder(object):
    def __init__(self, create_room_level_response_body: CreateRoomLevelResponseBody = CreateRoomLevelResponseBody({})) -> None:
        self._create_room_level_response_body: CreateRoomLevelResponseBody = create_room_level_response_body
    
    def room_level(self, room_level: RoomLevel) -> "CreateRoomLevelResponseBodyBuilder":
        self._create_room_level_response_body.room_level = room_level
        return self
    
    def build(self) -> "CreateRoomLevelResponseBody":
        return self._create_room_level_response_body